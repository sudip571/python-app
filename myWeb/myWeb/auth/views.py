
# third part Import

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

# Local import
from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import Employee



@auth.route('/register', methods=['GET','POST'])
def register():
    """
    Handle requestes to the /register route
    Add an employee to the database through the registration form
    """

    form=RegistrationForm()

    if form.validate_on_submit():

      #employee = Employee()
      #employee.email= form.email.data,
      #employee.username = form.username.data,      
      # or 
      employee = Employee(
          email= form.email.data,
          username= form.username.data,
          first_name= form.first_name.data,
          last_name= form.last_name.data,
          password= form.password.data
          )

      # add employee to database

      db.session.add(employee)
      db.session.commit()
      flash('You have successfully regstered. You may now login')

      # redirect to the Login Page
      # instead of auth.login we can write .login only
      # Here . refers to current blueprint

      return redirect(url_for('auth.login'))

    # if validation fails,return again to Registration page

    return render_template('auth/register.html',form=form,title='Register')

@auth.route('/login', methods=['GET','POST'])
def login():
    """
    handle the request to /login route
    Log an employee in through login form
    """
    form=LoginForm()

    if form.validate_on_submit():
        # check if user exist on database
        #check if the entered password is correct
        employee=Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(form.password.data):
            # log user in
            login_user(employee)
            # redirect user to appropriate dashboard
            if employee.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))
            
    

        # credential are wrong
        else:
            flash('Invalid Email or Password')

    # if form form validation fails, load login template again
    return render_template('auth/login.html',form=form,title="Login")

@auth.route('/logout')
def logout():
    """
    handle request to /logout route
    Log an user out 
    """
    logout_user()
    flash('You have successfully been logged out')

    # redirect to login page
    return redirect(url_for('auth.login'))
   

        


 
            
           
