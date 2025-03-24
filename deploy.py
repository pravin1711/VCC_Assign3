import os

# Startup script for new VM
STARTUP_SCRIPT = """#!/bin/bash

apt update -y
apt install -y python3 python3-pip stress
pip3 install flask psutil
echo 'from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route("/")

def home():
  cpu_usage = psutil.cpu_percent(interval=1)
  return jsonify({"message": "Hey! Deploying on google cloud after resourcs usage is greater than 75%!"})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)' > app.py

nohup python3 app.py > flask.log 2>&1 &
"""

# Save startup script
with open("startup.sh", "w") as f:
    f.write(STARTUP_SCRIPT)
# GCP Autoscaling Command
command = f"""gcloud beta compute instance-groups managed create instance-group-2 --project=assign2-452517 --base-instance-name=instance-group-2 --template=projects/assign2-452517/regions/us-west1/instanceTemplates/assign3 --size=1 --zone=us-west1-b --list-managed-instances-results=pageless && gcloud beta compute instance-groups managed set-autoscaling instance-group-2 --project=assign2-452517 --zone=us-west1-b --mode=on --min-num-replicas=1 --max-num-replicas=3 --target-cpu-utilization=0.75 --cpu-utilization-predictive-method=none --cool-down-period=60
"""
