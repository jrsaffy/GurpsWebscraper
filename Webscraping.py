import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#Opens webpages from gurps wiki and creates a csv with info about advantages, disadvantages, and skills

#Open, Save, and Parce Webpage
#Save info as csv


#Opens the webpage and returns it
#parameters should be type string
def openWebpage(url):
	uClient = uReq(url)
	pageHTML = uClient.read()
	pageSoup = soup(pageHTML,"html.parser")
	return pageSoup
	
#finds all of the tables labeled as "wikitable"
def searchSoup(soup):
	tables = soup.findAll("table",{"class":"wikitable"})
	return tables
	
#Function below breaks single responsibility - Not best practice:
	#Also formats and removes blank lines
	
#How to make more general?
	#What if the tables have different dimentions?
	#What if you dont want to join tables?
	

#turns the tables into a list of rows 
def transformToList(tables):
	contents = []
	for i in tables:
		tableRows = i.find_all('tr')
		for j in tableRows:
			rowList = []
			cell = j.find_all('td')
			for k in cell:
				text = str(k.text)
				text = text[0:-1]
				rowList.append(text)
			if(len(rowList) > 0):
				contents.append(rowList)	
	return contents


		
#takes the list created in "transformToList" and writes a csv file
def createCSV(list,fileName):
	fileName = open(fileName + ".csv","w+")
	for i in range(0,len(list)):
		for j in range(0,len(list[i])):
			fileName.write((list[i])[j] + ',')
		fileName.write('\n')
	fileName.close()
	

#Main program here:
def main():
	#Advantages
	advantagesWebpage = openWebpage("https://gurps.fandom.com/wiki/List_of_Advantages")
	advantagesTables = searchSoup(advantagesWebpage)
	advantages = transformToList(advantagesTables)
	createCSV(advantages,"advantages")

	#Disadvantages
	disadvantagesWebpage = openWebpage("https://gurps.fandom.com/wiki/List_of_Disadvantages")
	disadvantagesTables = searchSoup(disadvantagesWebpage)
	disadvantages = transformToList(disadvantagesTables)
	createCSV(disadvantages,"disadvantages")

	#Skills
	skillsWebpage = openWebpage("https://gurps.fandom.com/wiki/List_of_Skills")
	skillsTables = searchSoup(skillsWebpage)
	skills = transformToList(skillsTables)
	createCSV(skills,"skills")

if __name__ == "__main__":
	main()





















