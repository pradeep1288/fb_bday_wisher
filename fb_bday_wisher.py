#!/usr/bin/python

from facepy import GraphAPI
import datetime
import random

oauth_token = 'FB_API'
graph = GraphAPI(oauth_token)
friend_list = graph.get("me/friends?fields=birthday")
birthday_wishes = ["Life wouldn't be the same without a friend like you. Happy Birthday!",
"My best wishes for a furious and voracious day filled with plenty of smile and laughter. Happy Birthday to you!",
"May the special day of yours be filled with loving memories full of fun and the company of good friends. Happy Birthday!",
"Look for the best and leave behind all the rest. Happy Birthday my friend!",
"One year older means one year wiser. The truth is that our company needed an old wise person like you. Happy Birthday my friend"
]
friend_list_bday_ids = []

#Get today's day and month
now = datetime.datetime.now().strftime("%m-%d")
month_day = now.split('-')

for friend in friend_list['data']:
    if friend.has_key('birthday'):
        bday_array = friend['birthday'].split('/')
        if bday_array[0] == month_day[0] and bday_array[1] == month_day[1]:
            friend_list_bday_ids.append(friend)