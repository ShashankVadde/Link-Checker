import urllib.request

link = 'https://google.com'

def connect():
    try:
        urllib.request.urlopen(link)
        return True
    
    except:
        return False
if connect():
    print("Connected.")

else:
    print("Error 000 Not Found ! ")
    