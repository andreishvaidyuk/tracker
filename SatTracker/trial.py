from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, send, emit, disconnect, join_room
import time
import json
from SatTracker.sattracker import *



app = Flask(__name__)
app.config['SECRET_KEY'] = 'andrey'
socketio = SocketIO(app)

# create object of class "SatTracker"
tracker = SatTracker()


@app.route('/')
def sessions():
    return render_template("mymap.html")


@socketio.on('message')
def message_received(message, methods=['Get', 'Post']):
    print(message['data'])


@socketio.on('start')
def start_observation_event(satellite, methods=['Get', 'Post']):
    """
    Метод принимает наименование спутника и активирует расчет его координат и отображение траектории на карте.
    Сначала определяются координаты наземной станции, затем по наименованию спутника идет поиск его TLE.
    При наличии TLE вызывается функция "observation", которая запускает цикл расчета координат данного спутника.
    Если TLE не найдет, то выводится сообщение - "Satellite name not found". Если никакое имя спутника не пердавалось,
    выводится сообщение - "Enter satellite name".
    :param satellite: name of the satellite
    :param methods:
    :return:
    """
    sat_name = str(satellite['satellite_name']).upper()
    print('Satellite name: ' + sat_name)
    if sat_name != '':
        tracker.isActive = True
        print("Setting ground segment Location.")
        gs_location = tracker.set_location()
        print_gs_location(gs_location)
        print("\nGetting TLE.")
        tle = tracker.get_tle(sat_name, 'text_files/tle.txt')
        if tle:
            print("\nLoading TLE data.")
            tracker.load_tle("text_files/tle.txt")
            observation(tracker)
        else:
            print("Satellite name not found")
            msg = json.dumps("Satellite name not found")
            socketio.emit('response', msg)
    else:
        msg = json.dumps("Enter satellite name")
        socketio.emit('response', msg)


@socketio.on('stop')
def stop_observation_event(satellite, methods=['Get', 'Post']):
    """
    Метод останавливает расчет координат спутника и отображение траектории на карте.
    :param satellite: Name of the satellite
    :param methods:
    :return:
    """
    sat_name = str(satellite['satellite_name'])
    print('Satellite name: ' + sat_name)
    tracker.isActive = False
    observation(tracker)


def observation(tracker):
    """
    Метод запускает цикл расчета координат спутника и отображение его траектории на карте
    :param tracker: Object of class "SatTracker"
    :return:
    """
    if not tracker.isActive:
        print("Observation stopped")
    else:
        for i in range(5):
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
