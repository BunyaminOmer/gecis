import requests
import json

class Service:
   url = "https://randomuser.me/api/"

   def send(self):
      response = requests.get(self.url)
      return response.json()
   
   def parse_data(self):
      tut = self.send() 
      result = tut["results"]
      for r in result:
         print(r["gender"], 1)
         print(r["name"]["title"], 2)
         print(r["name"]["first"], 3)
         print(r["name"]["last"], 4)
         print(r["location"]["street"]["number"], 5)
         print(r["location"]["street"]["name"], 6)
         print(r["location"]["city"], 7)
         print(r["location"]["state"], 8)
         print(r["location"]["country"], 9)
         print(r["location"]["postcode"], 10)
         print(r["location"]["coordinates"]["latitude"], 11)
         print(r["location"]["coordinates"]["longitude"], 12)
         print(r["location"]["timezone"]["offset"], 13)
         print(r["location"]["timezone"]["description"], 14)
         print(r["email"], 15)
         print(r["login"]["uuid"], 16)
         print(r["login"]["username"], 17)
         print(r["login"]["password"], 18)
         print(r["login"]["salt"], 19)
         print(r["login"]["md5"], 21)
         print(r["login"]["sha1"], 22)
         print(r["login"]["sha256"], 23)
         print(r["dob"]["date"], 24)
         print(r["dob"]["age"], 25)
         print(r["registered"]["date"], 26)
         print(r["registered"]["age"], 27)
         print(r["phone"], 28)
         print(r["cell"], 29)
         print(r["id"]["name"], 30)
         print(r["id"]["name"], 31)
         print(r["picture"]["large"], 32)
         print(r["picture"]["medium"], 33)
         print(r["picture"]["large"], 34)
         print(r["nat"], 35)
      x = tut["info"]["seed"]
      print(x, 36)
      y = tut["info"]["results"]
      print(y, 37)
      w = tut["info"]["page"]
      print(w, 38)
      z = tut["info"]["version"]
      print(z, 39)

nesne = Service()
nesne.parse_data()