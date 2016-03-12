# to be run on an individual computer, not the server
# works for both python 2 and 3
# request is complex, but only relies on standard libraries
# to make testing faster, message is sent along with data
#     so that single computer sends multiple messages.

import platform

try:
    import http.client as h
    import urllib.parse as p
except:
    import httplib as h
    import urllib as p
    input = raw_input


url = "0.0.0.0:8000" # will throw error unless it is replaced with actual website
port = 8000
heads = {"Content-Type" : "application/json"}
info = {
        "plat" : platform.platform(),
        "ver" : platform.python_version(),
       }

def send(message = ""):
    """Encodes and sends message (str) as post request"""
    conn = h.HTTPConnection(url)
    info["msg"] = message
    data = p.urlencode(info)
    req = conn.request('POST', '/send/', data)
    conn.close()

if __name__ == "__main__":
    while True:
        msg = input("Message to send with data: ")
        send(msg)

