from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('mongodb://fellong:fellon@54.180.114.229', 27017)
db = client.dbsparta


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('fellonparty.html')


# API 역할을 하는 부분
@app.route('/apply', methods=['POST'])
def apply():
    name = request.form['name']
    gender = request.form['gender']
    count = request.form['count']
    address = request.form['address']
    phone = request.form['phone']

    user = db.fellonparty.find_one({'name': name, 'phone': phone})
    if user is not None:
        return jsonify({
            'success': 'false',
            'message': 'This user is already applied'
        })

    data = {'name': name, 'gender': gender, 'count': count,
               'address': address, 'phone': phone}

    db.fellonparty.insert_one(data)

    return jsonify({'success': 'true'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
