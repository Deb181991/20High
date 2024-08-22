import json

import requests


class Api_helper:
    # API-POST method
    url = "https://uat-app.lineclearexpressonline.com/Accounts/CreateShipment"
    # payload = "{\"user\": \"suraj.parida71@gmail.com\", \"passwd\":\"Test@1234\"}"
    # user = "suraj.parida71@gmail.com"
    # passwd = "Test@1234"
    headers = {
        'Authorization': "c3VyYWoucGFyaWRhNzFAZ21haWwuY29tOlRlc3RAMTIzNA==",
        'Content-Type': "application/json",
        # 'Authorization': "Basic c3VyYWoucGFyaWRhNzFAZ21haWwuY29tOlRlc3RAMTIzNA==",
        # 'Postman-Token': "<calculated when request is sent>",
        # 'Content-Type': "application/json",
        # 'Content-Length': "<calculated when request is sent>",
        # 'Host': "<calculated when request is sent>s",
        # 'User-Agent': "PostmanRuntime/7.29.2",
        # 'Accept': "*/*",
        # 'Accept-Encoding': "gzip, deflate, br",
        # 'Connection': "keep-alive",
    }

    # responce = requests.request("POST", url, data=payload)
    response = requests.post(url, headers=headers, data=json.loads(open("data.json", "r").read()))
    # a = requests.post(url2, data=json.loads(open("data.json", "r").read()))
    # print(a)
    print(response)
    print(response.content)
    print(response.headers)
    # print(responce.json())
    # print(a.json())
    # b = a.json()
    # assert a.json()['job'] == 'Automation developer'
    # # assert a.status_code == 203
    # assert a.status_code == 201
    # # MAke post request with json input body
    # rep = requests.post(url2, b)
    # print(rep.content)
    # # Validating responce code
    # assert rep.status_code == 201
    # # fetch header from responce
    # print(rep.headers)
    # print(rep.headers.get('Content-Type'))
    # print(rep.headers.get('Content-Length'))
    # rep_json = json.loads(rep.text)
    # print(rep_json)
    # id = rep_json['id']
    # print(id)
