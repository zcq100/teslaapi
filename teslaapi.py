import configparser
import requests
import logging
import json
import pickle
import os

logging.basicConfig(level=logging.DEBUG)


class Connect:
    def __init__(self, email, passwd, access_token=None):
        self.headers = {'User-Agent': 'app'}
        self.headers["Content-Type"] = "application/json"

        self.access_token = None
        self.expiration = 0
        self.baseurl = "https://owner-api.teslamotors.com"

        if access_token:
            self.__sethead(access_token)
        else:
            self.oauth = {
                "grant_type": "password",
                "client_id": "81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384",
                "client_secret": "c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3",
                "email": email,
                "password": passwd
            }
            reps = self.post("/oauth/token", json.dumps(self.oauth))
            logging.info(f"获取到的Token:{reps}")
            access_token = reps["access_token"]
            self.__sethead(access_token)

    def post(self, command, data={}):
        url = self.baseurl+command
        resp = requests.post(url, headers=self.headers, data=data)
        j = resp.json()
        logging.debug(j)
        return j

    def get(self, command, params=None):
        url = self.baseurl+command
        resp = requests.get(url, headers=self.headers, params=params)
        j = resp.json()
        logging.debug(j)
        return j

    def __sethead(self, access_token, expiration=0):
        self.access_token = access_token
        self.expiration = expiration
        self.headers["Authorization"] = f"Bearer {access_token}"


class Vehicles:
    def __init__(self, connect):
        self.connect = connect
        self._cars = []
        self._car = None

    def cars(self):
        resp = self.connect.get("/api/1/vehicles")
        for car in resp["response"]:
            self._cars.append(car)
        self._car = self._cars[0]

    def info(self):
        resp = self.connect.get(
            "/api/1/vehicles/{id}/vehicle_data".format(self._car["id"]))
        print(resp)
