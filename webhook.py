from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print("Dados recebidos do GitHub:", data)
        return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(port=5000)