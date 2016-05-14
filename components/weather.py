import datetime
import forecastio
import pytz
from flask import current_app



def get_weather():
    lat = current_app.config.get('LATITUDE')
    lon = current_app.config.get('LONGITUDE')
    api_key = current_app.config.get('API_KEY')
    units = current_app.config.get('UNITS')

    datetime.datetime


    forecast = forecastio.load_forecast(api_key, lat, lon, units=units)
    current_forecast = forecast.currently()
    daily_forecast = forecast.daily()
    weather = {}
    # Today's details
    weather['currTemp'] = int(round(current_forecast.temperature))
    weather['currIcon'] = current_forecast.icon

    pacific = pytz.timezone('US/Pacific-New')
    sunrise = pytz.utc.localize(daily_forecast.data[0].sunriseTime)
    sunset = pytz.utc.localize(daily_forecast.data[0].sunsetTime)
    weather['sunrise'] = sunrise.astimezone(pacific).strftime('%H:%M')
    weather['sunset'] = sunset.astimezone(pacific).strftime('%H:%M')
    weather['rainProb'] = current_forecast.precipProbability * 100
    weather['summary'] = daily_forecast.data[0].summary
    weather['minTemp'] = int(round(daily_forecast.data[0].temperatureMin))
    weather['maxTemp'] = int(round(daily_forecast.data[0].temperatureMax))
    weather['forecasts'] = get_forecasts(forecast)

    return weather


def get_forecasts(forecast):

    forecast_days = current_app.config.get('FORECAST_DAYS')
    daily_forecast = forecast.daily()
    forecasts = []
    for i in range(1, forecast_days + 1):
        daily = daily_forecast.data[i]
        forecast = (daily.icon, int(round(daily.temperatureMin)), int(round(daily.temperatureMax)), daily.time.strftime('%a'))
        forecasts.append(forecast)

    return forecasts
