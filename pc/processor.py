from flask import Flask, request

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    print("Otrzymano z laptopa dane:", data)
    number = data.get('number')
    result = number ** 2
    print(f"Received {number}, squared: {result}")
    return {"result": result}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
