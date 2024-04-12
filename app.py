import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_use = psutil.cpu_percent()
    mem_use = psutil.virtual_memory().percent  
    message = None
    if cpu_use > 80 or mem_use > 80 :
        message = "High CPU, Memory, or Storage usage detected. Consider scaling up."
    return render_template("index.html", cpu_use=cpu_use, mem_use=mem_use, message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
