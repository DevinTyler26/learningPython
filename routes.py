from flask import Flask, url_for, request, render_template
from app import app

@app.route('/')
def hello():
  createLink = "<a href='" + url_for('create') + "'>Create a question</a>"
  return """<html>
              <title>Devin's Trivia Game</title>
                <body>
                  <h1>Hello World!!!</h1>
                  """ + createLink + """
                </body
              </html>"""

@app.route('/create', methods=['GET', 'POST'])
def create():
  if request.method == 'GET':
    return render_template('CreateQuestion.html')
  elif request.method == 'POST':
    title = request.form['title']
    question = request.form['question']
    answer = request.form['answer']
    return render_template('CreatedQuestion.html', question = question)
  else:
    return '<h2>Bad Request</h2>'

@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
  if request.method == 'GET':
    question = 'Question here...'
    return render_template('AnswerQuestion.html', question = question)
  elif request.method == 'POST':
    submittedAnswer = request.form['submittedAnswer']
    answer = 'Answer'
    if submittedAnswer == answer:
      return render_template('Correct.html')
    else:
      return render_template('Incorrect.html', submittedAnswer = submittedAnswer)
  else:
    return '<h2>' + title + '</h2>'