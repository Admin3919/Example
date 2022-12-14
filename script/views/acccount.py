from flask import blueprints, render_template, request, current_app, redirect
from script import db, models

ac = blueprints.Blueprint('ac',__name__)

@ac.route('/login',methods=['GET','POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')

        obj = db.session.query(models.Users).filter(models.Users.name==user, models.Users.pwd==pwd).first()
        db.session.remove()
        if not obj:
            return render_template('login.html',msg="users or password error")

        current_app.auth_manager.login(user)
        return redirect('/index')

@ac.route('/logout')
def logout():
        current_app.auth_manager.logout()
        return redirect('/login')




