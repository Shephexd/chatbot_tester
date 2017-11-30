from flask import Flask, request
import json, sys

app = Flask(__name__)
home_button = {'type': 'buttons', 'buttons': ['Home', 'button 1', 'button 2', 'button 3']}
mykeyboard = json.dumps(home_button, ensure_ascii=False)

@app.route('/')
def hello():
    return 'hello, world!'

def make_reply(message):
    response_message = message
    return response_message

@app.route('/reply_test', methods=['GET'])
def test_reply():
    message = request.args.get('message')
    response_message = make_reply(message)
    return response_message

@app.route('/keyboard')
def keyboard():
    return mykeyboard


@app.route('/message', methods=['POST'])
def post_message():
    user_message = request.get_json()
    user_content = user_message['content']
    print(repr(user_content))

    if str(user_content) in ['Home', 'home', '홈']:
        return mykeyboard
    return make_reply(user_content)


if __name__ == '__main__':
    app.run()
