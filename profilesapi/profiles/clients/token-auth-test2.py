import requests

def client():
    data = {
        "username":"test",
        "email":"test@example.com",
        "password1":"changepass",
        "password2":"changepass"
    }

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
                            data=data)
    
    print("Status code:", response.status_code)
    response_data = response.json()
    print(response_data)
    #print(response)

if __name__=="__main__":
    client()