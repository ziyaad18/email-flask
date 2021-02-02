import smtplib
from flask import Flask, render_template, request
from email.mime.text import MIMEText


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('portfolio.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/send-email/', methods=["POST", "GET"])
def send_email():

    try:
        subject = request.form['subject']
        email = request.form['email']
        message = MIMEText(request.form['message'])
        message['Subject'] = subject
        message['From'] = email
        message['To'] = email

        server = smtplib.SMTP('smtp.gmail.com', 465)
        sender_email = email
        receiver_email = "ziyaadpetersen347@gmail.com"
        password = "Petersenboss15"

        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
    except smtplib.SMTPException as e:
        return "Something wrong happened: " + e
    return render_template('email-success.html')

if __name__== "__main__":
    app.run(debug=True)
