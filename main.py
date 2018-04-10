from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)

app.config['DEBUG'] = True   

@app.route("/")
def index():
    username = request.args.get('username')
    email = request.args.get('email')
    error1 = request.args.get('error1')
    error2 = request.args.get('error2')
    error3 = request.args.get('error3')
    error4 = request.args.get('error4')
    if username == None:
        return render_template('ushome.html')
    else:
        return render_template('ushome.html', username=username, email=email, error1=error1, error2=error2, error3=error3, error4=error4)


@app.route("/welcome", methods=['POST'])
def welcome():
    error1 = ''
    error2 = ''
    error3 = ''
    error4 = ''
    user = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = str(request.form['email'])
    validEmail = True
    emailCheck = False
    andCount = 0
    periodCount = 0
    emailError = ''
    if len(user) > 20 or len(user) < 3:
        error1 = 'Must be between 3 and 20 characters'
    if len(password) > 20 or len(password) < 3:
        error2 = 'Must be between 3 and 20 characters'
    if len(verify) > 20 or len(verify) < 3:
        error3 = 'Must be between 3 and 20 characters'
    if len(email) > 20 or len(email) < 3:
        error4 = 'Must be between 3 and 20 characters'
    if password != verify:
        error3 = "Passwords do not match!"
    if user == '':
        error1 = 'A username is required'
    if password == '':
        error2 = 'A valid password is required'
    if verify == '':
        error3 = 'Password verification is required'

    if len(email) > 0:
        while validEmail == True and emailCheck == False:
            for character in email:
                if character == ' ':
                    validEmail = False
                    emailError = 'Spaces not allowed'
                if character == '@':
                    andCount +=1
                    if andCount > 1:
                        validEmail = False
                        emailError = 'Multiple @ symbols not allowed'
                if character == '.':
                    periodCount += 1
                    if periodCount > 1:
                        validEmail = False
                        emailError = 'Multiple periods not allowed'
            if periodCount == 0:
                validEmail = False
                emailError = 'Period not found'
            if andCount == 0:
                validEmail = False
                emailError = 'The @ symbol is missing'            
            emailCheck = True
    if validEmail == False:
        error4 = emailError
    print(error1)
    print(error2)
    print(error3)
    print(error4)
    if error1 == '' and error2 == '' and error3 == '' and error4 == '':   
        return render_template('uswelcome.html', username=user)
    else:
        return redirect('/?' + 'username=' + user + '&email=' + email + '&error1=' + error1 + '&error2=' + error2 + '&error3=' + error3 + '&error4=' + error4)

app.run()