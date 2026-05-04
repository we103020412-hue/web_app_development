# 路由設計 (API Design) - 天氣預報系統

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 首頁與天氣查詢 | GET | `/` | `templates/index.html` | 顯示所有地區選單，並根據查詢參數 (Query Parameters) 顯示對應的天氣預報資料。預設顯示所有地區的今日天氣。 |

> **說明**：由於天氣系統主要為「查詢」與「顯示」資料，因此我們只需要一個強大的首頁路由，透過 `GET` 請求附加查詢參數來篩選資料，例如 `/?region_id=1&date=2026-05-04&time_period=早上`。這樣做也符合 RESTful 設計，且讓使用者能夠將特定的查詢結果加入書籤分享。

## 2. 每個路由的詳細說明

### `GET /` (首頁與查詢面板)
- **輸入 (URL 參數)**：
  - `region_id` (可選)：指定地區 ID。
  - `date` (可選)：指定預報日期 (YYYY-MM-DD)。
  - `time_period` (可選)：指定時段 (早上、下午、晚上)。
- **處理邏輯**：
  1. 呼叫 `Region.get_all()` 取得所有地區資料，供前端渲染下拉選單。
  2. 從 `request.args` 取得篩選條件。
  3. 呼叫 `WeatherForecast.get_forecasts(region_id, date, time_period)` 取得過濾後的天氣資料。
- **輸出**：
  - 渲染 `index.html`，並將地區清單與天氣資料傳入。
- **錯誤處理**：
  - 若 `region_id` 格式錯誤或找不到，則忽略該條件或設為預設值。

## 3. Jinja2 模板清單

| 檔案名稱 | 說明 | 繼承關係 |
| --- | --- | --- |
| `base.html` | 包含 HTML 架構、Bootstrap CDN、共用 Navbar（導覽列）與頁尾。 | - |
| `index.html` | 包含查詢表單（選擇地區、日期、時間）與天氣卡片顯示區塊。 | 繼承 `base.html` |

## 4. 路由骨架程式碼規劃

將建立 `app/routes/main.py` 作為主要路由檔案，定義 `Blueprint` 並實作上述邏輯。
