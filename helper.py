import requests
from whois import whois
  
def check_email(e_mail):
    domen = e_mail[e_mail.find('@')+1:]
    b = 'http://'+ domen
    try:
        a = requests.get(b , timeout=5)
        if not a:
            whois(b)
            return True

        return True
    except BaseException:
        return False

