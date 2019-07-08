import requests
import validators
from bs4 import BeautifulSoup

def retrieve(siteurl,query,debug,verbose):
    query=query.lower()
    if validators.url(siteurl):
        print("Working ...")
    else:
        print("invalid url")
    if debug==True:
        print("Debugging has been Enabled")
    if verbose==True:
        print("Verbose output is Enabled")
    
    if verbose==True:
        print("Making the request to the url:")
        print(siteurl)

    r = requests.get(siteurl)
    
    if debug==True:
        print(r.content)
        print(r.status_code)
        print(r.headers)
    
    if verbose==True:
        print("Passing the downloaded content to BeautifulSoup from url")
        print(siteurl)

    soup = BeautifulSoup(r.content, 'html5lib')

    if debug==True:
        print("Output:")
        print(soup.prettify())
    output={}
    if verbose==True:
        print("Parsing to find a tags:")
    for link in soup.find_all('a'):
        output[link.get_text().lower()]=link.get("href")

    if debug==True:
        print(output)


    print("done parsing")
    if verbose==True:
        print("Finding the query")
    if query.lower() in output:
        print("found")
        print(output[query.lower()])
        return output[query.lower()]
    else:
        return "Error!"


