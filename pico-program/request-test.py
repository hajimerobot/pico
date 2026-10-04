request = "GET /ledon? HTTP/1.1"
request_line = request.split()[1]
print(request_line)

if request_line.startswith("/ledon"):
    print("LED ON")
elif request_line.startswith("/ledoff"):
    print("LED OFF")
