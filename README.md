# Party Up!

Welcome to Party Up! 

Any gamer will tell you about the dangers of "solo queuing" and how quickly it can erode the ranks that you've diligently earned. We here at Party up want to remind you of something we all forgot a long time ago, before the COVID, before the internet, before God of War: Video games are better with your friends!

Enter Party Up! The one stop shop for :

* Meeting likeminded gamers and making friends
* Putting together crack squads to push the limits of your skill level and boost your ranking
* Trophy Hunting or Achievement Unlocking. Here you can team up and smash out those multiplayer goals with ease.
* Fun - so you don't want a new BFF, nor care about high-level gaming. That's alright. Here you can find other people who also just want to mess around

Party Up is a full-stack software development project that has been built using Django and Bootstrap frameworks, with additional HTML, CSS and JavaScript. 

You can visit the live website [here](https://partyupgaming.herokuapp.com/)

![Landing terminal screen](media/readme/amiresponsive.JPG)

# Contents

# UX

The project has been completed using the core UX design thinking principles to ensure an efficient and easy to use app was created that had a distinct purpose and provided satisfaction to users. The project was created mobile-first and agile practices were also followed.

## Strategy 


The primary goals of the website admins are:
- To create, update and delete Game posts and comments
- To be able to see view and delete the posts and comments of others.

The primary goals of the website users are: 
- To register for an account on the website. 
- To sign in and sign out of the website. 
- To connect with other users
- To View a list of all available game forums
- To enter each forum and see the all the posts created
- To view the details of each post and see any comments made on the post


## Structure
### Website pages
- The website currently has a landing page and 6 game pages but was built so that additional game pages can be created quickly.
- All pages extend the same base html file, so they have the same look.
- Pages are described below.

### Database
- The project uses a relational database (PostgreSQL)
- Data is handled by the application with Django

## Target Audience

The target audience of this website is any person who :

* enjoys online video games
* wants to meet other gamers and make friends
* is looking for a team mate for ranked play
* is looking for a team mate for trophy/achievement hunting


## User Stories

* As an unregistered user I can view each post on the website so that I can select one to read and decide whether to sign up
* As a user I can navigate intuitively so that I can view the desired content
* As a logged in user I can change the details on my profile page so that all my details and information are up to date
* As a logged in user I can view my profile page so that I can see my personal account details
* As an admin I can create, remove, update or delete posts so that I can ensure site content is relevant and inoffensive
* As an Admin I can log out of the admin panel so that I can disconnect from the website
* As an admin I can log in so that I can access the sites backend
* As a user I can access social media accounts connected to the website so that I may learn more about the company
* As a user I can quickly identify the purpose of the website from the landing page so that determine if the website is relevant to me
* As a registered user I can login and logout of my account so that I can access and keep secure my data
* As a registered user I can set a password so that so that my account is secure
* As a registered user I can request a new password in case I forget my own so that I can regain access to my account
* As a user I can contact the website so that I can provide feedback or present queries
* As an unregistered user I can create an account so that I can interact fully with the website
* As an unregistered user I can easily find the sign up page so that I can register and interact with the website
* As a user I can fill in my personal details on my account page so that I can auto populate forms with my information on the site
* As a registered user I can delete my account so that ensure my details are removed after I no longer want to use it
* As a registered user I can comment on posts so that I can connect with other gamers
* As a registered user I can delete my posts so that my post are no longer visible and I will receive no further messages
* As a registered user I can update my posts so that I can keep my posts relevant and up to date with information
* As a registered user I can create posts so that I can find other gamers who want to achieve the same things
* As a user I can easily see if I am logged in or not so that I can choose to login or logout depending on what I want to do

## Agile

An agile approach was used for creating this website. The project board can be found here: [Kanban](https://github.com/users/LordButley/projects/1/views/1)

Where possible I worked within sprints to achieve the goals set for that sprint. User stories were created along with a Kanban board. As this work has been largely completed alongside the day job and the family commitments, the sprints themselves had to be fluid. This resulted in the project loosely being contained with 4 sprints. Sprint 1 and 2 were more standard in that the MoSoCo importances were added to user stories and worked towards during a set length of time. These can be seen in the Kanban board. For sprints 3 and 4, they were more akin to actual sprinting where I was doing everything in all my free time to dash for the finish line.

## Skeleton

The project was created using a mobile first perspective and as such only mobile wireframes were created.

[Wireframes](media/readme/Wireframes.JPG) 

## Design

### Font

"Permanent Marker" font was used for the logo and main title as it characterises the playful yet impactful nature of the website. It was not however used for posts and comments due to it's less than perfect readability when smaller.
"Montserrat" was used for all post and comment text due to it's crisp readability.

### Colors

The website needed to be a blank slate as it needed to contain lots of different coloured icons for each game. This basically meant the background had to be white or black. However I decided on black with red highlighting as it suited the images more and is inline with the gaming industry standard of clean, impactful colours with high contrast.

# Features

## Existing Features

### Home page

![Homepage1](media/readme/homepage1.JPG)
![Homepage2](media/readme/homepage2.JPG)

The homepage consists of a brief introduction of the website followed by clickable tiles which take you to the individual game pages

### Navigation

![Navbar](media/readme/navbar.JPG)
![Footer](media/readme/footer.JPG)

The burger bar expands to reveal login capabilities as well as a drop down of all the available games. All user feedback responses are highlighted in crimson.
The footer icons open onto new tabs and direct to the relevant pages


### Game page

![Gamepage](media/readme/gamepage.JPG)

The game page shows a list of posts relating to that game. If you aren't logged in you will not be able to see the "Create new post" button. Likewise if you are not logged in or you did not create the initial post you will not see the edit and delete icons on each post.

### Post page

![Postpage](media/readme/postpage.JPG)

The post page shows the post content and a list of comments relating to it. If you aren't logged in you will not be able to see the "Create new comment" section. Likewise if you are not logged in or you did not create the initial post you will not see the delete icons on each post. There is no edit functionality for comments specifically in keeping with modern trends.


### Login / Logout / Register

![Login](media/readme/signin.JPG)
![Logout](media/readme/signout.JPG)
![Postpage](media/readme/register.JPG)

The login, logout and postpage section are all styled in the same crisp edgey way with a similarly sharp background.

### Feedback

Messages pop up with new posts and comments are created, updated (only posts) and deleted. Note there is no success message if you do not change page and you can instantly see the result such as when you post a comment.
There is also crimson colour feedback when you hover over an interactive element.

### Data and Database

The data base is split into 3 different models:

Game, Post and Comment

## Features to implement in the future

First I would target the Use stories that did not get completed:

* As a logged in user I can change the details on my profile page so that all my details and information are up to date
* As a logged in user I can view my profile page so that I can see my personal account details
* As a registered user I can set a password so that so that my account is secure
* As a registered user I can request a new password in case I forget my own so that I can regain access to my account
* As a user I can contact the website so that I can provide feedback or present queries
* As an unregistered user I can create an account so that I can interact fully with the website
* As an unregistered user I can easily find the sign up page so that I can register and interact with the website
* As a registered user I can delete my account so that ensure my details are removed after I no longer want to use it

## Technologies Used

 ### Languages Used:

 1. [Python](https://en.wikipedia.org/wiki/Python) 
      - Programming language providing content and logic of project

 2. [HTML](https://en.wikipedia.org/wiki/HTML) 
      - Programming language providing content and structure of website.

 3. [CSS](https://en.wikipedia.org/wiki/CSS) 
      - Programming language providing styling of website.

 4. [JavaScript](https://en.wikipedia.org/wiki/Javascript)
      - Programming language used for the functions and interactivity behind the quiz.
 
 ### Frameworks, Libraries & Programs Used:

    
 1. [GitPod](https://gitpod.io/)
    - IDE (Integrated Development Environment), for writing, editing and saving code.

 2. [GitHub](https://github.com/) 
    - Remote code repository.

 3. [Heroku](https://www.heroku.com/)
    - Cloud application platform used to host program

 5. Python Libraries:
    - os - Used to clear the terminal
    - time - Used for creating a timer
    - random - Used to randomise questions
    - prettytable - Used for the leaderboard
    - string - Used for capitalizing input to match that of the database
    - gspread and google.oauth2.service_account for linking google sheets

 6. [https://pep8ci.herokuapp.com/](https://pep8ci.herokuapp.com/)
    - PEP8 Validator used to check code for compliance

 7. [HTML Validator](https://validator.w3.org/nu/)

 8. [CSS Validator](https://jigsaw.w3.org/css-validator/validator)

## Testing

The testing process can be seen in the [TESTING.md](TESTING.md) document.

## Deployment

### Heroku
The site is hosted using Heroku, deployed directly from the master branch of GitHub. The deployed site will update automatically as new commits are pushed to the master branch.

#### How I deployed my project to Heroku.
To host on Heroku you must follow these steps:

#### Updating dependencies for Heroku deployment

1. Create a requirements.txt file in the home directory of project
2. In the terminal write : pip3 freeze > requirements.txt

#### Creating a Heroku App

Heroku was used to deploy the site and it was achieved by following the steps below:

Heroku was used to deploy the site and it was achieved by following the steps below:
  1.	Go to the Heroku's website.
  2.	Create an account if required or select log in.
  3.	From the Heroku dashboard, click on the “New” button in top righthand corner then "Create new app".
  4.	Enter a unique "App name" and "Choose a region" before clicking on "Create app".
  5.	Go to "Config Vars" under the "Settings" tab.
  6.	Click on "Reveals Config Vars" and enter the following information:
	      - CLOUDINARY_URL : add your cloudinary key here.
        - DATABASE_URL : add the url from postgres database.
        - SECRET_KEY = a secret key for your app.
        - PORT : 8000
        - DISABLE_COLLECTSTATIC = 1 during development (Remove when deploying production!)
  7.	Go to "Buildpacks" section and click "Add buildpack".
  8.	Select "/herokupython" and click "Save changes"

- Project Version Control – Git was used to control the versions of the project during development. Changes were added, committed, and saved using commands such as ‘git add .’ and ‘git commit’, and ‘git push’. Once changes had been committed, they were pushed and stored on the GitHub repository with the rest of the projects source code.

#### Deploy section

1. Click on Github under deployment method
2. Search for repository and then click on "connect"
3. Click on "Enable Automatic Deploys"

#### Forking a GitHub Repository
1. Login to GitHub.
2. Locate your desired repository.
3. Locate the fork option in the top-right hand corner of the repository page.    
4. You will be asked where you want to fork it to.

## Credits

### Code

I learned how to write this project using the code institute walk through projects and as such some of the code structuring may be similar.

### Thanks

- to tutor support at Code Institute. I have constantly found their positivity and genuine interest in helping resolve issues in my code a great help 
- to my partner who is always willing to test everything I create 