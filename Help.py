#https://chat.ncss.cloud/syd-2-alfred
from flask import Flask, request, jsonify
import requests
import json


app = Flask(__name__)

#https://RundownGroundedServers--five-nine.repl.co/syd2/news
@app.route("/help", methods=['POST'])
def sources():
  #ASSEMBLE the REPLY
  reply =  "<b>Hi! My name is Alfred.</b><p>To get started, try searching something like 'Whats happening with <u>the cricket</u>?'</p><p>If you want help with a certain feature, type 'help' and choose a category:</p><ul><li>Fridge</li><li>Recipes</li><li>Diet and exercise</li><li>Entertainment</li><li>Is Bruce a Sandwich?</li></ul>"
  return jsonify({
  'author': 'Alfred',
  'text': reply
})

@app.route("/help-recipes", methods=['POST'])
def recipes():
  reply = "<b>Here are some commands for recipes and cooking:</b><ul><li>I'm going to start cooking <u>burger</u></li><li>Next step</li><li>Repeat step <u>3</u></li><li>Repeat previous step</li><li>What are the ingredients for <u>burger?</u></li><li>Gimme food</li><li>Let's cook that</li></ul>"
  return jsonify({
    'author': 'Alfred',
    'text': reply
  })

@app.route("/help-entertainment", methods=['POST'])
def entertainment():
  reply = '<b>Here are some commands for entertainment:</b><ul><li>What is the latest article from <u>bbc-news</u></li><li>Remind me that <u>The Simpsons</u> is on at <u>11:30</u></li><li>What is happening with <u>the bushfires?</u></li><li>Recommend me a <u>movie</u> like <u>inception</u></li></ul>'
  return jsonify({
    'author': 'Alfred',
    'text': reply
  })

@app.route("/help-fridge", methods=["POST"])
def fridge():
  reply = '<b>Here are the commands for fridge/pantry:</b><ul><li>Add <u>2L milk</u> to the <u>fridge</u></li><li>Remove <u>2 apples</u> from the <u>pantry</u></li><li>Clear the <u>fridge</u></li>'
  return jsonify({
    'author': 'Alfred',
    'text': reply
    })

@app.route("/help-diet", methods=['POST'])
def diet():
  reply = '<b>Here are some commands for diet and excercise:</b><ul><li>I weigh <u>60 kgs</u></li><li>I ate <u>burger</u></li><li>I just <u>ran</u> for <u>20</u> minutes</li><li>Alfred, tell me about <u>fruit pizza</u></ul>'
  return jsonify({
    'author': 'Alfred',
    'text': reply
    })

@app.route("/other", methods=['POST'])
def bruce():
  reply = '<marquee behavior="alternate"><h3 style ="font-family:comic-sans;color:red">Bruce is a Sandwich</h3></marquee>'
  args = request.get_json()
  if args.get('agent') == 'Alexa':
    reply = 'Bruce is a Sandwich'
  return jsonify({
    'author': 'Alfred',
    'text': reply
    })

app.run(host='0.0.0.0')

#ROOM SETTINGS FOR BOT
#NEWS BOT
#What's happening with (?P<Trigger>.*)
#https://RundownGroundedServers--five-nine.repl.co/syd2/news
