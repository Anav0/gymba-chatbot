
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

app = Flask(__name__)

pan_japa = ChatBot("Pan Japa",
                     storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                     database = "gymba",
                     database_uri = os.getenv("MONGO_CONNECTION_STRING"))

trainer = ChatterBotCorpusTrainer(pan_japa)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def get_bot_response():
    try:
        userText = request.args.get('message')
        if userText is None:
            return str("No message argument provided")
        return str(pan_japa.get_response(userText))
    except Exception:
        return str("Somthing went wrong")


if __name__ == "__main__":
    app.run("localhost",6000)