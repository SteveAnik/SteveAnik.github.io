from flask import Flask, request, jsonify
import os


app = Flask(__name__, static_folder='static')

# Serve the static index.html   
@app.route('/', methods=['GET'])
def serve_index():
    return app.send_static_file('index.html')

# Handle POST requests from the front-end
@app.route('/', methods=['POST'])
def handle_post():
    data = request.get_json()
    user_message = data.get('userMessage', 'No message provided')
    
    return jsonify({"response"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)