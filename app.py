from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):

    grade = 0
    num = False
    capital = False
    special = False
    length = False
    letters = False

    if len(password) >= 8:
        length = True
        grade += 1

    for char in password:
        if char.isdigit():
            num = True
        elif char.isalpha():
            letters = True
            if char.isupper():
                capital = True
        elif not char.isalnum():
            special = True

    if num:
        grade += 1
    if letters:
        grade += 1
    if capital:
        grade += 1
    if special:
        grade += 1

    if grade == 5:
        return "Strong Password"
    elif grade >= 3:
        return "Normal Password"
    else:
        return "Weak Password"

@app.route('/home')
def home_page():
    return render_template("home.html")

@app.route('/')
def main_home():
    return render_template("home.html")

@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        password = request.form['password']
        result = check_password_strength(password)
        return render_template("index.html", strength=result)

    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)