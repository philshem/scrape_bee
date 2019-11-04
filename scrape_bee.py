#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json
import os

def main():
	
	# the answers are stored as a json inside the page source
	url = 'https://www.nytimes.com/puzzles/spelling-bee'
	
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
	main()

