import smtplib
from email.message import EmailMessage
from datetime import datetime
import time
from pathlib import Path

dateAndTime = datetime.now().strftime("%Y-%m-%d_%H:%M")

time.sleep(10)

sender = "root820429@gmail.com"
receiver = "tomas.bicik@silektro.cz"
password = "eivycyfjumdrtidv"

msg = EmailMessage()
msg["Subject"] = "Export namerenych dat"
msg["From"] = sender
msg["To"] = receiver
msg.set_content("Export namerenych dat. Datum a cas vygenerovani souboru viz. nazev souboru. ")

fileToSend = Path(f"/home/sysadmin/OTE/XMLfiles/export_{dateAndTime}.xml") # opravit nazev a cestu
fileName = f"export_{dateAndTime}.xml"

with open(fileToSend, "rb") as f:
    content = f.read()
    msg.add_attachment(content, maintype="application", subtype="xml", filename=fileName)
    
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)