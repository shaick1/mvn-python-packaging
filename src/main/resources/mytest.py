#Import
import requests
import json

#Details on Sample Rest endpoints for Test purpose
#GET call to https://jsonplaceholder.typicode.com/posts/1/comments
#refer https://jsonplaceholder.typicode.com/guide.html

#HEADERS and PROXY
#use www-proxy-brmdc.us.oracle.com
MYPROXY={"http":"www-proxy-brmdc.us.oracle.com:80","https":"www-proxy-brmdc.us.oracle.com:80"}

#GET call
response = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments",proxies=MYPROXY)
print (response.status_code)
print(response.json())

#Process Json response
##find number of items in the Json
##find if we have any empty value in any item
##List all emails if email has ".net"
#for item in response.json():
# if "net" in item["email"]:
# print item["name"]
# print item["email"]


#POST call
body= {"title":"mytitle","body":"test","userId":1}
body_json=json.dumps(body)
#call to https://jsonplaceholder.typicode.com/posts
HEADERS = {"Content-type": "application/json"}

rep = requests.post("https://jsonplaceholder.typicode.com/posts",proxies=MYPROXY,headers=HEADERS,data=body_json)
print (rep.status_code)
print(rep.json())

#PUT call
#call to https://jsonplaceholder.typicode.com/posts/1
#HEADERS = {"Content-type": "application/json"}

body= {"title":"mytitle","body":"tesqqqqt","userId":1}
body_json=json.dumps(body)
#call to https://jsonplaceholder.typicode.com/posts
HEADERS = {"Content-type": "application/json"}

rep = requests.put("https://jsonplaceholder.typicode.com/posts/1",proxies=MYPROXY,headers=HEADERS,data=body_json)
print (rep.status_code)
print(rep.json())

#DELETE call
#call to https://jsonplaceholder.typicode.com/posts/1

rep = requests.delete("https://jsonplaceholder.typicode.com/posts/1",proxies=MYPROXY)
print (rep.status_code)
print(rep.json())
