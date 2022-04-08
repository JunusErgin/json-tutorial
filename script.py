import requests # pip install requests
import re


url = 'https://www.instagram.com/junus.ergin/'
print('Start crawling...')
resp = requests.get(url)



def find_between(s, first, last ):
    """
    Findet einen beliebigen Text zwischen 2 Markern
    """
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return 'No result found'

if resp.ok:
    start_marker = '<meta content="'
    end_marker = 'Abonnenten, '
    result = find_between(resp.text, start_marker, end_marker)
    print(result)

    # Text Datei erstellen und Output speichern
    with open("Output.txt", "w") as text_file:
        print(resp.text, file=text_file)

else:
    print ("Error {}".format(resp.status_code))
    print (resp.text)