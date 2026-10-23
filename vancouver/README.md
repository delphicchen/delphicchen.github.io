# 溫哥華景點整理

依區域整理的大溫哥華景點頁，手機打開 `index.html`（或 GitHub Pages 網址）即可使用：分頁切換區域，地圖標出 SkyTrain 三條線和景點，每張卡片可直接開 Google 地圖或 Uber 導航。

## 怎麼改內容

只改 `guide.json`，再執行：

```
python3 build.py
```

會重新產生 `index.html`。`guide.json` 結構：

- `areas`：每個區域一筆，`name`、`sub`（副標）、`note`（橘色提醒）、`spots`（景點）。
  - `spots` 每一筆：`p` 地點代碼、`d` 說明、`m` 建議交通（`canada`、`expo`、`millennium`、`uber`、`ferry`、`walk`）、`tags`（例如 `免費`、`室內`、`網購`、`親子`）。
- `places`：地點資料，`zh`、`n`（英文名）、`lat`、`lon`、`q`（Google 地圖搜尋字串），可加 `fee`（票價）、`buy`（購票網址）。
- `stations`、`lines`：SkyTrain 車站和路線，一般不用改。

## 資料來源

- 底圖：[OpenStreetMap](https://www.openstreetmap.org/copyright)；地圖程式庫：[Leaflet](https://leafletjs.com/) 1.9.4（BSD-2-Clause，見 `vendor/`）
- 車站座標：Wikipedia；路線以直線連接各站，僅示意
- 票價：各景點官網、Vancouver Tourism、TransLink 等 2026 年網路資料，僅供參考
