from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send,emit
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    send(data, broadcast=True)  # Gửi tin nhắn đến mọi người

@socketio.on('join')
def on_join(data):
    room = data.get('room')
    username = data.get('username', 'Anonymous')
    join_room(room)
    # Notify everyone in the room about the new user
    emit('message', {
        'username': 'System',
        'message': f"{username} đã vào phòng {room}.",
        'timestamp': datetime.now().strftime('%H:%M:%S')
    }, room=room)

@socketio.on('leave')
def on_leave(data):
    room = data.get('room')
    username = data.get('username', 'Anonymous')
    leave_room(room)
    # Notify everyone in the room about the user leaving
    emit('message', {
        'username': 'System',
        'message': f"{username} đã rời phòng {room}.",
        'timestamp': datetime.now().strftime('%H:%M:%S')
    }, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
    socketio.run(app, host='192.168.71.127', port=5000)

