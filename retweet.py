import tweepy.errors
from secret import *
import random
import schedule
import requests
import time


def retweet1(n):
    try:
        lista = open('lista.txt', 'r')
        itens = lista.readlines()
        word = random.choice(itens).strip('\n') + ' -is:retweet lang:pt'
        # uber  -is:retweet lang:pt

        print(keys[n]['User'] + ' Key word: ' + word[:word.find('-')])
            # do_kaioshin  Key word: uber

        ids = list()
        for tweet in client(n).search_recent_tweets(query=word, max_results=20).data:
            ids.append(tweet.id)

        if len(ids) == 0:
            retweet1(n)
        else:
            ret = random.choice(ids)
            print(client(n).retweet(ret))
            print(client(n).like(ret))

    except (TypeError, requests.exceptions.RequestException, requests.exceptions.ConnectionError,
            tweepy.errors.BadRequest, tweepy.errors.Forbidden, tweepy.errors.TwitterServerError):
        time.sleep(300)
        retweet1(n)


def retweet2(n):
    try:
        lista = open('hashtag.txt', 'r')
        itens = lista.readlines()
        word = random.choice(itens).strip('\n') + ' -is:retweet lang:pt'
        ids = list()
        print(keys[n]['User'] + ' Key word: ' + word[:word.find('-')])

        for tweet in client(n).search_recent_tweets(query=word, max_results=20).data:
            ids.append(tweet.id)

        if len(ids) == 0:
            retweet2(n)
        else:
            ret = random.choice(ids)
            print(client(n).retweet(ret))
            print(client(n).like(ret))

    except (TypeError, requests.exceptions.RequestException, requests.exceptions.ConnectionError,
            tweepy.errors.BadRequest, tweepy.errors.Forbidden, tweepy.errors.TwitterServerError):
        time.sleep(300)
        retweet2(n)


def retweet3(n):
    try:
        lista = open('lista2.txt', 'r')
        itens = lista.readlines()
        word = random.choice(itens).strip('\n') + ' -is:retweet lang:pt'
        ids = list()
        print(keys[n]['User'] + ' Key word: ' + word[:word.find('-')])

        for tweet in client(n).search_recent_tweets(query=word, max_results=20).data:
            ids.append(tweet.id)

        if len(ids) == 0:
            retweet3(n)
        else:
            ret = random.choice(ids)
            print(client(n).retweet(ret))
            print(client(n).like(ret))

    except (TypeError, requests.exceptions.RequestException, requests.exceptions.ConnectionError,
            tweepy.errors.BadRequest, tweepy.errors.Forbidden, tweepy.errors.TwitterServerError):
        time.sleep(300)
        retweet3(n)


schedule.every(1).to(10).minutes.do(retweet2, n=0)
schedule.every(1).to(10).minutes.do(retweet3, n=1)
schedule.every(1).to(10).minutes.do(retweet2, n=2)
schedule.every(1).to(10).minutes.do(retweet1, n=3)
schedule.every(1).to(10).minutes.do(retweet2, n=4)
while True:
    schedule.run_pending()
    time.sleep(1)
