# todo:
# checar questão de encriptar o token

from collections import defaultdict
from urllib.parse import urlparse

def organize_contacts_by_domain(data):
    organized_contacts = defaultdict(list)
    
    for contact in data.get("connections", []):
        emails = contact.get("emailAddresses", [])
        names = contact.get("names", [])
        
        if emails and names:
            email = emails[0]["value"]
            name = names[0]["displayName"]
            domain = email.split("@")[1]  # Extrai o domínio do e-mail
            organized_contacts[domain].append({"name": name, "email": email})
    
    return dict(organized_contacts)
