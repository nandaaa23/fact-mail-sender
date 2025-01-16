import yagmail
from yagmail.sender import SMTP
import os
import time
from datetime import datetime as dt
import requests
import json

sender = 'sender_mail@gmail.com'
receiver = 'receiver_mail@gmail.com'

while True:
  now = dt.now()
  if now.hour == 10 and now.minute == 36:
    
    # URL from where we will fetch the data
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    # Use GET request
    response = requests.get(url)

    # Load the request in json file
    data = json.loads(response.text)
    
    # We will need 'text' from the data
    useless_fact = data['text']

    subject = "This is the subject!"
    contents = """
    Good morning.
    DID YOU KNOW?\n
    """,useless_fact
    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
    time.sleep(60)