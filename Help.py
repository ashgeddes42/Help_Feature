#https://chat.ncss.cloud/syd-2-alfred
from flask import Flask, request, jsonify
import requests
import json


app = Flask(__name__)

#https://RundownGroundedServers--five-nine.repl.co/syd2/news
@app.route("/help", methods=['POST'])
def sources():
  #GET the query / what they want to hear about
  '''
  args = request.get_json()
  query = args['params']['']
  '''
  #ASSEMBLE the REPLY
  reply =  "<p>Hi! My name is Alfred. To get started, try searching something like 'Whats happening with <u>the cricket</u>?' <p>If you want help with a certain feature, type choose a category:</p><p><ul><li>Fridge</li><li>Recipes</li><li>Diet and exercise</li><li>Entertainment</li></ul>"

@app.route("/help-recipes", methods=['POST'])
def recipes():
  reply = "<ul><li>I'm going to start cooking <u>burger</u></li><li>Next step</li><li>Repeat step <u>3</u></li><li>Repeat previous step</li><li>What are the ingredients for <u>burger?</u></li><li>Let's cook that</li></ul>"
  return jsonify({
    'text': reply
  })

@app.route("/help-entertainment", methods=['POST'])
def entertainment():
  reply = '<ul><li>What is the latest article from <u>bbc-news</u></li></ul>'
  return jsonify({
    'text': reply
  })

@app.route("/help-fridge"
  fridge =  '<ul><li>Add <u>4 apples</u> to the <u>fridge</u></li><li>Remove <u>2 apples</u> from the <u>fridge</u></li><li>Clear the <u>fridge</u></li>'

@app.route("/h")
  d_e = '<ul><li>I weigh </u>60 kgs</u></li><li>I ate <u>burger</u></li><li>I just <u>ran</u> for <u>20</u> minutes</li></ul>'



    #GIVE the REPLY back to USER
  return jsonify({
    'author': 'Alfred',
    'text': reply,
    })

app.run(host='0.0.0.0')

#ROOM SETTINGS FOR BOT
#NEWS BOT
#What's happening with (?P<Trigger>.*)
#https://RundownGroundedServers--five-nine.repl.co/syd2/news
