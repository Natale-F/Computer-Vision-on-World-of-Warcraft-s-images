# Computer Vision on World of Warcraft's images

![alt text](https://upload.wikimedia.org/wikipedia/fr/4/42/World_of_Warcraft_Shadowlands_Logo.png)

Being a World of Warcraft player for many years and recently graduated with a Master's degree in Applied Mathematics, Statistics and Data Science. I was wondering on what subject I could do a project. 
While wandering on the WoW website I realized that an important number of images were available and that it would be possible to use my knowledge of the game as well as my professional skills to realize a project of Artificial Intelligence from these images.

How did I realise that I could do something with these data ? 

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
       The 2 downloads database can be download from Google Drive : https://drive.google.com/drive/folders/1jQmVFVDiBfFnWIGnOfJNonF2-bA6xQS5?usp=sharing

 - **Data formatting** prepares the downloaded data and formats it in a format useful for machine learning.    
    - "data_extracting.ipynb" : prepares the "labels information" for the 2 previously downloaded bases and saves it in csv documents
    - "prepare_directory_structure.ipynb" : moves the images from the "with background" database into an architecture easily usable for a binary classification task (whether a character comes from the horde or from the alliance) into an architecture easily usable for a classification task using keras tools
    
    <img src="https://scontent-mrs2-2.xx.fbcdn.net/v/t1.15752-9/130465760_2792962437619996_1499920078488726211_n.png?_nc_cat=108&ccb=2&_nc_sid=ae9488&_nc_ohc=_ixeKiaQ4PEAX8PI8fk&_nc_ht=scontent-mrs2-2.xx&oh=668efa5fd9223638089f5461438f7b2a&oe=5FF5B297">
   
   - "resize_images.ipynb" : resize the images of the base "With_background" from size (1200, 1600) to (800, 700).
   
   
 - **Machine Learning** : try some Machine Learning algorithms on these data !
    - "baseline_model_and_problematic_images.ipynb" : this notebook helps to find an interval in which useful binary classification patterns (whether a character belongs to the horde or the alliance) will be found. This gives you an idea of the achievable performance of a model for this task before you even start coding!
    - "MLP_classifier.ipynb" : this notebook presents a first Neural Network model using Multi-Layer Perceptron, some explanations are given, the objective being especially to have a first model different from the "dumb" models.
    
