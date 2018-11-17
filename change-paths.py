#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import bencoder
from pprint import pprint

f = open("resume.dat", "rb")
d = bencoder.decode(f.read())
# del d[b"info"][b"pieces"] # That's a long hash
# pprint(d)

# print(type(d))
# print(type(d.items()))

# Ключи первого уровня - относительные пути к торрент файлам.


# for key, value in d.items() :
#     print (key)

def changePaths(input, mapping = False):

	# items = input.items()
	
	# for key, value in items:
	for i in range(2):
		key, value = input.popitem()
		print(key.decode("utf-8"))
		print(value.keys())
		# del value[b"info"][b"pieces"] # That's a long hash
		keysToDecode = (b'caption', b'path')

		for fkey, fvalue in value.items() :
			print(fkey)
			# if "decode" in dir(value):
			if fkey in keysToDecode:
				print (fvalue.decode("utf-8"))
			else:
				print (fvalue)

			if fkey == b'targets':
				print('it is targets')
				# for tkey, tvalue in fvalue.items():
				print(fvalue[0][1].decode("utf-8"))
		# print(value[b'caption'].decode("utf-8"))
		# print(value[b'moved'])
		# b'added_on', b'blocks', b'blocksize', b'cached', b'caption', b'codec', b'completed_on', b'corrupt', b'dht', b'download_url', b'downloaded', b'downspeed', b'episode', b'episode_to', b'feed_url', b'hashfails', b'have', b'info', b'last seen complete', b'last_active', b'lsd', b'moved', b'order', b'override_seedsettings', b'path', b'peers6', b'prio', b'prio2', b'quality', b'rss_name', b'runtime', b'scrambled', b'season', b'seedtime', b'started', b'superseed', b'superseed_cur_piece', b'targets', b'time', b'trackermode', b'trackers', b'ulslots', b'uploaded', b'upspeed', b'use_utp', b'valid', b'visible', b'wanted_ratio', b'wanted_seedtime', b'waste', b'webseeds'

changePaths(d)
