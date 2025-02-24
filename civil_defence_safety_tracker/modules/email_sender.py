import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(risk_id, risk_type, level, location, date):
    """
    Sends an email notification when a new risk is recorded.

    This function constructs an email message containing details about the recorded risk
    and sends it to a predefined recipient using SMTP and SSL encryption.

    Args:
        risk_id (int): The unique identifier of the recorded risk.
        risk_type (str): The type of risk (e.g., "Fire", "Flood").
        level (str): The severity level of the risk (e.g., "High", "Medium", "Low").
        location (str): The location where the risk occurred.
        date (str): The date of the recorded risk in YYYY-MM-DD format.

    Returns:
        None

    Example:
        send_email(101, "Fire", "High", "Jeddah", "2024-02-25")
        # Sends an email alert about the recorded fire risk.
    """
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
