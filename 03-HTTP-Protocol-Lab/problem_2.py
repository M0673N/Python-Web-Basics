from urllib import parse

url = input()


def print_data(protocol, host, port, path, query, fragment):
    result = f'''Protocol: {protocol}
Host: {host}
Port: {port}
Path: {path}
'''
    if query:
        result += f'Query: {query}'
    if fragment:
        result += f'Fragment: {fragment}'

    print(result)


def validate_data(protocol, host, port, path, query, fragment):
    if not protocol or not host or not port or not path or '.' not in host:
        return False
    return True


def process_url(data):
    protocol = data.scheme
    if ':' in data.netloc:
        host = data.netloc.split(':')[0]
        port = data.netloc.split(':')[1]
    else:
        host = data.netloc
        port = 80 if data.scheme == 'http' else 443
    path = data.path
    if not path:
        path = '/'
    query = data.query
    fragment = data.fragment

    result = validate_data(protocol, host, port, path, query, fragment)
    if not result:
        print('Invalid URL')
    else:
        print_data(protocol, host, port, path, query, fragment)


process_url(parse.urlparse(url))
