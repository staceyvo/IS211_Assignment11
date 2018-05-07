from flask import Flask

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


@app.route('/')
def display_tasks():
    task_table = '<html> <head> <title> Your Tasks </title> <body>'

    for task in to_do:
        task_table += '<p>{}, {}, {} </p>'.format(task['name'], task['email'], task['priority'])
    task_table += '</body> </html>'
    return task_table


if __name__ == '__main__':
    app.run()
