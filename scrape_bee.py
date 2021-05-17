#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json
import os,sys
os.chdir(sys.path[0])

def scrape_bee(url):

	r = requests.get(url, headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	soup = BeautifulSoup(r.text,'html.parser')


	element = soup.find('div', class_='pz-game-screen')

	element = element.find('script')

	data = element.contents[0].replace('window.gameData = ','')

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
			# get list of urls to scrape old puzzles from wayback machi	ne
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
		scrape_bee(u.strip())

