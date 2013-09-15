import fbconsole
import urllib
from requests import get
 
fbconsole.AUTH_SCOPE = ['publish_actions', 'read_stream','user_actions.news', 'publish_stream']
fbconsole.authenticate()

s = fbconsole.fql("SELECT post_id FROM stream WHERE source_id=me() LIMIT 100")
print fbconsole.ACCESS_TOKEN

for i in s:
    print str(i['post_id'])
    f = urllib.urlopen("https://graph.facebook.com/" + str(i['post_id']) + "/comments/?access_token="+fbconsole.ACCESS_TOKEN+"&message=Thank%20you&method=POST")
    print f.read()
