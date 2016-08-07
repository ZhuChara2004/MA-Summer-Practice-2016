from test_prof.app.api.__init__ import app
from flask import render_template, request, make_response, redirect
from test_prof.app.api.admin import auth, equals
import datetime


@app.route('/', methods=['GET'])
def get_tests():
    return render_template('test_index.html')


@app.route('/<id>', methods=['GET'])
def test(id):
    return render_template("test.html", id=id)


@app.route('/login', methods=['GET', 'POST'])
def get_user():
    if request.method == 'GET':
        if equals(request.cookies.get('business_c_token')):
            return render_template('admin.html')
        else:
            return render_template('login.html')
    elif request.method == 'POST':
        token = auth(request.form['login'], request.form['password'])
        if token:
            expire_date = datetime.datetime.now()
            expire_date = expire_date + datetime.timedelta(days=365)
            resp = make_response(redirect('/login'))
            resp.set_cookie('business_c_token', value=token, expires=expire_date)
            return resp
        else:
            return render_template('login.html', mesg='error validation')


@app.route("/logout", methods=['GET'])
def logout():
    resp = make_response(redirect('/login'))
    resp.set_cookie('business_c_token', '', expires=0)
    return resp


@app.route('/new_test', methods=['GET'])
def new_test():
    return render_template('new_test.html')

if __name__ == '__main__':
    app.run(debug=True)
