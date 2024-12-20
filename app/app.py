from flask import Flask, request, render_template, redirect, url_for, session, flash
import bcrypt
from models import db, User, CV, PersonalDetails, Employment, Education, Languages, Websites, Skills
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'portfolio_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Astghiksar1@localhost/portfoliogy_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'portfoliogy@gmail.com'
app.config['MAIL_PASSWORD'] = 'yfnntkrpyhxmlujn'

mail = Mail(app)
serializer = URLSafeTimedSerializer(app.secret_key)


db.init_app(app)

with app.app_context():
    db.create_all()
@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    from itsdangerous import URLSafeTimedSerializer, BadData

    try:
        serializer = URLSafeTimedSerializer(app.secret_key)
        email = serializer.loads(token, salt='password-reset-salt', max_age=3600)
    except BadData:
        flash('The reset link is invalid or has expired.', 'error')
        return redirect(url_for('forgot_password'))

    if request.method == 'POST':
        new_password = request.form.get('password')
        if not new_password:
            flash('Please enter a new password.', 'error')
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                user.password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
                db.session.commit()
                flash('Your password has been updated!', 'success')
                return redirect(url_for('login'))
            else:
                flash('User not found.', 'error')

    return render_template('reset_password.html', token=token)

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
            job_title = request.form.get('job_title')
            summary = request.form.get('summary')

            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            country = request.form.get('country')
            city = request.form.get('city')

            title_position = request.form.getlist('title_position')
            company = request.form.getlist('company')
            emp_start_date = request.form.getlist('emp_start_date')
            emp_end_date = request.form.getlist('emp_end_date')
            location = request.form.getlist('location')

            degree = request.form.getlist('degree')
            institution = request.form.getlist('institution')
            edu_start_date = request.form.getlist('edu_start_date')
            edu_end_date = request.form.getlist('edu_end_date')

            language = request.form.getlist('language')
            level = request.form.getlist('level')

            skill = request.form.getlist('skill')

            label = request.form.getlist('label')
            link = request.form.getlist('link')

            cv = CV(user_id=user_id, job_title=job_title, summary=summary)
            db.session.add(cv)
            db.session.flush() 

            if first_name and last_name and email:
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

            for i in range(len(language)):
                if language[i] and level[i]:
                    lang = Languages(
                        cv_id=cv.id,
                        language=language[i],
                        level=level[i]
                    )
                    db.session.add(lang)

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

@app.route('/showcase')
def showcase():
  
    if 'user_id' not in session:
        flash("Please log in to view the showcase.", "warning")
        return redirect(url_for('login'))

    user_id = session['user_id']

    try:
       
        user = User.query.get(user_id)
        if not user:
            flash("User not found. Please log in again.", "danger")
            return redirect(url_for('login'))

    
        cv = CV.query.filter_by(user_id=user_id).first()
        if not cv:
            flash("You don't have a CV yet. Please create one to view the showcase.", "warning")
            return redirect(url_for('create_cv'))

      
        personal_details = PersonalDetails.query.filter_by(cv_id=cv.id).first()
        employments = Employment.query.filter_by(cv_id=cv.id).all()
        education = Education.query.filter_by(cv_id=cv.id).all()
        languages = Languages.query.filter_by(cv_id=cv.id).all()
        websites = Websites.query.filter_by(cv_id=cv.id).all()

        
        return render_template('showcase.html',
                               user=user,
                               personal_details=personal_details,
                               employments=employments,
                               education=education,
                               languages=languages,
                               websites=websites,
                               job_title=cv.job_title,
                               summary=cv.summary)

    except Exception as e:
        print(f"Error occurred in showcase route: {e}")
        flash("An unexpected error occurred. Please try again.", "danger")
        return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/password')
def password():
    return render_template('password.html')

if __name__ == '__main__':
    app.run(debug=True),
