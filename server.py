
from flask import Flask
from flask_socketio import SocketIO, send

# ساخت اپلیکیشن Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # کلید امنیتی
socketio = SocketIO(app, cors_allowed_origins="*")  # فعال کردن CORS برای همه

# مسیر اصلی (اختیاری)
@app.route('/')
def home():
    return "Chat server is running!"

# مدیریت پیام‌های چت
@socketio.on('message')
def handle_message(message):
    print(f"Message received: {message}")
    send(message, broadcast=True)  # ارسال پیام به همه کاربران متصل

# اجرای سرور
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)  # اجرا روی همه اینترفیس‌ها
