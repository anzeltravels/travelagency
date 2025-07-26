from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

SENDER_EMAIL = "anzeltravels@gmail.com"
SENDER_PASSWORD = "coxn qpxo cqyk zwxm"
RECEIVER_EMAIL = "anzeltravels@gmail.com"

@app.route('/')
def contact_form():
    return render_template("contact.html")

@app.route('/submit', methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    email_message = EmailMessage()
    email_message['Subject'] = f"New Contact Form Submission from {name}"
    email_message['From'] = SENDER_EMAIL
    email_message['To'] = RECEIVER_EMAIL
    email_message.set_content(f"""
    Name: {name}
    Email: {email}
    Message:
    {message}
    """)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(email_message)
        return "✅ Message sent successfully!"
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
