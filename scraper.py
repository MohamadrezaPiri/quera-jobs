import requests
from bs4 import BeautifulSoup
import smtplib
import re
import time

# URL = 'https://quera.org/magnet/jobs/rjmrq'
URL = 'https://quera.org/magnet/jobs?level=intern&level=junior'

headers={
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}



last_job=[]
print(last_job)
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

        server.login('piri8993@gmail.com', 'ehwnemuhychzjdwl')

        subject='New junior/intern job'
        body= f"A new junior/intern job has been defined: {new_job}"

        msg=f'Subject: {subject}\n\n{body}'

        server.sendmail('piri8993@gmail.com', 'piry.mreza@gmail.com', msg)
        print('Email has been sent')

        server.quit()


while True:
    recent_job=None
    # recent_mail=None
    # print(recent_job)
    # print(recent_mail)

    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,"html.parser")
    
    articles=soup.find_all("article")

    PYTHON_="python"  
    DJANGO="django"
    BACK_END="back-end"

    KEY_WORDS=[PYTHON_,DJANGO,BACK_END]

   

    for article in articles:
        job=article.text.lower()
        # print(PYTHON_ in job)
        # if PYTHON_ in job:
        #     print(f"https://quera.org/{article.h2.a['href']}")
        #     break
        for key_word in KEY_WORDS:
            # i=KEY_WORDS.index(key_word)
            if key_word in job:
                if not last_job or f"https://quera.org/{article.h2.a['href']}" != last_job[0]:
                    print(f"https://quera.org/{article.h2.a['href']}")
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
    # print(recent_job)        
    # print(recent_mail)        
    # print(recent_mail == recent_job)        
    if recent_job != None:
        print(recent_job)
        send_mail(recent_job)
    else:
        pass 
    time.sleep(10)  






































# last_job=[]
# def send_mail(new_job):
#         if not last_job:
#             last_job.append(new_job)
#         elif last_job[0] != new_job:
#             last_job.pop(0)
#             last_job.append(new_job)    
#         server=smtplib.SMTP('smtp.gmail.com',587)
#         server.ehlo()
#         server.starttls()
#         server.ehlo()

#         server.login('piry.mreza@gmail.com', 'wkypzytcsfcuavyw')

#         subject='New junior/intern job'
#         body= f"A new junior/intern job has been defined: {new_job[0]}"

#         msg=f'Subject: {subject}\n\n{body}'

#         server.sendmail('piry.mreza@gmail.com', 'thmydrda97@gmail.com', msg)
#         print('Email has been sent')

#         server.quit()



# while True:
#     recent_job=None
#     recent_mail=None
#     print(recent_job)
#     print(recent_mail)

#     page = requests.get(URL,headers=headers)

#     soup = BeautifulSoup(page.content,"html.parser")
    
#     articles=soup.find_all("article")

#     PYTHON_="python"  
#     DJANGO="django"
#     BACK_END="back-end"

#     KEY_WORDS=[PYTHON_,DJANGO,BACK_END]

   

#     for article in articles:
#         job=article.text.lower()
#         # print(PYTHON_ in job)
#         # if PYTHON_ in job:
#         #     print(f"https://quera.org/{article.h2.a['href']}")
#         #     break
#         for key_word in KEY_WORDS:
#             # i=KEY_WORDS.index(key_word)
#             if key_word in job:
#                 if f"https://quera.org/{article.h2.a['href']}" != recent_job:
#                     print(f"https://quera.org/{article.h2.a['href']}")
#                     recent_job =f"https://quera.org/{article.h2.a['href']}"
#                     break
#                 else:
#                     break
#             else:
#                 continue
#         if key_word not in job:
#             continue
#         else:
#             break    
#     print(recent_job)        
#     print(recent_mail)        
#     print(recent_mail == recent_job)        
#     if recent_mail != recent_job:
#         recent_mail = recent_job
#         send_mail(recent_mail)
#     else:
#         pass 
#     time.sleep(10)  


# while(True):    
#     job_title(recent_job, recent_mail)
#     time.sleep(10) 
