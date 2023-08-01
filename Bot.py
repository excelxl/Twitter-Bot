from requests_oauthlib import OAuth1Session
import tweepy
import os
import json
from time import sleep
import requests
from Funcs import *


def retweet(id):
    print()


def check(input, criteria):
    count = 0
    arr = input.split(" ")
    f = open("input.txt", "r")
    inp = f.read()
    for i in arr:
        if i in inp:
            count += 1
    if count > criteria:
        return True
    return False


def get(input, bearer_token):
    auth = tweepy.OAuth2BearerHandler(bearer_token)
    api = tweepy.API(auth)
    str = api.get_status(input, tweet_mode="extended")._json["full_text"]
    return str


def find(bearer_token, query_params):
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(search_url, headers, query_params)
    return json.dumps(json_response, indent=4, sort_keys=True)


def main():
    with open(r"C:\Users\white\Documents\Bot\config.json") as json_file:
        data = json.load(json_file)
    consumer_key = data["CONSUMER_KEY"]
    consumer_secret = data["CONSUMER_SECRET"]
    bearer_token = data["BEARER_TOKEN"]
    query_params = data["QUERY"]
    criteria = data["CRITERIA"]
    while True:
        str = find(bearer_token, query_params)
        arr = []
        str = json.loads(str)
        for set in str:
            arr.append([set["text"], set["id"]])
        for i in arr:
            if check(i["text"], criteria) == True:
                retweet(i["id"])
        

if __name__ == "__main__":
    main()
