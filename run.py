from flask import Flask, render_template, jsonify
from components import weather, directions, news, market
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config.from_object('config')
socketio = SocketIO(app)

@app.route('/')
def show_mirror():
    weather_data = weather.get_weather()
    return render_template('main.html', weather=weather_data)

@app.route('/_get_weather')
def get_weather():
    weather_data = weather.get_weather()
    return jsonify(weather_data)

@app.route('/_get_contextual')
def get_contextual():
    commute_time = directions.get_commute_time()
    commute_time['type'] = 'direction'
    return jsonify(commute_time)

@app.route('/_get_news_headlines')
def get_headlines():
    response = {}
    headlines = news.get_headlines()
    response['type'] = 'news'
    response['content'] = headlines
    return jsonify(response)

@app.route('/_get_market_prices')
def get_stock_prices():
    response = {}
    prices = market.get_market_prices()
    response['type'] = 'market'
    response['content'] = prices
    return jsonify(response)


# @socketio.on('update weather')
# def update_weather():
#     emit('weather update', {'data': 'some weather'})
#
# @socketio.on('connect')
# def test_connect():
#     print('Client connect request')
#     emit('my response', {'data': 'Connected'})
#
# @socketio.on('disconnect')
# def disconnect():
#     print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, debug=True)




