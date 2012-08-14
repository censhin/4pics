#!/usr/bin/env python2

import urllib2
import sys
import re
import threading

def get_images(url):
	r = re.compile('//images.4chan.org/[^"]*(?:.jpg|.jpeg|.bmp|.gif|.png)')
	return r.findall(urllib2.urlopen(url).read())

def download(url, folder = ''):
	web_file = urllib2.urlopen(url)
	if folder != '' and folder[-1] != '/':
		folder += '/'
	local_file = open(folder + url.split('/')[-1], 'w')
	local_file.write(web_file.read())
	web_file.close()
	local_file.close()

class Download(threading.Thread):
	def __init__(self, url, folder = ''):
		threading.Thread.__init__(self)
		self.url = url
		self.folder = folder
	def run(self):
		download(self.url, self.folder)

if __name__ == '__main__':
	if len(sys.argv) == 2 or len(sys.argv) == 3:
			list = get_images(sys.argv[1])
			done = []
			threads = []

			for i in list:
				if i not in done:
					done.append(i)
					i = 'https:%s' % i 
					print i
					if len(sys.argv) == 3:
						thread = Download(i, sys.argv[2])
						thread.start()
						threads.append(thread)
					else:
						thread = Download(i)
						thread.start()
						threads.append(thread)

			for thread in threads:
				thread.join()

	else:
		import os
		print 'This is a script to download images from 4chan.'
		print 'usage: %s http://server.com/ [directory]' % os.path.basename(sys.argv[0])
		print 'usage: %s http://server.com/' % os.path.basename(sys.argv[0])
