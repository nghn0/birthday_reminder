import datetime
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Date, Integer
from flask_bootstrap import Bootstrap5
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading


# Base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dates.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)
Bootstrap5(app)


# Database model for storing dates
class Bdates(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False)


# Form for adding dates
class Add(FlaskForm):
    name = StringField("Name")
    bdate = DateField("Date", validators=[DataRequired()])
    add = SubmitField("Add Date")


# Function to send an email in a thread
def send_mail(names):
    def email_task(names):
        l = ", ".join(i[0].name for i in names)
        sender_email = "nithish1053015@gmail.com"
        receiver_email = "nithish1053015@gmail.com"  # Send email to yourself
        app_password = "vpll aaye ctjf shom"

        subject = "Birthday Reminder"
        body = f"Today's birthdays: {l}. Don't forget to wish them!"

        # Create the email content
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, app_password)
                server.send_message(message)
                print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")

    # Start the email-sending task in a new thread
    email_thread = threading.Thread(target=email_task, args=(names,))
    email_thread.start()


# Home route
@app.route('/', methods=['POST', 'GET'])
def home():
    form = Add()
    current_date = datetime.date.today()  # Ensure it's a date object, not a string

    with app.app_context():
        db.create_all()  # Ensure the database and table exist
        # Query for today's birthdays
        d = db.session.execute(db.select(Bdates).where(Bdates.date == current_date)).fetchall()

        # Only send email if there are birthdays today
        if d:
            send_mail(d)

        if form.validate_on_submit():
            # Save form data to the database
            info = Bdates(
                name=form.name.data,
                date=form.bdate.data
            )
            db.session.add(info)
            db.session.commit()
            return redirect(url_for('home'))

        return render_template("index.html", form=form, added=False, names=d)


if __name__ == "__main__":
    app.run(debug=True)
