#https://chat.ncss.cloud/syd-2-alfred
from flask import Flask, request, jsonify
import requests
import json


app = Flask(__name__)

#https://RundownGroundedServers--five-nine.repl.co/syd2/news
@app.route("/recipes", methods=['POST'])
def sources():
  #GET the query / what they want to hear about

  #ASSEMBLE the REPLY
  recipes = "<p>Here are some commands involving recipes:</p><ul><li>I'm going to start cooking <u>burger</u></li><li>Next step</li><li>Repeat step <u>3</u></li><li>What are the ingredients for <u>burger?</u></li><li>Let's cook that</li></u>"

    #GIVE the REPLY back to USER
  return jsonify({
    'author': 'Alfred',
    'text': recipes,
    })

app.run(host='0.0.0.0')

#ROOM SETTINGS FOR BOT
#NEWS BOT
#What's happening with (?P<Trigger>.*)
#https://RundownGroundedServers--five-nine.repl.co/syd2/news
