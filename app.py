from flask import Flask
import os
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World v1"


if __name__ == '__main__':
    print('Server started')
    app.run(host='0.0.0.0', port=80)
else:
    print('Something went wrong')

        
