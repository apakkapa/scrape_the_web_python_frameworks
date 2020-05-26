# Scrape the web to rank a list of known python frameworks

USAGE

        scrape_the_web_python_frameworks framework1, framework2 [,framework_N]
  
        e.g.
  
        scrape_the_web_python_frameworks django, web2py, cherrypi, flask, bottle, quixote
  
OUTPUT

        django - 43,122,190
        flask  - 20,101,200
        ...
        web2py -  9,200,123
 

LIBRARIES USED

        Uses BeautifulSoup, Requests and Google results to pull it all together.
          BeautifulSoup is a Python library used for pulling data out of HTML and XML files
          Requests is a Python HTTP library. In this case it is used to read the contents a website using the get function.
          The Google query is used to get the HTML for the various rankings

For example, a google search for python and django, yields, among ohter things:

        About 48,500,000 results (0.52 seconds)
        
and another search for python and flask yields:

        About 25,300,000 results (0.62 seconds)
        
We can do this for all the pyhton frameworks and rank the results.

AUTOMATING (using Python)
Here is one method of automating this task.

        Use the get function of Requests to get the contents of a Google query on python and the xxx_framework, 
        where xxx_frameworks is django, flask, web2py etc

              requests.get('https://www.google.com/search?q=python+django')
              
        Use BeautifulSoup to look for the id result-stat, and save the number found
        
              soup = BeautifulSoup(requests.get('https://www.google.com/search?q=python+django'), 'html.parser')
              get_number_from(soup.find(id="result-stat"))
              
        
        Rinse and repeat
        
        Rank the results, with the highest number first

Hope you find this useful
