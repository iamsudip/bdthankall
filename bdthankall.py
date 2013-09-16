#!/usr/bin/env python

import fbconsole
import requests


def bdaythank(post_limit, comment=None):
    ''' Likes and comments all posts automatically
    '''

    fbconsole.AUTH_SCOPE = ['publish_actions', 'read_stream',
                            'user_actions.news', 'publish_stream'
                           ]

    fbconsole.authenticate()

    query = fbconsole.fql("SELECT post_id FROM stream WHERE source_id=me() LIMIT %s" % post_limit)


    for post in query:
        if comment:
            comment_id = requests.post("https://graph.facebook.com/" + str(post['post_id'])
                                   + "/comments/?access_token=" + fbconsole.ACCESS_TOKEN 
                                   + "&message=%s" % comment
                                  )
            print "Comment id: " + comment_id.text

        requests.post("https://graph.facebook.com/" + str(post['post_id'])
                      + "/likes/?access_token=" + fbconsole.ACCESS_TOKEN + "&method=POST"
                     )
        print "$ Liked"

    fbconsole.logout()


if __name__=='__main__':
    limit = raw_input("How many post I have to like? ")
    comment = raw_input("Any message to your friends? ")
    bdaythank(limit, comment)
    print "All done!"
