import requests
import emoji
from slacker import Slacker

def sendmotivationalquote():
    slack = Slacker("xxxxxxxxxxxxxxxxxxxxxxxxxx") # Slack token 
    slack_channel_name = "notification-code"
    URL = "https://zenquotes.io/api/quotes/"
    response = requests.request("GET", url=URL)
    try:
         if response.status_code == requests.codes.ok:
            data = response.json()
            quote = data[0]["q"]
            author = data[0]["a"]

            slack.chat.post_message(slack_channel_name, "Todays Quote is: "+ quote);
            slack.chat.post_message(slack_channel_name, "Author: " + author);
            
            print(emoji.emojize("Motivaional quote has been successfully sent to Slack :trophy:"))
    except requests.exceptions.HTTPError as err:
           print(err)

if __name__ == "__main__":
    sendmotivationalquote()
