#!/usr/bin/env python3

import datetime
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Data Scraper 1.0','From': 'youremail@domain.com'}

def scrape_old_bee(url,s):
	print(url)
	r = s.get(url, headers=headers)
	soup = BeautifulSoup(r.text,'html5lib')

	answers = soup.find('div', id='main-answer-list')
	
	pangrams = answers.findAll('mark')
	pangrams = [p.text for p in pangrams]
	#print(pangrams)

	answers = answers.findAll('li')
	answers = [a.text.split()[0] for a in answers]
	#print(answers)

	letters = list(set(''.join(answers)))
	#print(letters)
	for l in letters:
		if all(l in x for x in answers):
			center = l

	notes = soup.find('div', id='puzzle-notes')
	notes = notes.findAll('h3')
	notes = [{n.text.split(':')[0].strip() : int(n.text.split(':')[1])} for n in notes]
	#print(notes)

	d = construct_dict(letters, center, answers, pangrams, notes)

	print (d)
def construct_dict(l, c, a, p, n):

	d = {
		'letters' : l,
		'center' : c
	}

	return d

if __name__ == '__main__':
	# construct urls for scrape
	# first date is 20180729
	start = datetime.datetime(2018,7,29)
	stop = datetime.datetime.today()
	date_list = [start + datetime.timedelta(days=x) for x in range((stop-start).days + 1)]
	url_list = ['https://nytbee.com/Bee_'+dt.strftime('%Y%m%d')+'.html' for dt in date_list]
	#print(url_list)
	#exit(0)

	url_list = ['https://nytbee.com/Bee_20191007.html']

	# scrape urls
	s = requests.session()
	for url in url_list:
		scrape_old_bee(url,s)
