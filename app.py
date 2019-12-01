import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["initialstate", "moviestateask", "atmovies", "envy",
            "upsetstateask", "upsetstatesolve", "showfunction", "present",
			"upsetstatesolve2", "newsstateask", "technewsstateask", "gasprice",
			"technews", "panx"],
    transitions=[
	    #{
        #    "trigger": "advance",
        #    "source": "initialstate",
        #    "dest": "state1",
        #    "conditions": "is_going_to_state1",
        #},
        # 1
        {
            "trigger": "advance",
            "source": "initialstate",
            "dest": "showfunction",
            "conditions": "is_going_to_showfunction",
        },
        #2
        {
            "trigger": "advance",
            "source": "initialstate",
            "dest": "moviestateask",
            "conditions": "is_going_to_moviestateask",
        },
        #3
        {
            "trigger": "advance",
            "source": "moviestateask",
            "dest": "atmovies",
            "conditions": "is_going_to_atmovies",
        },
        #4
        {
            "trigger": "advance",
            "source": "moviestateask",
            "dest": "envy",
            "conditions": "is_going_to_envy",
        },
        #5
        {
            "trigger": "advance",
            "source": ["moviestateask", "upsetstateask"],
            "dest": "initialstate",
            "conditions": "is_going_to_back",
        },
        #6
        {
            "trigger": "advance",
            "source": "initialstate",
            "dest": "upsetstateask",
            "conditions": "is_going_to_upsetstateask",
        },
        #7
        {
            "trigger": "advance",
            "source": "upsetstateask",
            "dest": "upsetstatesolve",
            "conditions": "is_going_to_upsetstatesolve",
        },
        #8
        {
            "trigger": "advance",
            "source": "upsetstatesolve",
            "dest": "moviestateask",
            "conditions": "is_going_to_moviestateask",
        },
        #9
        {
            "trigger": "advance",
            "source": "upsetstatesolve",
            "dest": "present",
            "conditions": "is_going_to_present",
        },
		#10
        {
            "trigger": "advance",
            "source": "upsetstatesolve",
            "dest": "initialstate",
            "conditions": "is_going_to_ini",
        },
		#11
        {
            "trigger": "advance",
            "source": "initialstate",
            "dest": "newsstateask",
            "conditions": "is_going_to_newsstateask",
        },
		#12
        {
            "trigger": "advance",
            "source": "newsstateask",
            "dest": "technewsstateask",
            "conditions": "is_going_to_tech",
        },
		#13
        {
            "trigger": "advance",
            "source": "technewsstateask",
            "dest": "technews",
            "conditions": "is_going_to_technews",
        },
		#14
        {
            "trigger": "advance",
            "source": "technewsstateask",
            "dest": "panx",
            "conditions": "is_going_to_panx",
        },
		#15
        {
            "trigger": "advance",
            "source": "newsstateask",
            "dest": "gasprice",
            "conditions": "is_going_to_gasprice",
        },
        #16
        {
            "trigger": "advance",
            "source": "upsetstateask",
            "dest": "upsetstatesolve2",
            "conditions": "is_going_to_upsetstatesolve2",
        },
		#17
        {
            "trigger": "advance",
            "source": "upsetstatesolve2",
            "dest": "gasprice",
            "conditions": "is_going_to_upset",
        },
        #Back To initial 1
        {
            "trigger": "go_back",
            "source": ["state1", "atmovies", "envy", "showfunction", "present", "gasprice",
			           "technews", "panx"],
            "dest": "initialstate"
        },
		#Back To initial 2
        {
            "trigger": "advance",
            "source": ["moviestateask", "atmovies", "envy",
                       "upsetstateask", "upsetstatesolve", "showfunction", "present",
			           "upsetstatesolve2", "newsstateask", "technewsstateask", "gasprice",
			           "technews", "panx"],
            "dest": "initialstate",
			"conditions": "reset",
        },
    ],
    initial="initialstate",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Wrong instruction!! PLS check your spelling!!")

    return "OK"


@app.route("/show-fsm", methods=["Get"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
