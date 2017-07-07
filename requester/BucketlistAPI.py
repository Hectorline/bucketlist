import requests
import json


class BucketlistAPI:
    def __init__(self):
        self.url = 'http://localhost:5000'
        self.access_token = None

    def registration(self, email, password):
        headers = {
            'content-type': "application/json"
        }
        payload = '{"email":"' + email + '","password":"' + password + '"}'

        r = requests.request("POST", '{0}/auth/register'.format(self.url), data=payload, headers=headers)
        if r.status_code == 201:
            print(r.content)
        else:
            print(r.status_code)

    def login(self, email, password):
        headers = {
            'content-type': "application/json"
        }
        payload = '{"email":"' + email + '","password":"' + password + '"}'

        r = requests.request("POST", self.url + '/auth/login', data=payload, headers=headers)
        self.access_token = "Bearer " + r.json()["access_token"]
        print(r.json()["access_token"])

    def create(self, title):
        if self.access_token:
            payload = '{"name":"' + title + '"}'
            headers = '{"content-type":"application/json","authorization":"' + self.access_token + '"}'
            r = requests.request("POST", self.url + '/bucketlists/', data=payload, headers=json.loads(headers))
        else:
            raise Exception('You don\'t have any token linked')

        print(r.json())

    def read(self):
        if self.access_token:
            headers = '{"content-type":"application/json","authorization":"' + self.access_token + '"}'
            r = requests.request("GET", self.url + '/bucketlists/', headers=json.loads(headers))
        else:
            raise Exception('You don\'t have any token linked')

        print(r.json())

for j in range(1000):
    BucketlistAPI = BucketlistAPI()
    BucketlistAPI.registration("'prueba@test"+str(i)+".com'",'carajuelos')
    BucketlistAPI.login("'prueba@test"+str(i)+".com'",'carajuelos')
#print(BucketlistAPI.access_token)
    for i in range(100):
        BucketlistAPI.create(str(i)+' elefantes se balanceaban')