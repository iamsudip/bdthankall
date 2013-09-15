
import fbconsole
import json
from requests import get

fbconsole.AUTH_SCOPE = ['publish_actions', 'user_status']
fbconsole.authenticate()

post_id = fbconsole.fql("SELECT post_id  FROM stream WHERE source_id=me()")
jsonf = open('post_id.json', "w")
jsonf.write(json.dumps(post_id))
jsonf.close()
     
fbconsole.logout()
     




