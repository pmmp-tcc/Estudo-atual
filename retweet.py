from secret import *
import random
import schedule
import requests
import time


def retweet1(n):#n é a conta que vai retweetar  #somente hashtags
        lista = open('hashtag.txt', 'r') #abre o arquivo hashtag.txt que contém hashtags
        itens = lista.readlines()
        word = random.choice(itens).strip('\n') + ' -is:retweet lang:pt' #escolhe uma hashtag de hashtag.txt 
        # uber  -is:retweet lang:pt #exemplo do conteúdo do objeto word / #-is:retweet lang:pt para excluir os retweets, quer apenas os tweets da hashtag em português

        print(keys[n]['User'] + ' Key word: ' + word[:word.find('-')]) #fornece a conta honeypot que publicará o retweet com a hashtag selecionada 
            # do_kaioshin  Key word: uber #exemplo

        ids = list()
        for tweet in client(n).search_recent_tweets(query=word, max_results=20).data: #para pesquisar os 20 mais recentes tweets com a hashtag
            ids.append(tweet.id) #obter id de cada tweet

        if len(ids) == 0: #se a lista ids estiver vazia
            retweet1(n) #executa novamente essa função
        else:
            ret = random.choice(ids) #escolher aleatoriamente um id do tweet
            print(client(n).retweet(ret)) #para retweet 
            print(client(n).like(ret)) #curtir a publicação 

    

def retweet2(n): #hashtags e palavras
        lista = open('lista.txt', 'r') #abre o arquivo lista.txt que contém palavras e hashtags
        itens = lista.readlines()
        word = random.choice(itens).strip('\n') + ' -is:retweet lang:pt' #escolhe aleatoriamente um termo de lista.txt
        
        print(keys[n]['User'] + ' Key word: ' + word[:word.find('-')]) #fornece a conta honeypot que publicará o retweet com o termo selecionado
        
        ids = list()
        for tweet in client(n).search_recent_tweets(query=word, max_results=20).data: #para pesquisar os 20 mais recentes tweets com o termo
            ids.append(tweet.id)

        if len(ids) == 0:
            retweet3(n)
        else:
            ret = random.choice(ids)
            print(client(n).retweet(ret))
            print(client(n).like(ret))

    
#retweet entre 1 a 10 minutos
schedule.every(1).to(10).minutes.do(retweet2, n=0) #conta honeypot publica retweet que contém hashtag ou palavra
schedule.every(1).to(10).minutes.do(retweet1, n=1) #conta honeypot publica retweet que contém hashtag 
schedule.every(1).to(10).minutes.do(retweet2, n=2) #conta honeypot publica retweet que contém hashtag ou palavra
schedule.every(1).to(10).minutes.do(retweet1, n=3) #conta honeypot publica retweet que contém hashtag 
schedule.every(1).to(10).minutes.do(retweet2, n=4) #conta honeypot publica retweet que contém hashtag ou palavra
schedule.every(1).to(10).minutes.do(retweet1, n=5) #conta honeypot publica retweet que contém hashtag 
schedule.every(1).to(10).minutes.do(retweet2, n=6) #conta honeypot publica retweet que contém hashtag ou palavra
schedule.every(1).to(10).minutes.do(retweet1, n=7) #conta honeypot publica retweet que contém hashtag 
schedule.every(1).to(10).minutes.do(retweet2, n=8) #conta honeypot publica retweet que contém hashtag ou palavra
schedule.every(1).to(10).minutes.do(retweet2, n=9) #conta honeypot publica retweet que contém hashtag ou palavra
while True:
    schedule.run_pending()
    time.sleep(1)
