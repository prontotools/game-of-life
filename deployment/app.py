import os

from flask import Flask, request, abort


app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        group = request.json.get('group')

        if group == 'gof-01':
            os.system('cd game-of-life-01 && git pull origin master')
        elif group == 'gof-02':
            os.system('cd game-of-life-02 && git pull origin master')
        elif group == 'gof-03':
            os.system('cd game-of-life-03 && git pull origin master')

        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
