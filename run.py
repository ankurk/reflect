from flask import Flask, render_template, jsonify
from components import weather, directions
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




