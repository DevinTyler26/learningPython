from flask import Flask
from app import app

@app.route('/')
def hello():
  return '''<html>
              <title>Devin's Trivia Game</title>
                <body>
                  <h1>Hello World!!!</h1>
                </body
              </html>'''

@app.route('/create')
def create():
  return '<h2>This is the create page</h2>'

@app.route('/question/<title>')
def question(title):
  return '<h2>' + title + '</h2>'