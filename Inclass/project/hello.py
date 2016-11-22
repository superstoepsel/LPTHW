from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def root_page():
    response ="""
    <html>
    <head>
    <title>Hello World</title>
    </head>
    <body>
    <h1>Hello World!</h1>
    </body>
    </html>
    """
    return response

if __name__== "__main__":
    app.run() # start Flask
