import ssl, socket
hosts = [
    'ac-oxvckp8-shard-00-00.ellyvmc.mongodb.net',
    'ac-oxvckp8-shard-00-01.ellyvmc.mongodb.net',
    'ac-oxvckp8-shard-00-02.ellyvmc.mongodb.net'
]
ctx = ssl.create_default_context()
for host in hosts:
    print('HOST', host)
    try:
        with socket.create_connection((host, 27017), timeout=5) as s:
            with ctx.wrap_socket(s, server_hostname=host) as ss:
                print(' tls', ss.version(), ss.cipher())
    except Exception as e:
        print('ERROR', type(e).__name__, e)
