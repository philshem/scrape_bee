#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json
import os
import sys

def scrape_bee(url):

	r = requests.get(url)
	soup = BeautifulSoup(r.text,'html5lib')

	element = soup.find('div', class_='pz-game-screen')
	element = element.find('script')

	data = element.text.replace('window.gameData = ','')

	data = json.loads(data)
	print(json.dumps(data, indent = 4))

	dt = data.get('today').get('printDate')

	with open('data' + os.sep + dt + '.json','w') as fp:
		json.dump(data,fp)

	print(dt)
	
if __name__ == '__main__':
	
	# the answers are stored as a json inside the page source
	if len(sys.argv) == 1:
		# get today's puzzle
		urls = ['https://www.nytimes.com/puzzles/spelling-bee']
	elif len(sys.argv) == 2:
		try:
			# get list of urls to scrape old puzzles from wayback machine
			with open(sys.argv[1]) as f:
				urls = f.readlines()
		except:
			print('ERROR: Not a valid file:',f)
			exit(0)
	else:
		print('ERROR: Incorrect usage.')
		print('\tScript requires either no argument, for today\'s puzzle,')
		print('or a path to a file containing URLs. Exiting...')
		exit(0)

	for u in urls:
		try:
			scrape_bee(u.strip())
			print('INFO: Valid html in',u.strip())
		except:
			print('WARNING: Non-matching html in',u.strip())

