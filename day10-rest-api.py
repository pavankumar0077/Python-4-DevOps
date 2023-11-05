import requests


#Make a GET request to a URL
url_get = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url_get)

# Check if the request was successful (HTTP Status code 200)
if response.status_code == 200:
    #Print the response content
    print(response.json())
else:
    #Print an error message if the request was not successful
    print(f"Error: {response.status_code}")


url_post = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'pavan',
    'body': 'Checking...',
    'userId': 101
}

# Make a POST request with the data
response = requests.post(url_post, json=data)

if response.status_code == 201:
    print(f"Success! New post created with ID {response.json()['id']}")
else:
    print(f"Data not saved or posted.. ERROR : {response.status_code}")



# Make a PUT request with the data
url_put = 'https://jsonplaceholder.typicode.com/posts/1'
data = {
    'title': 'pavan',
    'body': 'Checking...',
}

response = requests.put(url_put, json=data)

if response.status_code == 200:
    print(f"Success! Post updated: {response.json()}")
else:
    print(f"Error: {response.status_code}")


#Make a DELETE request
url_del = 'https://jsonplaceholder.typicode.com/posts/1'

if response.status_code == 200:
    print("Success! Post deleted")
else:
    print(f"Error: {response.status_code}")