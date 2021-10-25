from xmlrpc.server import SimpleXMLRPCServer
import re

def strcount(text):
    answer = ""
    my_dict = {}
    for k in text:
        if k.isalpha():
            if k in my_dict:
                my_dict[k]=my_dict[k]+1
            else:
                my_dict[k]=1
    answer = str(my_dict)
    return answer

server = SimpleXMLRPCServer (("localhost",8000))
print("START")
server.register_function (strcount, "strcount")
server.serve_forever()
