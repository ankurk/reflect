import googlemaps
from datetime import datetime
from flask import current_app


def get_client():
    api_key = current_app.config.get('GOOGLE_MAPS_API_KEY')
    gmaps = googlemaps.Client(api_key)
    return gmaps


def get_travel_time(origin, dest):

    gmaps = get_client()
    now = datetime.now()
    directions_result = gmaps.directions(origin, dest, mode="driving", departure_time=now, traffic_model="best_guess")

    return unpack_result(directions_result)

def get_commute_time():
    origin = current_app.config.get('FROM')
    dest = current_app.config.get('TO')
    normal_time, traffic_time, route = get_travel_time(origin, dest)
    commute_time = {}
    commute_time['normal_time'] = normal_time
    commute_time['traffic_time'] = traffic_time
    commute_time['route'] = route
    return commute_time


def unpack_result(directions):
    best_route = directions[0]['legs'][0]
    normal_time = directions[0]['legs'][0]['duration']['text']
    traffic_time = directions[0]['legs'][0]['duration_in_traffic']['text']
    summary = directions[0]['summary']
    print directions[0]['legs'][0].keys()
    return normal_time, traffic_time, summary
