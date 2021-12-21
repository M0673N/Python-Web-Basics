def print_result(data):
    if data:
        print(f'''HTTP/1.1 200 OK
Content-Length: 2
Content-Type: text/plain

OK
''')
    else:
        print(f'''HTTP/1.1 404 Not Found
Content-Length: 9
Content-Type: text/plain

Not Found
''')


methods = {'get': [], 'post': []}

while True:
    command = input()
    if command == 'END':
        break

    path = command[:command.rindex('/')]
    method = command[command.rindex('/') + 1:]

    methods[method].append(path)

request = input().split()
if request[1] in methods[request[0].lower()]:
    print_result(True)
else:
    print_result(False)
