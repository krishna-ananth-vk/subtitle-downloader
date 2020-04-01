import requests 
from bs4 import BeautifulSoup 
movie = input()
movie = movie.split()
movie = "%20".join(movie)
# print(movie)

URL = "https://yts-subs.com/search/"+movie
header = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

r = requests.get(URL,headers=header) 
print(r.url)
soup = BeautifulSoup(r.content, 'html5lib') 
# print(soup.div['media-body'])
title = soup.find_all(class_='media-movie-clickable',limit=3)
c = 1
for i in title:
    # print(i)
    k = str(i)
    k = BeautifulSoup(k,'html5lib')
    
    print(c,k.find(class_='media-heading').text,end="--")
    print(k.find(class_='movinfo-section').text.strip())
    c+=1
    
n = int(input("Enter number to download : "))

k = str(title[n-1])
k = BeautifulSoup(k,'html5lib')
l = (k.find(class_='media-heading').text)
print(l)
print("Getting info...")

URL = "https://yts-subs.com"+k.a['href']
print(URL)

s = requests.get(URL,headers=header) 
# print(r.url)
ssoup = BeautifulSoup(s.content, 'html5lib') 
print(ssoup.find(class_='high-rating'))



title = ssoup.find_all(class_='high-rating')
print(title)
c = 1
for i in title:
    # print(i)
    k = str(i)
    k = BeautifulSoup(k,'html5lib')
    
    print(c,k.find(class_='sub-lang').text,end="  rating: ")
    print(k.find(class_='label').text)
    print(k.a['href'])
    c+=1
    
n = int(input("Enter number to download : "))

print("Getting File link...")


k = str(title[n-1])
k = BeautifulSoup(k,'html5lib')
# print(k.find(class_='media-heading').text)

URL = "https://yts-subs.com"+k.a['href']
print(URL)
print("Downloading...")
r = requests.get(URL) # create HTTP response object 

l = l+'.zip'
with open(l,'wb') as f: 
  
    # Saving received content as a png file in 
    # binary format 
  
    # write the contents of the response (r.content) 
    # to a new file in binary mode. 
    f.write(r.content) 

print("Unzipping....")






# print(soup.head)
