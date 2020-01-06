from flask import Flask, request, redirect, url_for

# create app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        #html form
        return '''
            <form method="post">
                First number: <input type="text" name="A" />
                Second number: <input type="text" name="B" />
                <p><input type="submit" name="operator" value="Add" />
                <input type="submit" name="operator" value="Subtract" />
                <input type="submit" name="operator" value="Multiply" />
                <input type="submit" name="operator" value="Divide" />
            </form>
        '''
    elif request.method == 'POST':
        a = request.form.get('operator')
        if a == 'Add':
            A = request.form.get('A')
            B = request.form.get('B')
            return redirect(url_for('add', A=A, B=B))

        if a == 'Subtract':
            A = request.form.get('A')
            B = request.form.get('B')
            return redirect(url_for('sub', A=A, B=B))

        if a == 'Multiply':
            A = request.form.get('A')
            B = request.form.get('B')
            return redirect(url_for('mul', A=A, B=B))

        if a == 'Divide':
            A = request.form.get('A')
            B = request.form.get('B')
            return redirect(url_for('div', A=A, B=B))

@app.route('/add')
def add():
    dict = request.args.to_dict()
    A = eval(dict['A'])
    B = eval(dict['B'])
    result = A+B
    return 'Result is: %s' % result

@app.route('/sub')
def sub():
   dict = request.args.to_dict()
   A = eval(dict['A'])
   B = eval(dict['B'])
   result = A-B
   return 'Result is: %s' % result

@app.route('/mul')
def mul():
    dict = request.args.to_dict()
    A = eval(dict['A'])
    B = eval(dict['B'])
    result = A*B
    return 'Result is: %s' % result

@app.route('/div')
def div():
    dict = request.args.to_dict()
    A = eval(dict['A'])
    B = eval(dict['B'])
    result = A/B

    return 'Result is: %s' % result


# run app
if __name__ == '__main__':
    app.run(debug=True)
