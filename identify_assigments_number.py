import requests 
from bs4 import BeautifulSoup 

# this is basically copied straight from https://www.geeksforgeeks.org/reading-selected-webpage-content-using-python-web-scraping/
  
def pull_assmnts_num(): 
    # the target we want to open     
    url='https://www.gradescope.com/courses/231243/assignments'
      
    #open with GET method 
    resp=requests.get(url) 

    if resp.status_code==200:
        print("Successfully opened the web page")
        print("The news are as follow :-\n")

        # we need a parser,Python built-in HTML parser is enough .
        soup=BeautifulSoup(resp.text,'html.parser')

        # l is the list which contains all the text i.e news
        l=soup.find("div",{"class":"table--header"})

        print(l)
        #now we want to print only the text part of the anchor.
        #find all the elements of a, i.e anchor
#        for i in l.findAll("a"):
#            print(i.text)
    else:
        print("Error")


pull_assmnts_num()
