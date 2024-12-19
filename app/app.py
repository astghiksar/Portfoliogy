from flask import Flask, request, render_template, redirect, url_for, session, flash
import bcrypt
from datetime import datetime
from models import db, User, CV, PersonalDetails, Employment, Education, Languages, Websites, Skills

app = Flask(__name__)
app.secret_key = 'portfolio_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://arpi:userarpi@localhost/portfoliogy_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    full_name = request.form.get('full_name')
    email = request.form.get('email')
    password = request.form.get('password')

    if not full_name or not email or not password:
        flash('Please fill in all fields.', 'error')
        return redirect(url_for('signup'))
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    try:
        new_user = User(full_name=full_name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Thank you for signing up, {full_name}!', 'success')
        return redirect(url_for('login'))
    except Exception as e:
        print(e)
        flash('An error occurred while signing up.', 'error')
        return redirect(url_for('signup'))

@app.route('/login')
def login_page():
    return render_template('login.html')
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()

    if user:
        if bcrypt.checkpw(password.encode(), user.password.encode()):
            session['user_id'] = user.id
            session['full_name'] = user.full_name
            flash(f'Welcome back, {user.full_name}!', 'success')
            return redirect(url_for('home'))
        else:
            flash("Invalid password. Please try again.", 'error')
            return redirect(url_for('login'))
    else:
        flash("User not found. Please sign up first.", 'error')
        return redirect(url_for('login'))

@app.route('/view_template')
def view_template():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('create_cv', full_name=session['full_name']))
@app.route('/')
def default():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    if 'full_name' in session:
        full_name = session['full_name']
        return render_template('home.html', full_name=full_name)
    return render_template('home.html')

@app.route('/create')
def create():
    if 'full_name' in session:
        full_name = session['full_name']
        return render_template('create.html', full_name=full_name)
    return render_template('create.html')

@app.route('/search')
def search():
    if 'full_name' in session:
        full_name = session['full_name']
        return render_template('search.html', full_name=full_name)
    return render_template('search.html')

@app.route('/template')
def template():
    if 'full_name' in session:
        full_name = session['full_name']
        return render_template('template.html', full_name=full_name)
    return render_template('template.html')

@app.route('/create2', methods=['GET', 'POST'])
def create_cv():
    if 'user_id' not in session:
        flash('You need to log in to create a CV.', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        user_id = session['user_id']
        user = User.query.get(user_id)
        if not user:
            flash('User not found.', 'error')
            return redirect(url_for('login'))

        try:
            # General CV fields
            job_title = request.form.get('job_title')
            summary = request.form.get('summary')

            # Personal Details
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            country = request.form.get('country')
            city = request.form.get('city')

            # Employment history
            title_position = request.form.getlist('title_position')
            company = request.form.getlist('company')
            emp_start_date = request.form.getlist('emp_start_date')
            emp_end_date = request.form.getlist('emp_end_date')
            location = request.form.getlist('location')

            # Education history
            degree = request.form.getlist('degree')
            institution = request.form.getlist('institution')
            edu_start_date = request.form.getlist('edu_start_date')
            edu_end_date = request.form.getlist('edu_end_date')

            # Languages
            language = request.form.getlist('language')
            level = request.form.getlist('level')

            skill = request.form.getlist('skill')

            # Websites
            label = request.form.getlist('label')
            link = request.form.getlist('link')

            # Create CV record
            cv = CV(user_id=user_id, job_title=job_title, summary=summary)
            db.session.add(cv)
            db.session.flush()  # To get CV ID immediately

            # Personal Details
            if first_name and last_name and email:  # Required fields check
                personal_details = PersonalDetails(
                    cv_id=cv.id,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    country=country,
                    city=city
                )
                db.session.add(personal_details)

            # Employment
            for i in range(len(title_position)):
                if title_position[i] and company[i]:
                    employment = Employment(
                        cv_id=cv.id,
                        title=title_position[i],
                        company=company[i],
                        start_date=datetime.strptime(emp_start_date[i], '%Y-%m-%d') if emp_start_date[i] else None,
                        end_date=datetime.strptime(emp_end_date[i], '%Y-%m-%d') if emp_end_date[i] else None,
                        location=location[i]
                    )
                    db.session.add(employment)

            # Education
            for i in range(len(degree)):
                if degree[i] and institution[i]:
                    education = Education(
                        cv_id=cv.id,
                        degree=degree[i],
                        institution=institution[i],
                        start_date=datetime.strptime(edu_start_date[i], '%Y-%m-%d') if edu_start_date[i] else None,
                        end_date=datetime.strptime(edu_end_date[i], '%Y-%m-%d') if edu_end_date[i] else None
                    )
                    db.session.add(education)

            # Languages
            for i in range(len(language)):
                if language[i] and level[i]:
                    lang = Languages(
                        cv_id=cv.id,
                        language=language[i],
                        level=level[i]
                    )
                    db.session.add(lang)

            # Websites
            for i in range(len(label)):
                if label[i] and link[i]:
                    website = Websites(cv_id=cv.id, label=label[i], url=link[i])
                    db.session.add(website)

            db.session.commit()
            flash('CV created successfully!', 'success')
            return redirect(url_for('home'))

        except Exception as e:
            db.session.rollback()
            print(f"Error: {e}")
            flash('An error occurred while creating your CV. Please try again.', 'error')
            return redirect(url_for('create2'))
    return render_template('create2.html')



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')

if __name__ == '__main__':
    app.run(debug=True),

