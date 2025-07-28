import requests
import time


def main():
    start_num = 10
    while True:
        start_num += 1
        print(f"Sending {start_num}...")
        try:
            requests.post("http://192.168.100.209/process", json={"number": start_num})
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(2)

if __name__ == "__main__":
    main()