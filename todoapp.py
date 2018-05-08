from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, validators, StringField, SelectField

app = Flask(__name__)

to_do = []


class CreateTaskForm(Form):
    task = StringField(u'Task', [validators.required(), validators.length(max=200)])
    email = StringField(u'Email Address', [validators.required(), validators.length(max=200)])
    priority = SelectField(u'Priority', choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')],
                           validators=[validators.required()])

@app.route('/clear')
def clear_list():
    del to_do[:]
    return redirect(url_for('display_tasks'))



@app.route('/submit', methods=['POST', 'GET'])
def to_do_tasks():
    if request.method == 'POST':
        if CreateTaskForm(request.form).validate():
            task2 = {
                'task': request.form['task'],
                'email': request.form['email'],
                'priority': request.form['priority']
            }
            to_do.append(task2)
        return redirect(url_for('display_tasks'))
    return render_template('to_do_template.html', data=to_do, my_form=CreateTaskForm())



@app.route('/')
def display_tasks():
    return render_template('task_template.html', data=to_do)


if __name__ == '__main__':
    app.run()
