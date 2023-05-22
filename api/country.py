from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):

        s_p=self.path 
        print(s_p)
        url_components = parse.urlsplit(s_p)
        print(url_components)
        query_strings_list = parse.parse_qsl(url_components.query)
        print(query_strings_list)
        dic = dict(query_strings_list)
        country = dic.get("country")
        print(country)
        
        if country:
            url = f"https://restcountries.com/v3.1/name/{country}"
            print(url)
            res = requests.get(url)
            data = res.json()
            result = data[0]["capital"][0]
            print(result)

            message = f"The capital of {country} is {result}"
        else:
            message = "There is no country specified."

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return
    
