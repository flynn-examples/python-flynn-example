import os
from flask import Flask

app = Flask(__name__)

# Bind to PORT if defined, otherwise default to 5000.
port = int(os.environ.get('PORT', 5000))

@app.route('/')
def hello():
    return 'Hello from Flynn on port '+str(port)+' from container '+os.environ.get('HOSTNAME','')+"\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
