import requests
import time
import os
from dotenv import load_dotenv


load_dotenv()
ip = os.getenv("SERVER_IP")
port = os.getenv("SERVER_PORT")

def main():
    start_num = 10
    while True:
        start_num += 1
        print(f"Sending {start_num}...")
        try:
            url = f"http://{ip}:{port}/process"
            requests.post(url, json={"number": start_num})
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(2)

if __name__ == "__main__":
    main()