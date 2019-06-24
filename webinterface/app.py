from flask import Flask, render_template, redirect, url_for, request
from SatTracker.sattracker import *

app = Flask(__name__)
app.debug = True


@app.route('/')
def home():
    return render_template('welcome.html')


@app.route('/mymap', methods=['POST', 'GET'])
def map():
    if request.method == "POST":
        thread1 = MyThread(1, "tracker-1")
        if "start" in request.form:
            thread1.start()
            print("\nTracking started")
            return render_template('mymap.html')
        elif "stop" in request.form:
            return render_template('mymap.html')
    elif request.method == "GET":
        return render_template('mymap.html')


def activate():
    thread1 = MyThread(1, "tracker-1")
    thread1.start()
    print("\nTracking started")


if __name__ == '__main__':
    app.run(debug=True)
