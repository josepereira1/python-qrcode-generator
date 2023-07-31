from flask import Flask, request, send_file
import qrcode, datetime

# put your qrcode text here
QRCODE_TEXT = 'qrcode text'

app = Flask(__name__)

# important: use this endpoint to URL cases (note: set the QR code text in QRCODE_TEXT var)
@app.route("/qrcode", methods=["GET"])
def get1():
    filename = 'qrcode-generator_' + datetime.datetime.now().strftime('%m%d%Y%H%M') + '.png'
    qrcodegen(filename, QRCODE_TEXT)
    return send_file(filename, as_attachment=True)

# important: do not use this endpoint to URL!
@app.route("/qrcode/<text>", methods=["GET"])
def get2(text):
    filename = 'qrcode-generator_' + datetime.datetime.now().strftime('%m%d%Y%H%M') + '.png'
    qrcodegen(filename, text)
    return send_file(filename, as_attachment=True)

def qrcodegen(filename, text):
    img = qrcode.make(text)
    img.save(filename)

@app.route("/", methods=['GET'])
def running():
    return "QR code generation service. Try http://localhost/qrcode to get your QR code file."

if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
