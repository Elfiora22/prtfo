from flask import Flask
'''import for show_user_profile  function  line 17'''
from markupsafe import escape 
'''import for testing URL'''
from flask import url_for
'''import for template rendering'''
from flask import render_template
'''import for request test, request qbject'''
from flask import request, redirect
'''for crezting the csv file'''
import csv


app = Flask(__name__)
'_____________Конспект_____________________'
'''
@app.route("/")
def index():
    return "<h1>O, Мир!</h1>"
'''
#@app.route('/hello')
#def hello():
    #return "<h4>привееt</h4>"

'''Variable section of URL passed to the function

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'
'''


'''Test URL endpoints
@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

Output of the test_request_context function 
/
/login
/login?next=/
/user/John%20Doe
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
'''

'''Test Request

now you can do something with the request until the
end of the with block, such as basic assertions:
with app.test_request_context('/hello', method='Post'):
    assert request.path == '/hello'
    assert request.method == 'POST'
'''    



'''Template Rendering
@app.route('/hello/')
@app.route('/hello/<name>/<int:post_id>')
def hello2(name=None, post_id=None):
    return render_template('index.html', name=name, post_id=post_id)
'''
'''__________________________________________  
Using Space template fom now''' 

'''main page - космонавт'''
@app.route('/')
def my_homepage():
    return render_template('index.html')

'''function dealing with the navbar'''
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')
        
        
def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        return csv_writer.writerow([email, subject, message])


'''function dealing with submit, redirect, write to the file '''
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
        except:
            return "did not post to database"
        return  redirect('thankyou.html')
    else:
        return 'somethong went wrong'

   



