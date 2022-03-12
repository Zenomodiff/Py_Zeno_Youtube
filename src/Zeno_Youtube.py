import re
import urllib.request
import requests
import json, random, string
from bs4 import BeautifulSoup as bs

class Youtube_Random:

    def VideoRandom(self):

        for i in range(1,2):
            page_number = (i)
        length = int(5) 
        upper = string.ascii_lowercase
        data = random.sample(upper,length)
        parser = "".join(data)
        search_keyword = parser
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        Video_Link = "https://www.youtube.com/watch?v=" + video_ids[1]
        r = requests.get(Video_Link)
        soup = bs(r.content, 'lxml')
        new = soup.select_one('title').text
        Title = new[:-10]
        new_string = ''
        for char in Title:
            if char != '"' and char != "'":
                new_string +=char
        Video_Name = new_string
        total = (f"{Video_Name} --- {Video_Link}")
        return total

ytRand = Youtube_Random()

class Youtube_Title:

    def VideoTitle(self): 

        for i in range(1,2):
            page_number = (i)
        length = int(5) 
        upper = string.ascii_lowercase
        data = random.sample(upper,length)
        parser = "".join(data)
        search_keyword = parser
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        Video_Link = "https://www.youtube.com/watch?v=" + video_ids[1]
        r = requests.get(Video_Link)
        soup = bs(r.content, 'lxml')
        new = soup.select_one('title').text
        Title = new[:-10]
        String = ''
        for char in Title:
            if char != '"' and char != "'":
                String +=char
        Video_Name = String 
        return Video_Name

ytTitle = Youtube_Title()

class Youtube_Link:

    def VideoLink(self): 

        for i in range(1,2):
            page_number = (i)
        length = int(5) 
        upper = string.ascii_lowercase
        data = random.sample(upper,length)
        parser = "".join(data)
        search_keyword = parser
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        Video_Link = "https://www.youtube.com/watch?v=" + video_ids[1] 
        return Video_Link

ytlink = Youtube_Link()

