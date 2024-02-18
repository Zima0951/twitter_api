
from flask import Flask, jsonify
from flask import request
import json

from model.twit import Twit 
#import jsonpickle



twits = []

app = Flask(__name__)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,Twit):
            return {"body": obj.body, "author": obj.author}
        else:
            return super().default(obj)        
        #return json.JSONEncoder.default()
    
app.json_encoder = CustomJSONEncoder

@app.route('/ping',methods=['GET'])
def ping():
    return jsonify({'response':'pong'} )

@app.route('/twit',methods=['POST'])
def create_twit():
    #twits = {"body":"hello world", "author":"@zima"}
    twit_json = request.get_json()
    twit = Twit(twit_json["body"],twit_json["author"])
    twits.append(twit)
    return jsonify({'status':'succes'})


@app.route('/twit',methods=['GET'])
def read_twits():
    twit_json = [twit.to_json() for twit in twits]
    return jsonify({'twits': twit_json})




if __name__=='__main__':
    app.run(debug=True)
    
    
