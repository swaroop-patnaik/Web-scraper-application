import pyshorteners

#org_url = input("Enter url ->") 

def shortener(org_url):
    us = pyshorteners.Shortener()
    return us.tinyurl.short(org_url)

#print(shortener(org_url))
