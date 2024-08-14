from flask import Flask, render_template, Response
import time


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/events')
def events():
    def generate():
        while True:
            yield f"data: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            time.sleep(1)
    return Response(generate(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)