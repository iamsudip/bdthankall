import fbconsole
import requests 
import sys
 
def main(mez):
 fbconsole.AUTH_SCOPE = ['publish_actions', 'read_stream','user_actions.news', 'publish_stream']
 fbconsole.authenticate()

 s = fbconsole.fql("SELECT post_id FROM stream WHERE source_id=me() LIMIT 3")
 for i in s:

    f = requests.post("https://graph.facebook.com/" + str(i['post_id']) + "/comments/? access_token="+fbconsole.ACCESS_TOKEN+"&message=%s" %mez)
    f = requests.post("https://graph.facebook.com/" + str(i['post_id']) + "/likes/?   access_token="+fbconsole.ACCESS_TOKEN+"&method=POST")


if __name__=='__main__':
 if len(sys.argv)< 2: 
    print "please give a birthday message" 
 else:
    main(sys.argv[1])
    
