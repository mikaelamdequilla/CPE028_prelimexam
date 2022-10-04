import json
from operator import index
from flask import Flask, jsonify, request

app = Flask(__name__)
temps=[

    { 
        "temp_id" : "1",
        "date": "Aug. 5, 2022",
        "temperature": "36 Celsius"
    }
]

@app.route('/temps', methods=['GET'])
def readTemp():
    return jsonify(temps)

@app.route('/temps/<string:temp_id>')
def getTemp(temp_id):
    for temp in temps:
        if (temp['temp_id']==temp_id):
            return jsonify(temp)
    return jsonify({'message':'ID not found'})

@app.route('/temps',methods=['POST'])
def addTemp():
    temp =request.get_json()
    temps.append(temp)
    return {'successfully added':len(temps)},200

@app.route('/temps/<int:index>',methods=['DELETE'])
def deleteTemp(index):
    temps.pop(index)
    return 'Temperature record was successfully deleted',200


if __name__ == '__main__':
    app.run()