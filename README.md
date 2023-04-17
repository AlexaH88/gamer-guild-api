<h1 align="center">Gamer Guild API</h1>

The Gamer Guild API was created to serve the [Gamer Guild](https://github.com/AlexaH88/gamer-guild) React app. The API includes the following apps, allowing for a rich database and a versatile front-end application:
- profiles
- followers
- chats
- posts
- events
- responses
- comments
- likes
- attends

## __User Experience (UX)__

### ***User stories***

- In order to fulfill the [User Stories](https://github.com/users/AlexaH88/projects/5) created for this portfolio project, relevant apps and models were created. The following user stories relied on the API specifically:
  ![API User Stories](./docs/readme/images/ux/user_stories.png)

### ***Entity Relationship Diagram***

- The following Entity Relationship Diagram was created to show the models used. The in-built Django User model was used for this project, and the following custom models were created:
  - Profile
  - Follower
  - Chat
  - Post
  - Event
  - Response
  - Comment
  - Like
  - Attend

-   Entity Relationship Diagram:
    ![Entity Relationship Diagram](./docs/readme/images/ux/entity_relationship_diagram.png)


## __Technologies Used__

### ***Languages Used***

-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### ***Frameworks, Libraries & Programs Used***

1. [Django Rest Framework:](https://www.django-rest-framework.org/)
    - The Django web framework was used to create the web API.

1. [PostgreSQL:](https://en.wikipedia.org/wiki/PostgreSQL)
    - PostgreSQL was used as the object-relational database system.

1. [ElephantSQL:](https://www.elephantsql.com/)
    - ElephantSQL was used to host the database.

1. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.

1. [Heroku:](https://heroku.com/)
    - Heroku was used for the deployed application.


## __Testing__

### ***Python Testing***

-   [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code in this project. All code passed without errors, except `settings.py` and `env.py` which showed E501 'line too long' warnings.
    ![Results settings.py](./docs/readme/images/testing/python_testing_error_settings.png)
    ![Results env.py](./docs/readme/images/testing/python_testing_error_env.png)

### ***Manual Testing***

- Manual testing was performed throughout development, ensuring the database was being updated as expected when creating, reading, updating or deleting data, where appropriate.

#### **Attendees App**
- List View (Read, Create if logged in):
    ![List View](./docs/readme/images/testing/manual_testing_attendees_list_logged_in.png)
- List View (Read if not logged in):
    ![List View](./docs/readme/images/testing/manual_testing_attendees_list_not_logged_in.png)
- Detail View (Read, Delete if owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_attendees_detail_owner.png)
- Detail View (Read if not owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_attendees_detail_not_owner.png)
- Detail View (Read if not logged in):
    ![Detail View](./docs/readme/images/testing/manual_testing_attendees_detail_not_logged_in.png)
#### **Chats App**
<!-- - List View (Read if logged in):
    ![List View](./docs/readme/images/testing/manual_testing_profiles_list_logged_in.png)
- List View (Read if not logged in):
    ![List View](./docs/readme/images/testing/manual_testing_profiles_list_not_logged_in.png)
- Detail View (Read, Update, Delete if owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_profiles_detail_owner.png)
- Detail View (Read if not owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_profiles_detail_not_owner.png) -->
<!-- - Detail View (Read if not logged in):
    ![Detail View](./docs/readme/images/testing/manual_testing_attendees_detail_not_logged_in.png) -->
#### **Comments App**
- List View (Read, Create if logged in):
    ![List View](./docs/readme/images/testing/manual_testing_comments_list_logged_in.png)
- List View (Read if not logged in):
    ![List View](./docs/readme/images/testing/manual_testing_comments_list_not_logged_in.png)
- Detail View (Read, Update, Delete if owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_comments_detail_owner.png)
- Detail View (Read if not owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_comments_detail_not_owner.png)
- Detail View (Read if not logged in):
    ![Detail View](./docs/readme/images/testing/manual_testing_comments_detail_not_logged_in.png)
#### **Events App**
- List View (Read, Create if logged in):
    ![List View](./docs/readme/images/testing/manual_testing_events_list_logged_in.png)
- List View (Read if not logged in):
    ![List View](./docs/readme/images/testing/manual_testing_events_list_not_logged_in.png)
- Detail View (Read, Update, Delete if owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_events_detail_owner.png)
- Detail View (Read if not owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_events_detail_not_owner.png)
- Detail View (Read if not logged in):
    ![Detail View](./docs/readme/images/testing/manual_testing_events_detail_not_logged_in.png)
#### **Followers App**
- List View (Read, Create if logged in):
    ![List View](./docs/readme/images/testing/manual_testing_followers_list_logged_in.png)
- List View (Read if not logged in):
    ![List View](./docs/readme/images/testing/manual_testing_followers_list_not_logged_in.png)
- Detail View (Read, Delete if owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_followers_detail_owner.png)
- Detail View (Read if not owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_followers_detail_not_owner.png)
- Detail View (Read if not logged in):
    ![Detail View](./docs/readme/images/testing/manual_testing_followers_detail_not_logged_in.png)
#### **Likes App**
- List View (Read, Create if logged in):
    ![List View](./docs/readme/images/testing/manual_testing_likes_list_logged_in.png)
- List View (Read if not logged in):
    ![List View](./docs/readme/images/testing/manual_testing_likes_list_not_logged_in.png)
- Detail View (Read, Delete if owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_likes_detail_owner.png)
- Detail View (Read if not owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_likes_detail_not_owner.png)
- Detail View (Read if not logged in):
    ![Detail View](./docs/readme/images/testing/manual_testing_likes_detail_not_logged_in.png)
#### **Posts App**
- List View (Read, Create if logged in):
    ![List View](./docs/readme/images/testing/manual_testing_posts_list_logged_in.png)
- List View (Read if not logged in):
    ![List View](./docs/readme/images/testing/manual_testing_posts_list_not_logged_in.png)
- Detail View (Read, Update, Delete if owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_posts_detail_owner.png)
- Detail View (Read if not owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_posts_detail_not_owner.png)
- Detail View (Read if not logged in):
    ![Detail View](./docs/readme/images/testing/manual_testing_posts_detail_not_logged_in.png)
#### **Profiles App**
- List View (Read if logged in):
    ![List View](./docs/readme/images/testing/manual_testing_profiles_list_logged_in.png)
- List View (Read if not logged in):
    ![List View](./docs/readme/images/testing/manual_testing_profiles_list_not_logged_in.png)
- Detail View (Read, Update if owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_profiles_detail_owner.png)
- Detail View (Read if not owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_profiles_detail_not_owner.png)
- Detail View (Read if not logged in):
    ![Detail View](./docs/readme/images/testing/manual_testing_profiles_detail_not_logged_in.png)
#### **Responses App**
<!-- - List View (Read, Create if logged in):
    ![List View](./docs/readme/images/testing/manual_testing_profiles_list_logged_in.png) -->
<!-- - List View (Read if not logged in):
    ![List View](./docs/readme/images/testing/manual_testing_responses_list_not_logged_in.png) -->
<!-- - Detail View (Read, Update, Delete if owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_profiles_detail_owner.png) -->
<!-- - Detail View (Read if not owner):
    ![Detail View](./docs/readme/images/testing/manual_testing_profiles_detail_not_owner.png) -->
<!-- - Detail View (Read if not logged in):
    ![Detail View](./docs/readme/images/testing/manual_testing_responses_detail_not_logged_in.png) -->

### ***Fixed Bugs***

-   #### Count Bug

	- The likes, comments, attending counts on the post and event detail view were showing up incorrectly. A newly created post or event would show several likes, comments and attendees despite the fact that the back-end database correctly showed 0, as did the PostsPages and EventsPages.
		- Detail View:
		![Detail View](./docs/readme/images/testing/bug_counts_detail_view.png)
    	- Database:
    	![Database](./docs/readme/images/testing/bug_counts_database.png)

	- This issue was fixed on the back-end by revising the EventDetail and PostDetail views to be specific to events and posts resepectively and not all the user's likes, comments etc.
		- Original Code:
    	![Original Code](./docs/readme/images/testing/bug_counts_original_code.png)
    	- Fixed Code:
    	![Fixed Code](./docs/readme/images/testing/bug_counts_fixed_code.png)

[//]: <> (Deployment section taken from Dave Horrocks, and credited in the Content section of the Credits)
## __Deployment__

### ***Heroku***

1. Navigate to your [Heroku dashboard](https://dashboard.heroku.com/apps)
2. Click "New" and select "Create new app".  
  ![New heroku](./docs/readme/images/deployment/heroku-new.png)
3. Input a meaningful name for your app and choose the region best suited to
  your location.  
  ![Create new app](./docs/readme/images/deployment/heroku-create.png)
4. Select "Settings" from the tabs.  
  ![Settings tab](./docs/readme/images/deployment/heroku-settings.png)
5. Click "Reveal Config Vars".  
 ![Config vars button](./docs/readme/images/deployment/heroku-config-vars.png)
6. Input all key-value pairs as necessary from the `.env` file. **Ensure DEBUG
   and DEVELOPMENT are not included**.
   ![Config vars](./docs/readme/images/deployment/heroku-config-var.png)
7. Click "Add buildpack".  
 ![Add buildpack](./docs/readme/images/deployment/heroku-add-buildpacks.png)
8. Add "python" from the list or search if necessary, remember to
 click save.  
 ![Select buildpacks](./docs/readme/images/deployment/heroku-select-buildpacks.png)
9. Select "Deploy" from the tabs.  
![Settings tab](./docs/readme/images/deployment/heroku-deploy-tab.png)
10. Select "GitHub - Connect to GitHub" from deployment methods.  
 ![Select GitHub](./docs/readme/images/deployment/heroku-select-github.png)
11. Click "Connect to GitHub" in the created section.  
 ![Connect to GitHub](./docs/readme/images/deployment/heroku-connect-github.png)
12. Search for the GitHub repository by name.  
13. Click to connect to the relevant repo.
14. Either click `Enable Automatic Deploys` for automatic deploys or `Deploy
 Branch` to deploy manually. Manually deployed branches will need
 re-deploying each time the repo is updated.  
 ![Heroku deploy branch](./docs/readme/images/deployment/heroku-deploy-branch.png)
15. Click `View` to view the deployed site.  
    ![Heroku view](./docs/readme/images/deployment/heroku-view.png)
16. The live site can also be accessed from your repo in GitHub from the
    environments section of the repo.

The site is now live and operational

## __Credits__

### ***Code***

- The following were used as references to help with writing the HTML, CSS, JavaScript and Python code:
  - [Code Institute LMS](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopmentadvancedfrontend), in particular the [Django Rest Framework Walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/f775d54df4da44d18309888b3fe884f7/bc5fbada70104d489aa0363a03d8bda8/)
  - [W3Schools](https://www.w3schools.com/) 
  - [Stack Overflow](https://stackoverflow.com/)
  - [MDN Web Docs](https://developer.mozilla.org/en-US/)
  - [Django Rest Framework Documentation](https://www.django-rest-framework.org/)

### ***Content***

- The Deployment section in the README was taken from the masterful [Dave Horrocks](https://github.com/DaveyJH), who put it so much better than I could! 

### ***Acknowledgements***

Massive thanks to: 

- My mentor, [Lauren-Nicole Popich](https://github.com/CluelessBiker), for guiding me and giving me helpful feedback and advice - and for giving me confidence when I didn't believe in myself!

- My fellow Code Institute students and friends for their help, generous feedback, and incredible knowledge:
  
  - [Abi Harrison](https://github.com/Abibubble)
  - [Dave Horrocks](https://github.com/DaveyJH)
  - [Emanuel Silva](https://github.com/manni8436)
  - [Kera Cudmore](https://github.com/kera-cudmore)
  - [Megan Vella](https://github.com/Medusas71)
  - [Monika Hrda](https://github.com/monika-hrda)
  - [Natalie Alexander](https://github.com/natalie-kate)
  - [Sandra Atino](https://github.com/Atinos31)
  - [Suzy Bennett](https://github.com/suzybee1987)

- Tutor Support, Student Care and the Slack Community at [Code Institute](https://codeinstitute.net/global/) for their support.

- And last but not least, my fiancé [Antoine Masson](https://www.linkedin.com/in/antoine-masson-55b65094/) for helping me through the stressful moments and for supporting us financially while I make this big career change. 
