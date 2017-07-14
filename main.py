from bs4 import BeautifulSoup
import json
import requests
import urllib

#handle= input("Inter Handle ::  ")
handle="atulmaster"
request="https://www.codechef.com/users/"+handle
r=requests.get(request)
soup = BeautifulSoup(r.text,"html.parser")
fin = soup.find("div",{"class":"rating-header"})
ranks=soup.find("div",{"class":"rating-ranks"})
rating=fin.find("div",{"class":"rating-number"})
stars = fin.find("div",{"class":"rating-star"})
res=rating.text
print("Your rank on Codechef :: "+res)
st=""
for star in stars:
   st+=star.text
print("Your stars in codechef :: "+st)
Highest_rating=fin.find("small")
print("Your "+Highest_rating.text)
allranks=ranks.findAll("li")
Rank_list=[]
for ran in allranks:
    Rank_list.append(ran.find("a").text)
print("Your Global Rank :: "+Rank_list[0])
print("Your Country Rank :: "+Rank_list[1])
question_solved=soup.find("div",{"class":"content"})
solve_list=question_solved.find("article")
print(solve_list.text)