import socket
import machine
from time import sleep

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECTED"
SERVER = "192.168.137.125"#ændre til at være socket serveren der skal sendes til
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

rw = machine.Pin(32, machine.Pin.IN)

previousVal = None

def send(msg):
    message = msg.encode(FORMAT)
    msgLength = len(message)
    sendLength = str(msgLength).encode(FORMAT)
    sendLength += b' ' * (HEADER - len(sendLength))
    client.send(sendLength)
    client.send(message)
    

while True:
    val1= rw.value()
    sendVal = str(val1)
    
    if sendVal != previousVal:
        send(sendVal)
    
    
    previousVal = sendVal