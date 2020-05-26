# Scrape the web to rank a list of python frameworks

## USAGE
```
python scrape_the_web_python_frameworks.py framework1, framework2 [,framework_N]
        e.g.
python scrape_the_web_python_frameworks.py django, web2py, cherrypi, flask, bottle, quixote
```
  
## OUTPUT
```
django - 43,122,190
flask  - 20,101,200
...
web2py -  9,200,123
``` 

## LIBRARIES USED

Uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#), [Requests](https://requests.readthedocs.io/en/master/) and [Google results](https://www.google.com/search?q=python+django) to pull it all together.

* **BeautifulSoup** - Python library used for pulling data out of HTML and XML files 
* **Requests** - Python HTTP library. Used to read the contents a website using the <b>get</b> function 
* **Google query** - get the for the various framework rankings as HTML 

For example, a google search for python and django, yields, among other things:

        About 48,500,000 results (0.52 seconds)
        
and another search for python and flask yields:

        About 25,300,000 results (0.62 seconds)
        
We can do this for all the pyhton frameworks and rank the results.

## AUTOMATING (using Python)

Here is one method of automating this task.

1. Use the **get** function of **Requests** to get the HTML contents of a **Google query** on **python** and the **xxx_framework**, where **xxx_frameworks** is **django**, **flask**, **web2py** etc

              requests.get('https://www.google.com/search?q=python+django')
              
2. Use **BeautifulSoup** to look for the id result-stat, and save the number found
        
              soup = BeautifulSoup(requests.get('https://www.google.com/search?q=python+django'), 'html.parser')
              get_number_from(soup.find(id="result-stat"))
              
        
 3. Repeat for each framework
        
 4. Rank the results, with the highest-numbered framework first
