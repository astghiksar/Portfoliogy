# from flask import Flask, request, jsonify, render_template, redirect, url_for
# import bcrypt
# import psycopg2
#
# # Initialize Flask app
# app = Flask(__name__)
#
# # Database connection setup (replace with your own connection details)
# conn = psycopg2.connect(
#     dbname="portfoliogy_db",  # Replace with your database name
#     user="arpi",             # Replace with your PostgreSQL username
#     password="userarpi",     # Replace with your PostgreSQL password
#     host="localhost",             # Replace with your PostgreSQL host (localhost if local)
#     port="5432"                   # Default PostgreSQL port
# )
# cursor = conn.cursor()
#
# @app.route('/signup')
# def signup_page():
#     return render_template('signup.html')
# @app.route('/signup', methods=['POST'])
# def signup():
#     full_name = request.form.get('full_name')
#     email = request.form.get('email')
#     password = request.form.get('password')
#
#     if not full_name or not email or not password:
#         return 'Please fill in all fields.', 400
#
#     # Hash the password
#     hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
#
#     # Insert into the database
#     try:
#         cur = conn.cursor()
#         cur.execute("""
#             INSERT INTO users (full_name, email, password)
#             VALUES (%s, %s, %s)
#         """, (full_name, email, hashed_password))
#         conn.commit()
#         cur.close()
#         return f'Thank you for signing up, {full_name}!', 200
#     except Exception as e:
#         print(e)
#         return 'An error occurred while signing up.', 500
#
#
#
# @app.route('/')
# def default():
#     return redirect(url_for('home'))
#
# @app.route('/home')
# def home():
#     return render_template('home.html')
#
# @app.route('/create')
# def create():
#     return render_template('create.html')
#
# @app.route('/search')
# def search():
#     return render_template('search.html')
#
# @app.route('/template')
# def template():
#     return render_template('template.html')
#
# @app.route('/create2')
# def create2():
#     return render_template('create2.html')
# @app.route('/login')
# def login_page():
#     return render_template('login.html')
#
#
# @app.route('/login', methods=['POST'])
# def login():
#     # Get form data (username and password)
#     username = request.form['username']
#     password = request.form['password']
#
#     # Fetch the stored hashed password from the database
#     cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
#     stored_hashed_password = cursor.fetchone()
#
#     if stored_hashed_password:
#         # Compare the entered password with the stored hashed password
#         if bcrypt.checkpw(password.encode(), stored_hashed_password[0].encode()):
#             return jsonify({"message": "Login successful!"}), 200
#         else:
#             return jsonify({"message": "Invalid password!"}), 400
#     else:
#         return jsonify({"message": "User not found!"}), 404
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import bcrypt
import psycopg2

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'portfolio_key'

# Database connection setup (replace with your own connection details)
conn = psycopg2.connect(
    dbname="portfoliogy_db",  # Replace with your database name
    user="arpi",             # Replace with your PostgreSQL username
    password="userarpi",     # Replace with your PostgreSQL password
    host="localhost",        # Replace with your PostgreSQL host (localhost if local)
    port="5432"              # Default PostgreSQL port
)
cursor = conn.cursor()



@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    full_name = request.form.get('full_name')
    email = request.form.get('email')
    password = request.form.get('password')

    if not full_name or not email or not password:
        return 'Please fill in all fields.', 400

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    # Insert into the database
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO users (full_name, email, password)
            VALUES (%s, %s, %s)
        """, (full_name, email, hashed_password))
        conn.commit()
        cur.close()
        return render_template('signup.html', message=f'Thank you for signing up, {full_name}!')
    except Exception as e:
        print(e)
        return 'An error occurred while signing up.', 500

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    cursor.execute("SELECT id, full_name, password FROM users WHERE email = %s", (email,))
    stored_user = cursor.fetchone()

    if stored_user:
        stored_hashed_password = stored_user[2]
        if bcrypt.checkpw(password.encode(), stored_hashed_password.encode()):
            # Store user details in the session
            session['user_id'] = stored_user[0]
            session['full_name'] = stored_user[1]
            return redirect(url_for('home'))
        else:
            return jsonify({"message": "Invalid password!"}), 400
    else:
        return jsonify({"message": "User not found!"}), 404


@app.route('/')
def default():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    if 'full_name' in session:  # Check if user is logged in
        full_name = session['full_name']
        return render_template('home.html', full_name=full_name)
    return render_template('home.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/template')
def template():
    return render_template('template.html')

@app.route('/create2')
def create2():
    return render_template('create2.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
