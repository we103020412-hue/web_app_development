DROP TABLE IF EXISTS weather_forecasts;
DROP TABLE IF EXISTS regions;

CREATE TABLE regions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE weather_forecasts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    region_id INTEGER NOT NULL,
    forecast_date TEXT NOT NULL,
    time_period TEXT NOT NULL,
    condition TEXT NOT NULL,
    temperature INTEGER NOT NULL,
    FOREIGN KEY (region_id) REFERENCES regions (id)
);

-- Insert Mock Data
INSERT INTO regions (name) VALUES ('台北市'), ('新北市'), ('台中市'), ('台南市'), ('高雄市');

INSERT INTO weather_forecasts (region_id, forecast_date, time_period, condition, temperature) VALUES 
(1, '2026-05-04', '早上', '晴朗', 28),
(1, '2026-05-04', '下午', '多雲', 30),
(1, '2026-05-04', '晚上', '陰天', 25),
(2, '2026-05-04', '早上', '晴朗', 27),
(2, '2026-05-04', '下午', '下雨', 26),
(2, '2026-05-04', '晚上', '下雨', 24),
(3, '2026-05-04', '早上', '晴朗', 29),
(3, '2026-05-04', '下午', '晴朗', 32),
(3, '2026-05-04', '晚上', '多雲', 28),
(5, '2026-05-04', '早上', '多雲', 30),
(5, '2026-05-04', '下午', '多雲', 33),
(5, '2026-05-04', '晚上', '晴朗', 29);
