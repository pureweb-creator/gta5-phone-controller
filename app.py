from ahk import AHK
from flask import Flask, render_template
from flask_socketio import Namespace, SocketIO, emit

ahk = AHK()

host = "192.168.0.105"
port = "5000"

app = Flask(__name__, static_folder='static', template_folder='templates')
socketio = SocketIO(app, async_mode=None)

keycommands = {
    "fwd": "w",
    "bwd": "s",
    "rt": "d",
    "lt": "a"
}
class Control(Namespace):

    @app.route('/')
    def route():
        return render_template('index.html', sync_mode=socketio.async_mode)

    def on_connect(self):
        emit('after connect',  {'data':'Connected!'})

    def on_disconnect(self):
        emit('disconnect', {'data': 'Disonnected!'})

    def on_touchstart(self, msg):
        touch = msg.get('data')
        print(f"Touchstart {touch}")
        ahk.key_down(keycommands.get(touch))

    def on_touchend(self, msg):
        touch = msg.get('data')
        print(f"Touchend {touch}")
        ahk.key_up(keycommands.get(touch))

    def on_click(self, msg):
        touch = msg.get('data')
        print(f"Click {touch}")
        ahk.key_press(keycommands.get(touch))

socketio.on_namespace(Control('/'))

if __name__ == "__main__":
    socketio.run(app, host=host, port=port, debug=True)
