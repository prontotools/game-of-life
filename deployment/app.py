from flask import Flask, request, abort


app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        group = request.json.get('group')

        if group == 'gof-01':
            print('hi')
        elif group == 'gof-02':
            print('hey')
        elif group == 'gof-03':
            print('hhh')

        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
