#GET
import requests

response = requests.get("https://api.github.com")
print(response)

#response object
import requests

response = requests.get("https://api.github.com")
print(response.text)

#status
import requests

response = requests.get("https://api.github.com")
print(response.status_code)

#json
import requests

response = requests.get("http://api.github.com")

data = response.json()
print(data)

#POST
import requests

data ={"username":"Shubhangi","password":123}
response = requests.post("https://httpbin.org/post", data=data)

print(response.text)

#delete
import requests

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)










