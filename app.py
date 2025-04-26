from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import matplotlib.colors as mcolors

app = Flask(__name__, static_folder='static')
CORS(app)  
def generate_shades(base_color):
    try:
        rgb = mcolors.to_rgb(base_color)
    except ValueError:
        return []
    shades = []
    for factor in [0.8, 0.6, 0.4, 0.2, 1.2, 1.4, 1.6, 1.8]:
        new = tuple(min(1, max(0, c * factor)) for c in rgb)
        shades.append(mcolors.to_hex(new))
    return shades

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/get_shades', methods=['POST'])
def get_shades():
    color = request.get_json().get('color', '')
    shades = generate_shades(color)
    if not shades:
        return jsonify({'error': 'Invalid color'}), 400
    return jsonify({'shades': shades})

if __name__ == '__main__':
    app.run(debug=True)
