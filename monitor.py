import psutil
import subprocess
import time
import threading
import sys

THRESHOLD = 75  # CPU usage threshold
CHECK_INTERVAL = 5  # Check CPU every 5 seconds

def check_cpu():
    """Monitors CPU and triggers VM deployment if threshold is exceeded."""
    time.sleep(2)  # Initial delay
    while True:
        cpu_usage = psutil.cpu_percent(interval=CHECK_INTERVAL)
        print(f"[INFO] CPU Usage: {cpu_usage}%", flush=True)  # Force immediate output

        if cpu_usage > THRESHOLD:
            print("⚠️ [ALERT] High CPU detected! Deploying GCP VM for Pravin...", flush=True)
            try:
                subprocess.run(["python3", "deploy.py"], check=True)
                print("[SUCCESS] GCP VM deployed successfully for Pravin!", flush=True)
                break  # Stop checking after deployment
            except subprocess.CalledProcessError as e:
                print(f"[ERROR] Deployment failed: {e}", flush=True)

        time.sleep(10)  # Wait before rechecking

if __name__ == "__main__":
    print("[INFO] Starting CPU Monitoring for Pravin's system...", flush=True)
    
    monitor_thread = threading.Thread(target=check_cpu, daemon=True)
    monitor_thread.start()
    
    # Keep the main script running
    while True:
        time.sleep(1)
