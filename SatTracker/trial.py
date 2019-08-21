from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, send, emit, disconnect, join_room
import time
import json
from SatTracker.sattracker import *



app = Flask(__name__)
app.config['SECRET_KEY'] = 'andrey'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template("mymap.html")


@socketio.on('message')
def message_received(message, methods=['Get', 'Post']):
    print('message was received: ' + message['data'])


@socketio.on('my event')
def handle_my_custom_event(data, methods=['Get', 'Post']):
    sat_name = str(data['satellite_name'])
    print('Satellite name: ' + sat_name)
    tracker = SatTracker()
    tracker.activate()
    for i in range(5):
        sat_info = tracker.find_sat_coordinates_for_now()
        d = get_dict_of_sat_info(sat_info)
        data2 = json.dumps(d)
        print_sat_coordinates(sat_info)
        tracker.write_statistic()
        tracker.write_sat_coordinates()
        tracker.find_realtime_coord()
        time.sleep(5.0)
        tracker.observer.date = datetime.utcnow()

        emit('my response', data2)


if __name__ == '__main__':
    socketio.run(app, debug=True)


#
# from SatTracker.sattracker import *
#
#
# def main():
#     tracker = SatTracker()
#     tracker.activate()
#
#
# if __name__ == '__main__':
#     main()
