import requests

def client():
    """ creds = {"username":"admin","password":"1234"}

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
                             data=creds) """
    
    token = "Token 8c9a69e3c2b8418ca15e73891d0c6df9b640dab6"
    headers = {"Authorization": token}
    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)
    
    print("Status code:", response.status_code)
    response_data = response.json()
    print(response_data)
    #print(response)

if __name__=="__main__":
    client()