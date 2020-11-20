import os
from datetime import date
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
  if request.environ['HTTP_HOST'].endswith('.appspot.com'):  #Redirect the appspot url to the custom url
    return '<meta http-equiv="refresh" content="0; url=https://swahilicheatsheet.com" />'
  else:
    template_values = {
      'page_title' : "Swahili Cheat Sheet",
      'current_year' : date.today().year,
    }
    return render_template('home.html', **template_values)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)