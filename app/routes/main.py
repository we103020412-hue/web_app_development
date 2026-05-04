from flask import Blueprint, render_template, request
from app.models.region import Region
from app.models.weather import WeatherForecast

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """首頁：顯示天氣與查詢面板"""
    # 取得查詢參數
    region_id = request.args.get('region_id', type=int)
    date = request.args.get('date')
    time_period = request.args.get('time_period')

    # 取得選單資料
    regions = Region.get_all()

    # 取得天氣預報資料
    forecasts = WeatherForecast.get_forecasts(region_id, date, time_period)

    return render_template(
        'index.html', 
        regions=regions, 
        forecasts=forecasts,
        selected_region=region_id,
        selected_date=date,
        selected_time=time_period
    )
