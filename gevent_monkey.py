import gevent
from gevent import monkey; monkey.patch_all()
import socket

hosts = ['www.python.org', 'www.yahoo.com',
         'www.github.com']#https 換成 www

jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)

for job in jobs:
    print(job.value)
