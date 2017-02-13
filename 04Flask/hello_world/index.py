# Coding: utf8

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return """
       <html>
         <head>
           <title>Hello World!</title>
           <meta charset='utf-8'>
         </head>
         <body>
           <h1>Hello World!</h1>
         </body>
       </html>
       """