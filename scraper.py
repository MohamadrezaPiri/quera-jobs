import requests
from bs4 import BeautifulSoup
import smtplib
import re
import time


URL = 'https://quera.org/magnet/jobs?level=intern&level=junior'

headers={
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}



last_job=[]
# print(last_job)
def send_mail(new_job):
        if not last_job:
            last_job.append(new_job)
        elif last_job[0] != new_job:
            last_job.pop(0)
            last_job.append(new_job)    
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('sender@gmail.com', 'bezieujszsqloltf')

        subject='New junior/intern job'
        body= f"A new junior/intern job has been defined: {new_job}"

        msg=f'Subject: {subject}\n\n{body}'

        server.sendmail('sender@gmail.com', 'reciever@gmail.com', msg)
        print('Email has been sent')

        server.quit()


while True:
    recent_job=None
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,"html.parser")
    articles=soup.find_all("article")

    python_="python"  
    django="django"
    back_end="back-end"

    key_words=[python_,django,back_end]

    for article in articles:
        job=article.text.lower()
        
        for key_word in key_words:
            if key_word in job:
                if not last_job or f"https://quera.org/{article.h2.a['href']}" != last_job[0]:
                    recent_job =f"https://quera.org/{article.h2.a['href']}"
                    break
                else:
                    break
            else:
                continue
        if key_word not in job:
            continue
        else:
            break    
    
    if recent_job != None:
        print(recent_job)
        send_mail(recent_job)
    else:
        pass 
    time.sleep(1800)  






































