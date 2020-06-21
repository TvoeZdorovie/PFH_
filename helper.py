import requests
from dns import resolver 
  
def check_email(e_mail):

    pos = e_mail.find('@')
    if pos == 0 or pos == -1: 
        return False

    domen = e_mail[e_mail.find('@')+1:]
    try:
        #check MX
        answers = resolver.query(domen, 'MX')
        for i in answers:
            print(i)
        return True

    except BaseException:
        return False


