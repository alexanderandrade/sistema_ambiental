import tweepy 
from time import sleep
from datetime import datetime
from textblob import TextBlob 
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
from credenciales import *
import os
import csv
import json

class Tendencia():
    def obtener_tendencia(self,nombre_tendencia,numero,idioma):
        #Se autentica en twitter
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True) 

        #Se pregunta por la palabra a preguntar
        palabra = nombre_tendencia

        #Se define la cantida de tweets a capturar
        numero_de_Tweets = int(numero)

        #Se define el idioma de los tweets a analizar
        lenguaje = idioma

        def ObtenerTweets(palabra,times,lenguaje):
            #Se define las listas que capturan la popularidad
            tweet_list = []
            polaridad_list = []
            objetividad_list = []
            numero_list= []
            numero = 1
            longitud_list=[]
            id_list=[]
            fecha_list=[]
            fuente_list=[]
            likes_list=[]
            rts_list=[]

            for tweet in tweepy.Cursor(api.search, palabra, lang=lenguaje).items(numero_de_Tweets):
                try:
                    #Se toma el texto, se hace el analisis de sentimiento
                    #y se agrega el resultado a las listas

                    analisis = TextBlob(tweet.text)
                    polaridad_sentimiento = analisis.sentiment.polarity
                    objetividad_sentimiento = analisis.sentiment.subjectivity
                    longitud = len(tweet.text)
                    id_t=tweet.id
                    fecha=tweet.created_at
                    fuente = tweet.source
                    likes=tweet.favorite_count
                    rts= tweet.retweet_count

                    tweet_list.append(tweet.text)
                    polaridad_list.append(polaridad_sentimiento)
                    objetividad_list.append(objetividad_sentimiento)
                    numero_list.append(numero)
                    numero += numero
                    longitud_list.append(longitud)
                    id_list.append(id_t)
                    fecha_list.append(fecha)
                    fuente_list.append(fuente)
                    likes_list.append(likes)
                    rts_list.append(rts)


                except tweepy.TweepError as e:
                    print(e.reason)

                except StopIteration:
                    break
                
            datos=pd.DataFrame({'polaridad':polaridad_list, 'objetividad':objetividad_list, 'tweet' : tweet_list,
                'longitud':longitud_list, 'id':id_list,'fecha':fecha_list,'fuente':fuente_list,'likes':likes_list,'RTs':rts_list})
            return(datos)

        data = ObtenerTweets(palabra,numero_de_Tweets,lenguaje)
        #data.to_csv("tweets.csv",encoding='utf-8')
        data_final=data.to_json(orient='columns')
        return (data_final)

