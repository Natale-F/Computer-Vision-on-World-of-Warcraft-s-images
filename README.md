# Computer Vision on World of Warcraft's images

![alt text](https://upload.wikimedia.org/wikipedia/fr/4/42/World_of_Warcraft_Shadowlands_Logo.png)

Being a World of Warcraft player for many years and recently graduated with a Master's degree in Applied Mathematics, Statistics and Data Science. I was wondering on what subject I could do a project. 
While wandering on the WoW website I realized that an important number of images were available and that it would be possible to use my knowledge of the game as well as my professional skills to realize a project of Artificial Intelligence from these images.

How did I realise that I could do something with this data ? 

See for yourself some examples!



Gnome (Alliance)             |  Tauren (Horde)
:-------------------------:|:-------------------------:
<img src="https://wow.zamimg.com/uploads/screenshots/normal/389945-gnome.jpg" width="500" height="400">  |  <img src="https://wow.zamimg.com/uploads/screenshots/normal/858396-tauren.jpg" width="500" height="400"> 

Human (Alliance)             |   Orc (Horde)
:-------------------------:|:-------------------------:
<img src="https://wow.zamimg.com/uploads/screenshots/normal/427531-humain.jpg" width="500" height="400"> | <img src="https://wow.zamimg.com/uploads/screenshots/normal/438665-orc.jpg" width="500" height="400">

We can clearly distinguish differences between these characters as a human (skin colour, texture, face, size, ...). The purpose of this project is to work and use some Data Sciences skills with a fun and personal subject in order to allow an AI algorithm to identify these characteristics that we naturally distinguish.

**Enjoy it !**

 # Main steps :
 - **Download a large dataset using Web Scraping** (character's images with their features, for example "Orc", "Horde", ...). 
 
    <img src="https://miro.medium.com/max/1200/0*tvUoZ_MhMZQ69t5e.png">
    
    - "recovery_players_names.ipynb" retrieves the names and servers of the 50 000 best EU players (items level) and store these informations in a DataFrame
    - "image_download.ipynb" use the previous DataFrame to retrives more informations about these players and store character's images.
      One of the 2 downloads database can be download **here :** https://drive.google.com/drive/folders/1jQmVFVDiBfFnWIGnOfJNonF2-bA6xQS5?usp=sharing

 - **Data formatting** prepares the downloaded data and formats it in a format useful for machine learning.    
    - "data_extracting.ipynb" : prepares the "labels information" for the 2 previously downloaded bases and saves it in csv documents
    - "prepare_directory_structure.ipynb" : moves the images from the "without background" database into an architecture easily usable for a classification task using keras       tools. 
    
    <img src="https://scontent-mrs2-2.xx.fbcdn.net/v/t1.15752-9/129598791_1234404036944097_2302524932097460726_n.png?_nc_cat=102&ccb=2&_nc_sid=ae9488&_nc_ohc=gfD077toyaEAX8-j65e&_nc_ht=scontent-mrs2-2.xx&oh=95c6de9e868dba5d0b5def9ada468024&oe=5FEAEEDF">
   
 - **Machine Learning tasks** : try some AI algorithms on these data !
    - "...." : simple binary classification task --> find the faction of the character !
    
    
      





**Link DATA :** 

Images origins :
 - logo World of Warcraft ! https://upload.wikimedia.org/wikipedia/fr/4/42/World_of_Warcraft_Shadowlands_Logo.png
 - Gnome picture : https://wow.zamimg.com/uploads/screenshots/normal/389945-gnome.jpg
 - Tauren picture : https://wow.zamimg.com/uploads/screenshots/normal/858396-tauren.jpg
 - Human picture : https://wow.zamimg.com/uploads/screenshots/normal/427531-humain.jpg
 - Orc picture : https://wow.zamimg.com/uploads/screenshots/normal/438665-orc.jpg
 - Web Scraping ! https://miro.medium.com/max/1200/0*tvUoZ_MhMZQ69t5e.png
 - 
 
