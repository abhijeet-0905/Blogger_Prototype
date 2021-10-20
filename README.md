# Blogger_Prototype


[![git batch]](https://github.com/abhijeet-0905)

## Overview

Blogger_Prototype is a web based application where multiple users can each login with their own user credentials. They can create their own blog posts, update or delete their existing blog posts as well.

This application is built using Flask framework for the backend processing, and HTML and Bootstrap for the frontend design. It uses SQLAlchemy which is an open-source toolkit and Object-Relational Mapper(O.R.M).

## Features

- Each user can CREATE multiple blogs.
- Users can UPDATE or DELETE their blogs.
- Users can VIEW all the blogs posted on the site.
- Users can add their own profile picture.
- User can not update or delete the blogs posted by some other user.
- AUTHENTICATION is required to access a page other than HomePage.


## Tech

Blogger_Prototype uses a number of open source projects and toolkits to work properly:

- [Python][pyt]
- [Flask][flk]
- [SQLAlchemy][dbsql]
- [Bootstrap CDN][bst]
- [HTML][htm]

## Installation

In order to install the application, copy and paste all the files from the repository to your system directory.

Install the dependencies provided in [requirements.txt][dill] file.

If you want to use the pre-installed database files then go ahead and run the [app.py][dffl] file in the terminal and open the URL in the browser.

Otherwise, follow the below steps to create and initialize a new database before running the [app.py][dffl] file.

- set the current directory to the folder where you copied all the files.
```
cd your_dir_name
```
- set the FLASK_APP environment variable equal to the name of main application file.
```
set FLASK_APP=app.py
```
- initialize the database
```
flask db init
```
- prepare for migration
```
flask db migrate -m "YOUR MESSAGE"
```
- upgrade the database
```
flask db upgrade
```
- And now finally, RUN the [app.py][dffl] file.
```
python app.py
```

- copy and paste the URL in the browser.

> Note: Make sure your system is connected to the Internet. As Bootstrap have been included from CDN, it requires access to the internet.

## Conclusion
Blogger_Prototype is a basic, easy to use web application used to create blogs. That being said, more upgrades and modifications regarding both the frontend design and backend processing will be implemented soon.


   [dill]: <https://github.com/abhijeet-0905/Blogger_Prototype/blob/master/requirements.txt>
  [dffl]: <https://github.com/abhijeet-0905/Blogger_Prototype/blob/master/app.py>
  [pyt]: <https://www.python.org/>
  [flk]: <https://flask.palletsprojects.com/en/2.0.x/>
  [dbsql]: <https://www.sqlalchemy.org/>
  [bst]: <https://getbootstrap.com/docs/3.3/getting-started/>
  [htm]: <https://www.w3schools.com/html/>
  [git batch]: <https://img.shields.io/badge/abhijeet--0905-FollowMe-blue>
