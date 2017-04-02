#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import sys
import json
import readline

from myapp.modules import Words, Translates
from myapp import db

def main(query):
	#print(query)
	url = 'http://fanyi.youdao.com/openapi.do?keyfrom=translation-daily&key=2127275011&type=data&doctype=json&version=1.1&q=' + query
	fp = urllib2.urlopen(url)
	info = fp.read().decode("utf8")
	word = Words(word=query)
	db.session.add(word)
	db.session.commit()

	jsonData = json.loads(info)
	if 'basic' in jsonData:		
		res = jsonData["basic"]["explains"]	
		#target = "|".join(res)
		for explains in res:
			print('\t' + explains)
			trans = Translates(Translate=explains, word_id=word.id)
			db.session.add(trans)
		# yi bu de qu zhi xing?
		#add(Word(query, target))
		#print(target.encode('utf-8'))
	else:
		print('***Ensure the word is right!')

	db.session.commit()

def shell():
	
	while True:
		w = raw_input("translate>>>")
		if len(w) == 0:
			continue
		elif 'q' == w:	
			#close()		
			break
		else:
			main(w)

	

if __name__ == "__main__":
	if len(sys.argv) == 2 and sys.argv[1] == "shell":
		shell()
		#create_table()
	elif len(sys.argv) == 1:
		print('***Please input a target word.')
	else:
		main(sys.argv[1])