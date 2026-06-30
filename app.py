from flask import Flask, render_template
import socket
import platform
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route("/")
def home():

    return render_template(

        "index.html",

        # Deployment Information
        status="Running",
        environment="Production",
        version="v1.0.0",
        deployment="Docker Hub Pull",
        docker_image="suchit10/github-actions-dockerhub-cd:v1",
        repository="suchit10/github-actions-dockerhub-cd",

        # System Information
        hostname=socket.gethostname(),
        os_name=platform.system(),
        python_version=platform.python_version(),

        # AWS Region
        region="ap-south-1 (Mumbai)",

        # Time (Indian Standard Time)
        current_time=datetime.now(
            ZoneInfo("Asia/Kolkata")
        ).strftime("%d %B %Y | %I:%M:%S %p IST")

    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )