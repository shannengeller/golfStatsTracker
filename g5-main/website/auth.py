#import statements 
from flask import Blueprint, render_template, request, flash, redirect, url_for
from website.views import home
from .models import User, Holes, Player
from sqlalchemy.sql.schema import ForeignKeyConstraint , UniqueConstraint
from werkzeug.security import generate_password_hash, check_password_hash # storing a password as hash
from . import db
from flask_login import login_required, login_user, logout_user, current_user

auth = Blueprint('auth', __name__)

# this function controls the login page 
@auth.route('/login', methods = ['GET', 'POST'])
def login(): 
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # here we search through the database of users
        user = User.query.filter_by(email=email).first()

        if user: 
            # if inputter email and password are correct, show message and send to home page
            if check_password_hash(user.password, password):
                flash('Logged In Successfully!', category ='success')
                login_user(user, remember= True)
                return redirect(url_for('views.home'))
            else:
                # if password is incorrect prompt try again message 
                flash('Incorrect password, try again.', category='error')
        else:
            # if email does not exists, prompt error 
            flash('Email does not exist', category='error')

    return render_template("login.html", user= current_user)

# this function controls the logout feature, returning the user to the login page
@auth.route('/logout')
@login_required
def logout(): 
    logout_user()
    return redirect(url_for('auth.login'))

# this function controls the player stats button feature on the home page, redirecting the user once clicked on
@auth.route('/pstats')
def playerstats(): 
    return render_template("PlayerStats.html", user = current_user)

# this function controls the team stats button feature on the home page, redirecting the user once clicked on
@auth.route('/tstats')
def teamstats(): 
    return render_template("TeamStats.html", user = current_user)

# this function controls the stats entry button feature on the home page, redirecting the user once clicked on
@auth.route('/statsE', methods = ['GET', 'POST'])
def statsentry():
    if request.method == 'POST':
        # the inputter/requested information
        pname = request.form.get('Playername')
        cousren= request.form.get('Cousrsename')
        dates = request.form.get('Date') 

        allpars = request.form.get('Par') 
        allscores = request.form.get('Score')
        allfairways = request.form.get('Fairway')
        allgirs = request.form.get('Gir')
        allapproachds = request.form.get('ApproachD')
        alluds = request.form.get('UpDown')
        allsuds = request.form.get('SandUpDown')
        allputts = request.form.get('putts')
        allp2hs = request.form.get('p2h')

        # allpars = request.form.get(['Par','Par2','Par3','Par4','Par5','Par6','Par7','Par8','Par9','Par10','Par11','Par12','Par13','Par14','Par15','Par16','Par17','Par18']) 
        # allscores = request.form.get(['Score','Score2','Score3','Score4','Score5','Score6','Score7','Score8','Score9','Score10','Score11','Score12','Score13','Score14','Score15','Score16','Score17','Score18'])
        # allfairways = request.form.get(['Fairway','Fairway2','Fairway3','Fairway4','Fairway5','Fairway6','Fairway7','Fairway8','Fairway9','Fairway10','Fairway11','Fairway12','Fairway13','Fairway14','Fairway15','Fairway16','Fairway17','Fairway18'])
        # allgirs = request.form.get(['Gir','Gir2','Gir3','Gir4','Gir5','Gir6','Gir7','Gir8','Gir9','Gir10','Gir11','Gir12','Gir13','Gir14','Gir15','Gir16','Gir17','Gir18'])
        # allapproachds = request.form.get(['ApproachD','ApproachD2','ApproachD3','ApproachD4','ApproachD5','ApproachD6','ApproachD7','ApproachD8','ApproachD9','ApproachD10','ApproachD11','ApproachD12','ApproachD13','ApproachD14','ApproachD15','ApproachD16','ApproachD17','ApproachD18'])
        # alluds = request.form.get(['UpDown','UpDown2','UpDown3','UpDown4','UpDown5','UpDown6','UpDown7','UpDown8','UpDown9','UpDown10','UpDown11','UpDown12','UpDown13','UpDown14','UpDown15','UpDown16','UpDown17','UpDown18'])
        # allsuds = request.form.get(['SandUpDown','SandUpDown2','SandUpDown3','SandUpDown4','SandUpDown5','SandUpDown6','SandUpDown7','SandUpDown8','SandUpDown9','SandUpDown10','SandUpDown11','SandUpDown12','SandUpDown13','SandUpDown14','SandUpDown15','SandUpDown16','SandUpDown17','SandUpDown18'])
        # allputts = request.form.get(['putts','putts2','putts3','putts4','putts5','putts6','putts7','putts8','putts9','putts10','putts11','putts12','putts13','putts14','putts15','putts16','putts17','putts18'])    #     # allp2hs = request.form.get(['p2h','p2h2','p2h3','p2h4','p2h5','p2h6','p2h7','p2h8','p2h9','p2h10','p2h11','p2h12','p2h13','p2h14','p2h15','p2h16','p2h17','p2h18'])

        newplayer = Player(player_id = current_user.id, name = pname, coursename = cousren, date = dates)
        db.session.add(newplayer)
        Player.insert().prefix_with('IGNORE').values([...])
            
        # newholes = Holes(holes_id = newplayer.player_id, pars = allpars, scores = allscores, fairways = allfairways, girs = allgirs, approachds = allapproachds, uds = alluds, suds = allsuds, putts = allputts, p2hs = allp2hs)
        # db.session.add(newholes)
        
        db.session.commit()


        # for i in ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']:
        #     allpars = request.form.get('Par' + i) 
        #     allscores = request.form.get('Score' + i)
        #     allfairways = request.form.get('Fairway' + i)
        #     allgirs = request.form.get('Gir' + i)
        #     allapproachds = request.form.get('ApproachD' + i)
        #     alluds = request.form.get('UpDown' + i)
        #     allsuds = request.form.get('SandUpDown' + i)
        #     allputts = request.form.get('putts' + i)
        #     allp2hs = request.form.get('p2h' + i)
        #     newholes = Holes(holes_id = newplayer.player_id, pars = allpars, scores = allscores, fairways = allfairways, girs = allgirs, approachds = allapproachds, uds = alluds, suds = allsuds, putts = allputts, p2hs = allp2hs)
        #     db.session.add(newholes)
        #     db.session.commit()

        flash('Player Created.', category='success')
        return render_template("PlayerStats.html", user = current_user) 
    
    # db.session.query(Player).delete()
    # db.session.commit() 
    return render_template("StatEntry.html", user = current_user)

# this function controls the sign up feature for new users
@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up(): 
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')  
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        # here holds the case errors and prompts if there is an issue creating the account
        if user: 
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('Email must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('password must be at least 7 characters.', category='error')
        # if user does not exist in database & new account is created successfully -> prompt is given and user redirected to home
        else:
            new_user = User(email = email, first_name = first_name , password = generate_password_hash(password1, method = 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('Account Created.', category='success')
            return redirect(url_for('views.home'))

            #add user to database
    return render_template("sign_up.html", user = current_user)


