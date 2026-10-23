"""產生 index.html（單一檔案，地圖程式庫與景點資料都內嵌）。

用法：python3 build.py
只需要 Python 3，不用安裝任何套件。
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).parent
g = json.loads((ROOT / "guide.json").read_text(encoding="utf-8"))

errors = []
for a in g["areas"]:
    for key in ("key", "name", "sub", "spots"):
        if key not in a:
            errors.append(f"區域 {a.get('name','?')} 缺少欄位 {key}")
    for s in a.get("spots", []):
        if s.get("p") not in g["places"]:
            errors.append(f"{a.get('name')}：找不到地點 '{s.get('p')}'（請先在 places 新增）")
for pid, p in g["places"].items():
    for key in ("zh", "lat", "lon", "q"):
        if key not in p:
            errors.append(f"地點 {pid} 缺少欄位 {key}")
if errors:
    print("guide.json 有問題：\n  " + "\n  ".join(errors))
    sys.exit(1)

data_js = json.dumps(g, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
js = (ROOT / "vendor/leaflet.js").read_text(encoding="utf-8")
js = re.sub(r"//# sourceMappingURL=\S+", "", js).replace("</script", "<\\/script")
css = (ROOT / "vendor/leaflet.css").read_text(encoding="utf-8")
css = re.sub(r"/\*# sourceMappingURL=\S+ \*/", "", css)

html = (ROOT / "template.html").read_text(encoding="utf-8")
html = html.replace("/*LEAFLET_CSS*/", css).replace("/*LEAFLET_JS*/", js).replace("/*DATA*/", data_js)
(ROOT / "index.html").write_text(html, encoding="utf-8")
n = sum(len(a["spots"]) for a in g["areas"])
print(f"已產生 index.html（{len(html)//1024} KB，{len(g['areas'])} 區，{n} 個景點）")
