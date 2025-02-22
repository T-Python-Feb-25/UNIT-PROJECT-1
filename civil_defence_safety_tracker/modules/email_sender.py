import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(risk_id, risk_type, level, location, date):
    sender_email = "joojgamah@gmail.com"  
    sender_password = "xnzy dvrj nnkv lmca"  
    recipient_email = "wjdanalbdalzyz@gmail.com"  

    subject = f"⚠️ Alert: New Risk Recorded - {level.upper()}"
    body = f"""
    A new risk has been recorded in the system:

    🆔 ID: {risk_id}
    ⚠️ Type: {risk_type}
    🔥 Level: {level}
    📍 Location: {location}
    🗓️ Date: {date}

    Please take the necessary actions.
    """

    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

   
   
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        print("✅ Email sent successfully!")
        return "Success"
    except Exception as e:
        print(f"❌ Email sending failed: {e}")
        return "Failed"
