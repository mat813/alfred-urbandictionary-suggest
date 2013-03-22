#author: Mathieu Arnold

from alfred_utils.feedback import Feedback
import urllib
import json
import sys

query = sys.argv[1]
url = 'http://api.urbandictionary.com/v0/autocomplete?term=%s' % query
response = json.load(urllib.urlopen(url))

fb = Feedback()
for title in response:
    url = 'www.urbandictionary.com/define.php?term=%s' % title
    url.replace(' ', '_')
    fb.add_item(title,
        subtitle="Read Urban Dictionary article on %s" % title,
        arg=title.replace(" ", "_"))
print fb
