#!/usr/bin/env python
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
        #html form
          return '''
            <form method="post">
                First number: <input type="text" name="A" />
                Second number: <input type="text" name="B" />
                <p><input type="submit" name="operator" value="Subtract" />
	    </form>
        '''
	elif request.method == 'POST':
         a = request.form.get('operator')
         if a == 'Subtract':
            A = request.form.get('A')
            B = request.form.get('B')
            return redirect(url_for('sub', A=A, B=B))

@app.route('/sub')
def sub():
    dict = request.args.to_dict()
    A = eval(dict['A'])
    B = eval(dict['B'])
    result = A-B
    return 'Result is: %s' % result


if __name__ == '__main__':
    app.run(debug=True)
