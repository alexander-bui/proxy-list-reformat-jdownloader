TYPE = "http" # http, https, socks4, socks5

with open('proxy.txt', 'r') as f, open('output.txt', 'w') as out:
    for line in f:
        out.write(TYPE+"://"+line)