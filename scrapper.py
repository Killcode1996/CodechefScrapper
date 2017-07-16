from bs4 import BeautifulSoup
import json
import requests
import urllib

class Scrapper:


     def __init__(self, handle):
         self.handl=handle
         try:

             request = "https://www.codechef.com/users/" + self.handl
             r = requests.get(request)
             self.soup = BeautifulSoup(r.text, "html.parser")
             self.fin = self.soup.find("div", {"class": "rating-header"})
             self.ranks = self.soup.find("div", {"class": "rating-ranks"})
             self.rating = self.fin.find("div", {"class": "rating-number"})
             self.stars = self.fin.find("div", {"class": "rating-star"})
             self.question_solved = self.soup.find("section", {"class": "rating-data-section problems-solved"})
             self.contest_Attended_List = self.question_solved.findAll("p")
             self.solved_list = self.question_solved.find("span")
             self.lists_are = self.solved_list.findAll("a");
             self.allranks = self.ranks.findAll("li")
             self.Highest_rating = self.fin.find("small")
         except:
             print("Invalid Input :( ")


     def overAllRating(self):
         res=self.rating.text
         print(res)
         return res

     def countryRank(self):
         Rank_list = []
         for ran in self.allranks:
             Rank_list.append(ran.find("a").text)
         return Rank_list[0]

     def globalRank(self):
         Rank_list = []
         for ran in self.allranks:
             Rank_list.append(ran.find("a").text)
         return Rank_list[1]

     def ratingStars(self):
         st = ""
         for star in self.stars:
             st += star.text
         return st

     def highestRating(self):

         vt = self.Highest_rating.text
         ans=""
         for i in vt:
             if i>='0' and i<='9':
                 ans+=i
         return ans

     def contestAttended(self):
         cnt = 1
         for items in self.contest_Attended_List:
             cnt = cnt + 1
         return cnt

     def problemsolved(self):
            print("Practice Problems solved are ::  ")
            list=[]
            for problems in self.lists_are:
                list.append(problems.text)
            return list
