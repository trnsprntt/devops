from flask import Flask, render_template
from datetime import datetime
import pytz

MOSCOW_TIMEZONE = pytz.timezone('Europe/Moscow')

app = Flask(__name__)

@app.route('/')
def index():
    moscow_now = datetime.now(MOSCOW_TIMEZONE)
    return render_template('index.html',
                            time = moscow_now.strftime('%H:%M:%S'),
                            date = moscow_now.strftime('%d-%m-%Y'))
                            