import socket

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

print("Computer name is:", hostname)
print("IP address:", IP)