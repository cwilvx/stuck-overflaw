<!-- <div style="text-align: center; border: 1px solid white; border-radius: 5px;">
    <h1>ST<span style="color: red">U</span>CK OVERFLOW!</h1>
    <h5>~ saving the student's lives since I don't know when 😆 ~</h5>
</div> -->
![](/images/hero.png)
[Stuck overflaw](https://be-social-django.herokuapp.com/) is a web application that enables university students to seek assistance and network with other students and lectures.

This web app is built using [Python 3](https://www.python.org/), The [Django Framework](https://www.djangoproject.com/) and a [PostgreSQL](https://www.postgresql.org/) database. Django is a high level Python web framework that encourages rapid development and clean and pragmatic design.

The app implements a combined full stack development web app structure.

> This project has been deployed using Heroku at https://be-social-django.herokuapp.com/. The page may load slowly for the first time. This is because the dynos my be sleeping. Please be patient as the page loads for the first time. Also, the app is only responsive on large screens. eg. on a laptop or desktop. Please view the deployed application using a laptop or a desktop computer.
---
### Running the app locally
Since this app uses the PostgreSQL database, you need to have it installed in your machine. You can download the package from [their website](https://www.postgresql.org/download/).

Assuming you have all the needed tools, ie. Python3 and Postgresql, following the next few steps will brew and serve your app.

### Step 1 -- Create a postgreSQL database
We'll need a database named `overflow` for this app. You can create it by running these commands in the `psql` terminal.
```sql
create database overflow; 
```
### Step 2 -- Cloning the project locally
Running the following series of commands on a terminal window will get your app ready for the next step.

```bash
$ git clone git@github.com:geoffrey45/edunet.git #cloning via SSH
# or clone via HTTPS
$ git clone https://github.com/geoffrey45/stack-overflaw.git 
$ cd stack-overflaw
$ source virtual/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```
### Step 3 -- Configure the environmental variables
Some variables need to be provided by the serving environment. In your project folder, locate a file named `.env.example`. Then, rename this file to `.env` and edit the necesary details.

### Step 4 -- Serving the app
Now that you have everything in place, you can serve the app by executing:

```bash
$ python manage.py runserver
```
### Back to the app
---
This app allow a user to do the following main things:
1. Ask questions on the platform.
2. Read and answer an existing question.
3. Create a blog post about any topic.
4. View and comment on an existing post.

### The basic features and procedures
---
#### Step 1 -- The Signup process
The user creates an account using a simple page. The page can be accessed at http://127.0.0.1:8000/signup/ on a development server

![](/images/signup.jpg)
> Users can not contribute to a post unless they are logged in.

Once the users create their account, they are logged in automatically for the first time. We have allowed this for MVP purposes.

---
On logging in, the user is redirected to the home page.

![](/images/home.jpg)

From the home page, the user can see a list of existing posts displayed as cards. These cards are sorted from latest to oldest.

From the sidebar, the users can perform the following operations:
- search existing posts
- view and edit their profile
- view, modify and delete all their published articles

#### Step 2 -- Creating a post

By hitting <kbd>New Post</kbd> from the side bar or <kbd>New Question</kbd> from the navbar, the user can create a new post.

![](/images/new_post.jpg)
Once the user submits the details, the form data is stored in the database and will be displayed on the home as the latest post.
> Did you know? You can click on an image to enlarge it.
#### Step 3 -- Contributing to a post
By clicking on <kbd>Show this thread</kbd> on a post card, a user will be directed to a page showing the post details and existing comments. 

![](/images/post.jpg)

By filling and submitting the comments form at the bottom of this page, a user can contribute to this single post.

![](/images/comment.jpg)

---
## Other functionalities
---
### 1. GET all posts from `this` user
Users can retrieve all the posts created by a certain user by clicking <kbd>Users</kbd> under `Browse` from the sidebar.

![](/images/users.jpg)

By clicking <kbd>All from user</kbd>, the user can get a list of posts displayed as cards.

![](/images/all_from_user.jpg)

### 2. Search for posts
A user can search through all the posts by submitting the search term in the search form found in the sidebar.

![](/images/search.jpg)

### 3. Update an existing post
Users can update their posts, by clicking the <kbd>Update</kbd> button that only appears on the single post, only if they are logged in.

![](/images/update_post.jpg)

### 4. Deleting posts
If users are logged in, they can update or delete their existing posts from the sidebar.

![](/images/delete_post.jpg)

### 5. User account actions
Users can view their profile by clicking <kbd>Profile</kbd> button from the sidebar. Users can also update update or delete their profiles from the _`Account Actions`_ card found in the sidebar.

![](/images/profile.jpg)

---

### TL;DR and a bottom line
We have used Django Python web development framework to build this app. The app offers close to all the expected minimum viable product (MVP) features. The app's UI is not thoroughly polished due to the much effort and time used to polish the MVP logic.

As you may have noticed, most of the actions in the app have no confirmation. eg. the delete post or account action, create account, etc. We only allowed this for MVP purposes. In a production environment, these actions need to be checked to avoid accidental loss of data.

> For now, the app is only responsive on a large screen .eg. a computer or laptop screen. 

That's it

> Did you know? We were planning of using a more industrial approach to this project. We were in the process of developing this project using [Flask](https://flask.palletsprojects.com/) and [Mongo Db Atlas](https://www.mongodb.com/cloud/atlas) for the APIs and maybe [Vue.js](https://vuejs.org/) for the frontend. We quit mid-way due to to time factors. You can still look at the half-way developed API deployed [here](https://be-social-be.herokuapp.com/posts) and the code in [this GitHub repo](https://github.com/geoffrey45/be-social-be/). (Although the project is not quite documented 😶)

Thank you!
