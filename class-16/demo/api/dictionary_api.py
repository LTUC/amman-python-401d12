# url = https://api.dictionaryapi.dev/api/v2/entries/en/<word>
import requests

# serverless function

from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        s = self.path
        url_component = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_component.query)
        my_dic = dict(query_string_list)
        
        word = my_dic["word"]

        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
        definitions_arr =[]

        req = requests.get(url+word)
        rec_data = req.json()
        # print(rec_data)
        
        for word_data in rec_data:
            definition_result = word_data['meanings'][0]["definitions"][0]["definition"]
            definitions_arr.append(definition_result)

        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        if str(definitions_arr):
            msg = str(definitions_arr)
        else:
            msg="no response"
        
        self.wfile.write(msg.encode())

        return
