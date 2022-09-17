import socket

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

print("Computer name is:", hostname)
print("Computer IP Address is:", IP)