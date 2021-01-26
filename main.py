from bs4 import BeautifulSoup

with open ("website.html",'r') as file:
  inhoud = file.read()
#print(inhoud) 

soep=BeautifulSoup(inhoud,'html.parser')
#print(soep.prettify())

