# coding: utf8

from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    print request.headers.get('User-Agent') # Print les infos du browser sur la console
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