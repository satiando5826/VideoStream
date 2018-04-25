import socket
import sys
import subprocess

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 9999)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()

    try:
        arg = "ffmpeg.exe -re -i test.MP4 -r 30 -s 1280x720 -c:v libx264 -preset medium -crf 23 -f rtsp -rtsp_transport tcp rtsp://localhost:554/live"
        stream = subprocess.Popen(arg, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE) 

        for line in stream.stdout:
            print ("server:", line.rstrip())

    finally:
        connection.close()
        stream.kill()
