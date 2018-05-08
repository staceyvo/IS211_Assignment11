from flask import Flask, render_template
from wtforms import Form, validators, StringField, SelectField

app = Flask(__name__)


to_do = [
    {'name': 'order supplies',
     'email': 'stacey@me.com',
     'priority': 'medium'
     },
    {'name': 'feed the cat',
     'email': 'chris@you.com',
     'priority': 'high'
     },
    {'name': 'water the plants',
     'email': 'juan@juan.net',
     'priority': 'low'
     }
]

class CreateTaskForm(Form):
    task = StringField(u'Task', [validators.required(), validators.length(max=200)])
    email = StringField(u'Email Address', [validators.required(), validators.length(max=200)])
    priority = SelectField(u'Priority', choices=[('low','low'), ('medium', 'medium'), ('high', 'high')], validators=[validators.required()])


@app.route('/')
def to_do_tasks():
    return render_template('task_template.html', data=to_do, my_form=CreateTaskForm())

@app.route('/old')
def display_tasks():
    task_table = '<html> <head> <title> Your Tasks </title> <body>'

    for task in to_do:
        task_table += '<p>{}, {}, {} </p>'.format(task['name'], task['email'], task['priority'])
    task_table += '</body> </html>'
    return task_table


if __name__ == '__main__':
    app.run()
