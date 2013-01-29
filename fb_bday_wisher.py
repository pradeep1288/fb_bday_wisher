#!/usr/bin/python

import facebook
import datetime
import random

oauth_token = 'FB_ACCESS_TOKEN'
graph = facebook.GraphAPI(oauth_token)
friend_list = graph.get_object("me/friends")
birthday_wishes = ["Life wouldn't be the same without a friend like you. Happy Birthday!",
"My best wishes for a furious and voracious day filled with plenty of smile and laughter. Happy Birthday to you!",
"May the special day of yours be filled with loving memories full of fun and the company of good friends. Happy Birthday!",
"Look for the best and leave behind all the rest. Happy Birthday my friend!",
"One year older means one year wiser. The truth is that our company needed an old wise person like you. Happy Birthday my friend"
]
friend_list_ids = []
friend_list_bday_ids = []

#Get the list of all my friends and store their id's
for friend in friend_list['data']:
    friend_list_ids.append(friend['id'])

#Get today's day and month
now = datetime.datetime.now().strftime("%m-%d")
month_day = now.split('-')

#Iterate through my friend list and find out whose birthdays is it today
for friend in friend_list_ids:
    # Deal with any exceptions and prevent the loop from terminating
    try:
        each_friend = graph.get_object(friend)
        if each_friend.has_key('birthday'):
            bday_array = each_friend['birthday'].split('/')
            if bday_array[0] == month_day[0] and bday_array[1] == month_day[1]:
                friend_list_bday_ids.append(friend)
    except:
        pass 
        
# Now wish the friends with a random happy birhthay message            
for friend in friend_list_bday_ids:
    bday_wish  = birthday_wishes[random.randint(0, len(birthday_wishes) -1) ]
    graph.put_object(friend, 'feed', message = bday_wish)