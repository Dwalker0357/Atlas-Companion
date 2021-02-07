![](application/static/pics/atlas_title.png)
<br>
<br>
https://trello.com/b/nbbi3EbD/path-of-exile-atlas-app
<br>
<br>
Atlas Companion was a passion project created that uses python3-flask, jinja2's templating and mysql databases. Its goal was to deliver current updated information about the world map of the video game; path of exile, commonly referred to as the atlas of worlds or atlas for short.
 
<br>

The initial goals of the app were the following

• Create an image-mapped multi hyperlinked home page that linked to each corresponding page. 
<br>
• Create a dedicated information webpage for each of the 8 regions of the atlas plus one extra for the uncharted realms.
<br>
• Add a region skill tree image to each region page that opens a new webpage when prompted for a bigger clearer view of the information
<br>
• Display the relevant information on each region webpage including but not limited to maps, atlas base types and divination cards    
<br>
• The ability to create, display, update and delete (CRUD) map entries using the created relational mysql database
<br>
• The ability to CRUD divination card entry’s to the relevant assigned maps
<br>
• The ability to CRUD filtered tables of each divination card and what maps it is assigned to
<br>
• A search bar located on the home page to quickly navigate to the information you are looking for

![](readme_pics/trello.png)

<br>
My database would consist of five tables seen below in my ERD diagram:
<br>
<br>

![](readme_pics/ERD.png)

<br>
<br>
As seen above we have a separate table to allocate our many to many to relationships between divination cards and maps.
To query all the divination cards in a single map we use the following:
<br>

![](readme_pics/query1.png)

<br>
And for the reverse for what maps contain a single divination card:
<br>

![](readme_pics/query2.png)






<br>
<br>
My SQL database defined as db. Models and built using create.py:

<br>


![](readme_pics/models1.png)



![](readme_pics/models2.png)

<br>
<br>

__**<h1>Risk Assessment<h1>**__

<br>

![](readme_pics/risk_assessment.png)

<br>

<br>



__**Challenges faced and project evolution**__

<br>
My first challenge was creating my tables and implementing my relationships so I can query all the data I wanted. I initially had four tables but I soon realised the limitations of SQL, I had to create another table Cmap, so I could map as many divination cards to as many maps as I wanted using the corresponding foreign keys and as many to many relationships.
<br>
My Second challenge, and definitely my biggest, was trying to implement my pre-existing mysql database into my application, I tried on and off but mostly on for around three days to get it to work but it just refused to.
<br>
So I learned a very valuable lesson that it is almost always better to build your SQL tables using the flask db.models classes, in hindsight I would have saved a lot of time troubleshooting. which I would have used to add features to my application.
<br>
As a result of my issues during the development, I was unable to add all the features I planned to due to time restrictions, managing to only add the CRUD functionally of maps.
Moving forward I will take more consideration when designing, creating, and integrating databases into my application and will always make sure to create them using flask where ever possible. 
<br>
<br>
                                                                        
                                                                      
__**Completed Application showcase:**__
   
<br>

Interactive hyperlinked global region map
  
![](readme_pics/atlas_home.png)

<br>
<br>

The Html code behide the image mapping and home page

<br>


![](readme_pics/home_html.png)

<br>

My New Vastir Region page with implemented create form and filtered map display table
 
  <br>
  
  ![](readme_pics/new_vastir.png)


<br>

Expanded skill tree image that opens in a new tab
  
  <br>
  
  
![](readme_pics/tree_trello.png)
  
  
  <br>
  
  
  __**Video Demonstration of my application and all its features**__
  
 
 <br> 
  
  
  ![](readme_pics/Demo.mp4)
  
  
  <br>
  
  
  Application Test Coverage Report using Flask Pytest 

  
  <br>
  
  
  ![](readme_pics/test_coverage.png)
  
  
  <br>
  
  Application being deployed with jenkins via gunicorn
 
 <br>
 
 ![](readme_pics/jenkins.png)


<br>
<br>


__**Conclusion**__
 
 
 <br>
 

In conclusion, I think for the current knowledge I processed during my first project and what I possess now is night and day, If I were to face the same challenges that stunted my development I feel that would be able to overcome them in a fraction of the time.

<br>

It has been an excellent learning experience in project management, python/html programming and database management, I very much look forward in the future for continued development of flask based applications and continued support/redesign of this project as it was a passion project.

