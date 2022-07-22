import os
import random
from flask import Flask , Response
from slack import WebClient
from slackeventsapi import SlackEventAdapter


app = Flask(__name__)

slack_event_adaptor = SlackEventAdapter(os.environ.get("SLACK_ET"),"/slack/event",app)
slack_web_client =WebClient(token=os.environ.get("SLACK_BT"))

MESSAGE_BLOCK = {
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Result is"
			},
		},
		{
			"type": "actions",
			"block_id": "actionblock789",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Play Again"
					},
					"style": "primary",
					"value": "click_me_456"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Thank You"
					},
					"url": "https://api.slack.com/block-kit"
				}
			]
		}
	]
}
@app.route('/slack/add',methods =['POST'])
def add():
    return Response(), 200

@slack_event_adaptor.on("message")
def message(payload):
    print(payload)
    event = payload.get("event",{})
    text = event.get("text")
    if "flip a coin" in text.lower():
        channel_id = event.get("channel")

        rand_int = random.randint(0,1)
        if rand_int == 0 :
            result = "Heads"
        else:
            result = "Tails"
        message =f"The result is {result}"
        
        MESSAGE_BLOCK["blocks"]["section"]["text"]["text"]=message

        message_to_send ={"channel":channel_id, MESSAGE_BLOCK}

        return slack_web_client.chat_postMessage(**message_to_send)

if __name__ =='__main__':
    app.run(host="0.0.0.0",port=8080)