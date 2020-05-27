from bs4 import BeautifulSoup
import requests
import re
import sys

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
}

frameworks = [framework for framework in sys.argv[1:]]
# frameworks = ['flask', 'django', 'web2py'], or any space-separated list passed to the command line

search_for = 'result-stats'
results = {}


def main():
    for framework in frameworks:
        google_query = 'https://www.google.com/search?q=python+{}'.format(framework)
        # google_query = 'https://www.google.com/search?q=python+django', for example

        response = requests.get(google_query, headers=HEADERS)
        # response = '<Response object with lots of goodies, including a website's text>'

        html = response.text
        # html = '<html>...</html>'

        print(framework, google_query, len(html))

        soup = BeautifulSoup(html, 'lxml')
        # soup = BeautifulSoup(html, 'html.parser')
        # soup is now easier to parse, thanks to BeautifulSoup

        result = soup.find(id=search_for).text
        # result = 'About 252,000 results (0.43 seconds)'

        results[framework] = get_num_in(result)
        # {'web2py': 252000; 'django': 41900000}

    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    # sorted_results = [('django', 42100000), ('flask', 27500000), ('web2py', 249000), ('cherrypy', 206000)]

    for result in sorted_results:
        print('{:>20} - {:>10,}'.format(result[0], result[1]))


def get_num_in(result):
    # result = 'About 252,000 results (0.43 seconds)'
    pattern = re.compile('About ([0-9,]+) results')
    # set the pattern to search for - A number, with or without commas, in between About and results

    match = pattern.findall(result)
    # match = 252,000

    if match:
        return int(match[0].replace(',', ''))
        # return 252000
    else:
        return 0


if __name__ == '__main__':
    main()
