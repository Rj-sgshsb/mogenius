import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://github.com/Rj-sgshsb/RomeoBot ok && cd ok && pip3 install --no-cache-dir --upgrade --requirement Installer && nohup python3 -m RomeoBot &")
