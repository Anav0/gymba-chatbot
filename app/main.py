from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer
from dotenv import load_dotenv
import os



app = Flask(__name__)

@app.route("/")
def get_bot_response():
    try:
        userText = request.args.get('message')
        if userText is None:
            return str("No message argument provided")
        return str(pan_japa.get_response(userText))
    except Exception:
        return str("Something went wrong")


if __name__ == "__main__":
    print("1")
    load_dotenv(verbose=True)
    print("2")
    pan_japa = ChatBot("Pan Japa",
                     storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                     database = "gymba",
                     database_uri = os.getenv("MONGO_CONNECTION_STRING"))
    print("3")
    trainer = UbuntuCorpusTrainer(pan_japa)
    print("4")
    trainer.train()
    print("5")
    app.run(host='0.0.0.0', debug=True, port=80)
    print("6")