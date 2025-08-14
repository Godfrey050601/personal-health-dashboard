from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to Personal Health Dashboard</h1><p>Flask app for tracking personal health metrics with charts (SQLite + Chart.js)</p>"

if __name__ == '__main__':
    app.run(debug=True)
