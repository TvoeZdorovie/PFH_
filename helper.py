import requests
from dns import resolver 
  
def check_email(e_mail):

    pos = e_mail.find('@')
    if pos == 0 or pos == -1: 
        return False

    domen = e_mail[e_mail.find('@')+1:]
    
    b = 'http://'+ domen
    try:
        a = requests.get(b , timeout=3)
        if not a:
            #check MX
            answers = resolver.query(domain, 'MX')
            

        return True
    except BaseException:
        return False


