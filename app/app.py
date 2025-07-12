# app/app.py
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
messages = []

TEMPLATE = '''
<!doctype html>
<title>Message Board</title>
<h1>Leave a Message</h1>
<form method=post>
  <input name=message>
  <input type=submit value=Post>
</form>
<ul>
{% for msg in messages %}
  <li>{{ msg }}</li>
{% endfor %}
</ul>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        messages.append(request.form['message'])
        return redirect('/')
    return render_template_string(TEMPLATE, messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
