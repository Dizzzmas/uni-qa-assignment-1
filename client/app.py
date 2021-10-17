import os
import hashlib
import requests


def get_file_checksum(file_name: str):
    md5_hash = hashlib.md5()
    a_file = open(os.path.join(os.getcwd(), 'clientdata', file_name), "rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()

    return digest

def get_file_from_server():
    server_host = os.getenv('SERVER_HOST', 'http://server')
    server_port = os.getenv('SERVER_PORT', '5000')
    get_file_url = f"{server_host}:{server_port}/"
    get_checksum_url = f"{server_host}:{server_port}/checksum"
    saved_file_name = 'file.txt'

    response = requests.get(get_file_url)
    # Save file from response
    with open(os.path.join(os.getcwd(), 'clientdata', saved_file_name), 'wb') as f:
        f.write(response.content)
    
    server_checksum = requests.get(get_checksum_url).json().get('checksum')
    client_checksum = get_file_checksum(saved_file_name)

    if server_checksum != client_checksum:
        raise Exception('Checksum mismatch')
    else:
        print('Checksum match')


if __name__ == "__main__":
    get_file_from_server()
