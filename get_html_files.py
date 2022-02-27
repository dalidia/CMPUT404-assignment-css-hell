import socket

HOST = "www.google.com"
PORT = 80
PAYLOAD = f'GET / HTTP/1.1\r\nHost: {HOST}\r\n\r\n'
BUFFER_SIZE = 4096


def main():
    # creates a new socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket was created")
    except OSError as e:
        print("There was an error creating the socket", e)
        return