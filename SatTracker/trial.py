from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, send, emit, disconnect, join_room
import time
import json
from SatTracker.sattracker import *



app = Flask(__name__)
app.config['SECRET_KEY'] = 'andrey'
socketio = SocketIO(app)

tracker = SatTracker()
@app.route('/')
def sessions():
    return render_template("mymap.html")


@socketio.on('message')
def message_received(message, methods=['Get', 'Post']):
    print(message['data'])


@socketio.on('start')
def start_observation_event(satellite, methods=['Get', 'Post']):
    sat_name = str(satellite['satellite_name'])
    print('Satellite name: ' + sat_name)

    tracker.activate(sat_name)
    observation(tracker)


@socketio.on('stop')
def stop_observation_event(satellite, methods=['Get', 'Post']):
    sat_name = str(satellite['satellite_name'])
    print('Satellite name: ' + sat_name)
    tracker.isActive = False
    observation(tracker)


def observation(tracker):
    if tracker.isActive == False:
        print("Observation stopped\n\n\n")
    else:
        for i in range(50):
            if tracker.isActive:
                sat_info = tracker.find_sat_coordinates_for_now()
                d = get_dict_of_sat_info(sat_info)
                data = json.dumps(d)
                print_sat_coordinates(sat_info)
                tracker.write_statistic()
                tracker.write_sat_coordinates()
                tracker.find_realtime_coord()
                time.sleep(1.0)
                tracker.observer.date = datetime.utcnow()
                emit('my response', data)


if __name__ == '__main__':
    socketio.run(app, debug=True)
