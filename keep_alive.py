from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Scythe Bot is currently online. Join the server: https://discord.gg/JyBbNSRx8S"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()