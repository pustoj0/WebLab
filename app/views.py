from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.forms import RegistrationFrom, LoginForm
from app.models import User, Post


@app.route('/')
def index():
    return render_template('index.html', name='Інженерія програмного забезпечення', title='PNU')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        flash(f'Account created for {form.username.data}!', category='success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and bcrypt.check_password_hash(user.password_hash, str(form.password.data)):
            print('check passw success')
            flash('Logged in successfully.')
            return redirect(url_for('posts'))
        else:
            flash('Something goes wrong /check password/!')
    else:
        print('something goes wrong')
    return render_template('login.html', form=form, title='Login')


@app.route('/posts')
def posts():
    blog_post_list = Post.query.order_by("date_posted desc").all()
    return render_template('posts.html', title='Перелік постів',
                           posts=blog_post_list)
