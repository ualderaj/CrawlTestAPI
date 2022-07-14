import os.path
import random
import requests
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

#random_crawl API endpoint
@app.route('/random_crawl', methods=['GET'])
def randomcrawl():
    if(request.method == 'GET'):

        #random number from 1 to 6 to decide on film number to pull
        randomNumber = random.randint(1,6)

        #build the swapi.dev api url based on the randomnumber
        theurl = 'https://swapi.dev/api/films/' + str(randomNumber) +'/?format=json'

        #Pre Header data for the data return result
        startdata = '{"file_name": "'
        headingdata = '","opening_crawl":['

        #Make the call to the swapi.dev URL to pull the data for the movie
        req = requests.get(theurl).json()

        #pull the title of the movie
        thefile = req['title']

        #pull the opening crawl for the movie
        strreq = req['opening_crawl']

        #setup the separater for the end result to ensure json formatting
        reqsep = '","'

        #split out the single string opening_crawl into a json format with one line per element
        endreq = reqsep.join(strreq.split('\r\n'))

        #ensure the completed opening_crawl is a string
        crawl = str(endreq)

        #prep the end of the return result
        enddata = '"]}'

        #assemble the return data
        data = startdata + thefile + headingdata + crawl + enddata

        return data


#random_crawl_reverse API endpoint
@app.route('/random_crawl_reverse', methods=['GET'])
def randomcrawlreverse():
    if(request.method == 'GET'):

        #random number from 1 to 6 to decide on film number to pull
        randomNumber = random.randint(1,6)

        #build the swapi.dev api url based on the randomnumber
        theurl = 'https://swapi.dev/api/films/' + str(randomNumber) +'/?format=json'

        #Pre Header data for the data return result
        startdata = '{"file_name": "'
        headingdata = '","opening_crawl":['

        #Make the call to the swapi.dev URL to pull the data for the movie
        req = requests.get(theurl).json()

        #pull the title of the movie
        thefile = req['title']

        #pull the opening crawl for the movie
        strreq = req['opening_crawl']

        #setup the separater for the end result to ensure json formatting
        reqsep = '","'

        #split out the single string opening_crawl, reverse the elements order and convert into a json format with one line per element
        endreq = reqsep.join(reversed(strreq.split('\r\n')))

        #ensure the completed opening_crawl is a string
        crawl = str(endreq)

        #prep the end of the return result
        enddata = '"]}'

        #assemble the return data
        data = startdata + thefile + headingdata + crawl + enddata

        return data


if __name__ == '__main__':
    app.run(debug=True,port=8080)
