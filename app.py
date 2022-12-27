from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)

@app.route('/')
def index():
    GameOfLife(10, 10)
    return render_template("index.html")

@app.route('/live')
def live():
    live = GameOfLife()
    if live.counter and not live.end_of_game:
        live.form_new_generation()
    live.counter += 1
    return render_template("live.html", live=live)

if __name__ == '__main__':
    # app.run()
    app.run(host='127.0.0.1', port=5000, debug=True)

# Терминал
# set FLASK_DEBUG = 1