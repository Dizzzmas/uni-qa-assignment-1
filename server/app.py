from flask import Flask, request, send_file
import os
import hashlib


app = Flask(__name__)


def get_file_checksum(file_name: str):
    md5_hash = hashlib.md5()
    a_file = open(os.path.join(os.getcwd(), 'serverdata', file_name), "rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()

    return digest


@app.route("/")
def get_file():
    file_name = request.args.get('file_name', default = 'blah.txt', type = str)
    return send_file(os.path.join(os.getcwd(), 'serverdata', file_name))

@app.route("/checksum")
def get_cheksum():
    file_name = request.args.get('file_name', default = 'blah.txt', type = str)
    checksum = get_file_checksum(file_name)
    return dict(checksum=checksum)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=os.getenv('PORT', '5000'))
