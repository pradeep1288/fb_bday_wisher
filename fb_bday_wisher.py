#!/usr/bin/python

import facebook

oauth_token = 'AAACEdEose0cBAL0tZAicV6ZCKB2FrKhqNxK5GPXsJHhZACg4tvw4bqjhCyHDbDzOhXxjbrkOIG8jTZBIUG4cKahwMzhIWjUV8b30uFTigQZDZD'
graph = facebook.GraphAPI(oauth_token)
friend_list = graph.get_object("me/friends")
friend_list_ids = []

for friend in friend_list['data']:
    friend_list_ids.append(friend['id'])

friend_list_bdays = []


for friend in friend_list_ids:
    try:
        each_friend = graph.get_object(friend)
        if each_friend.has_key('birthday'):
            friend_list_bdays.append(each_friend['birthday'])
            print each_friend['birthday']
    except:
        pass     
print friend_list_bdays