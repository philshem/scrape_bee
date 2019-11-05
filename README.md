# scrape_bee

NYTimes Spelling Bee scraper 🐝☠️

Spoiler: shows the solution!

### to run the code

    git clone https://github.com/philshem/scrape_bee.git
    cd scrape_bee
    pip3 install -r requirements
    python3 scrape_bee.py

Doing this will save today's puzzle as a json to the folder 'data/'.

Requires BeautifulSoup and requests.

---

### using the wayback machine (archive.org) to download old puzzles

Alternative usage is to provide a URL, for example, with the wayback machine:

    echo https://web.archive.org/web/20190727114759/https://www.nytimes.com/puzzles/spelling-bee | python3 scrape_bee.py /dev/stdin

You can also use the python library [waybackpack](https://github.com/jsvine/waybackpack) to download all URLs from the wayback machine, and then pass those urls to the scrape_bee.py script:

    pip3 install waybackpack
    waybackpack https://www.nytimes.com/puzzles/spelling-bee --list > urls.txt

    python3 scrape_bee.py urls.txt

(Note that many of the archived URLs have no valid puzzle, or are not available due to the subscription call-to-action.)
