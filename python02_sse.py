from flask import Flask, Response
from flask_cors import CORS
import redis

app = Flask(__name__)
CORS(app)

app.secret_key = 'asdf' 
red = redis.StrictRedis() 
def event_stream(): 
    pubsub = red.pubsub() 
    pubsub.subscribe('chat') 
    # TODO: handle client disconnection. 
    for message in pubsub.listen(): 
        print (message) 
        if message['type']=='message': 
            yield 'data: %s\n\n' % message['data'].decode('utf-8')



@app.route('/')
def index():
    return 'Index Page'

@app.route('/world')
def world():
    return 'Hello World!'

@app.route('/stream') 
def stream(): 
    return Response(event_stream(), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run(debug=True)
