#!/usr/bin/env python

import urllib2
import sys
import re

def get_images(url):
	r = re.compile('http://images.4chan.org/[^"]*(?:.jpg|.jpeg|.bmp|.gif|.png)')
	return r.findall(urllib2.urlopen(url).read())

def download(url):
	web_file = urllib2.urlopen(url)
	local_file = open(url.split('/')[-1], 'w')
	local_file.write(web_file.read())
	web_file.close()
	local_file.close()

if __name__ == '__main__':
	if len(sys.argv) == 2:
			list = get_images(sys.argv[1])
			done = []
			for i in list:
				if i not in done:
					done.append(i)
					print i
					download(i)
	else:
		import os
		print 'This is a script to download images from 4chan.'
		print 'usage: %s http://server.com/lulz/faggot/' % os.path.basename(sys.argv[0])
