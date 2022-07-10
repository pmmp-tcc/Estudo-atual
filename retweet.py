import tweepy.errors
from secret import *
import random
import schedule
import requests
import time


def retweet1(n):#n é a conta que vai retweetar
        lista = open('lista.txt', 'r') #abre o arquivo lista.txt que contém palavras
        itens = lista.readlines()
        word = random.choice(itens).strip('\n') + ' -is:retweet lang:pt' #escolhe uma palavra aleatória de lista.txt 
        # uber  -is:retweet lang:pt #exemplo do conteúdo do objeto word / #-is:retweet lang:pt para excluir os retweets, quer apenas os tweets da palavra em português

        print(keys[n]['User'] + ' Key word: ' + word[:word.find('-')]) #fornece a conta honeypot que publicará o retweet com a palavra selecionada e que terá retweet
            # do_kaioshin  Key word: uber #exemplo

        ids = list()
        for tweet in client(n).search_recent_tweets(query=word, max_results=20).data: #para pesquisar os 20 mais recentes tweets com a palavra
            ids.append(tweet.id) #obter id de cada tweet

        if len(ids) == 0: #se a lista ids estiver vazia
            retweet1(n) #executa novamente essa função
        else:
            ret = random.choice(ids) #escolher aleatoriamente um id do tweet
            print(client(n).retweet(ret)) #para retweet 
            print(client(n).like(ret)) #curtir a publicação

    
def retweet2(n): #somente hashtags
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

    
def retweet3(n):
        lista = open('lista2.txt', 'r') #palavras e hashtags
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

    
#retweet entre 1 a 10 minutos
schedule.every(1).to(10).minutes.do(retweet1, n=0) 
schedule.every(1).to(10).minutes.do(retweet2, n=1)
schedule.every(1).to(10).minutes.do(retweet1, n=2)
schedule.every(1).to(10).minutes.do(retweet2, n=3)
schedule.every(1).to(10).minutes.do(retweet1, n=4)
schedule.every(1).to(10).minutes.do(retweet2, n=5)
schedule.every(1).to(10).minutes.do(retweet1, n=6)
schedule.every(1).to(10).minutes.do(retweet2, n=7)
schedule.every(1).to(10).minutes.do(retweet1, n=8)
schedule.every(1).to(10).minutes.do(retweet2, n=9)
while True:
    schedule.run_pending()
    time.sleep(1)
