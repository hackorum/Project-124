from flask import Flask, jsonify, request

app = Flask(__name__)
nums = [
    {
        'id': 1,
        'number': u'1234567890',
        'name': u'Someone',
    },
    {
        'id': 2,
        'title': u'098764321',
        'name': u'Not Someone',
    },
]

@app.route('/')
def HelloWorld():
    return 'Welcome To The Phone Number API'

@app.route('/add_data', methods=['POST'])
def add_data():
    if not request.json:
        return jsonify({'status': 'error', 'message': 'Please provide data in json format'}, 400)
    num = {
            'id': nums[-1]['id'] + 1,
            'number': request.json['number'],
            'name': request.json.get('name',""),
           }
    nums.append(num)
    return jsonify({'status': 'success', 'message': 'Number added successfully'})
@app.route('/get_data')
def get_data():
    return jsonify({'data': nums})
    
if __name__ == '__main__':
    app.run(debug=True)