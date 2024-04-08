from flask import Flask, request, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

app = Flask(__name__)

def decode_hex(hex_string):
    decoded = ''
    hex_list = hex_string.split(',')
    for hex_code in hex_list:
        try:
            decoded += bytes.fromhex(hex_code).decode('utf-8')
        except ValueError:
            decoded += f'Invalid Hex: {hex_code}'
    return decoded

def decode_binary(binary_string):
    decoded = ''
    binary_list = binary_string.split(',')
    for binary_code in binary_list:
        try:
            decoded += chr(int(binary_code, 2))
        except ValueError:
            decoded += f'Invalid Binary: {binary_code}'
    return decoded

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decode', methods=['POST'])
def decode():
    hex_code = request.form.get('hex_code', '')
    binary_code = request.form.get('binary_code', '')
    decoded_hex = decode_hex(hex_code)
    decoded_binary = decode_binary(binary_code)
    return render_template('decode.html', decoded_hex=decoded_hex, decoded_binary=decoded_binary)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=False)