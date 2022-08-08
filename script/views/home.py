from flask import blueprints, render_template

hm = blueprints.Blueprint('hm',__name__)

@hm.route('/index')
def index():

    return render_template('index.html')