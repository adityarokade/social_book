import requests
import json



URL = "http://localhost:8000/auth/users/"

def post_data():
    # data = {
    #     "emial":"adirokade15@gmail.com",
    #     "name":"AdityaRokade",
    #     "password":"djangoroot",
    #     "re_password":"djangoroot",
    #     "first_name":"adi",
    #     "last_name":"rokade"
    #     }

    # data ={
    #     'email':'adirokade15@gmail.com',
    #     'name':'AdityaRokade',
    #     'password':'djangoroot',
    #     're_password':'djangoroot',
    #     'first_name':'adi',
    #     'last_name':'rokade'
    # }
    # print(type(data))
    # print("myapp1")
    # json_data = json.dumps(data)
    # print("myapp2",json_data)
    # print(type(json_data))
    r = requests.post(url = URL, data = data)

    data = r.json()
    print(data)



    
post_data()