from flask import Flask, render_template
from requester import get_cantine_weekly_menu
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    week = get_cantine_weekly_menu()
    today = week[datetime.datetime.today().weekday()]
    normal = today[0]
    vegan = today[1]
    return render_template('index.html', normal=normal[12:], vegan=vegan[9:])


if __name__ == '__main__':
    app.run('0.0.0.0')
