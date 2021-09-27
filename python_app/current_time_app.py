from flask import Flask, render_template, send_from_directory
from datetime import datetime
import pytz

MOSCOW_TIMEZONE = pytz.timezone('Europe/Moscow')

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        moscow_now = datetime.now(MOSCOW_TIMEZONE)
        with open("static/visits.txt", "a+") as fo:
            fo.write("Accessed at " + str(moscow_now.strftime('%H:%M:%S')) + " " + str(moscow_now.strftime('%d-%m-%Y')) + "\n")
        return render_template('index.html',
                                time = moscow_now.strftime('%H:%M:%S'),
                                date = moscow_now.strftime('%d-%m-%Y'))
        

    @app.route('/visits')
    def download_file():
        return send_from_directory("static", "visits.txt")
    return app



                            