from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer
from dotenv import load_dotenv
import os
import logging


app = Flask(__name__)


@app.route("/")
def get_bot_response():
    try:
        userText = request.args.get('message')
        if userText is None:
            return str("No message argument provided")
        return str(pan_japa.get_response(userText))
    except Exception as e:
        print(e)
        return str("Something went wrong")

print("Loading enviroment variables...")
load_dotenv(verbose=True)
print("Connecting chatbot to Db...")
logging.basicConfig(level=logging.DEBUG)
pan_japa = ChatBot("Pan Japa",
                    storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                    database = "gymba",
                    database_uri = os.getenv("MONGO_CONNECTION_STRING"))
print("Creating trainer...")
trainer = UbuntuCorpusTrainer(pan_japa)
print("Training chatbot...")
trainer.train()
print("Training is finished!")
app.run(host='0.0.0.0', debug=True, port=80)
print("Done!")
