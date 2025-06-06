<h1 align="center">Gamer Guild API</h1>

The [Gamer Guild API](https://gamer-guild-api.onrender.com) was created to serve the [Gamer Guild](https://gamer-guild.onrender.com) React app. The API includes the following apps, allowing for a rich database and a versatile front-end application:
- profiles
- followers
- posts
- likes
- comments
- events
- replies
- polls (this model could ultimately not be implemented on the front-end)

## __User Experience (UX)__

### ***User stories***

- In order to fulfill the [User Stories](https://github.com/users/AlexaH88/projects/5) created for this portfolio project, relevant apps and models were created. The following user stories relied on the API specifically:
  ![API User Stories](./docs/readme/images/ux/user_stories.png)

### ***Entity Relationship Diagram***

- The following Entity Relationship Diagram was created to show the models used. The in-built Django User model was used for this project, and the following custom models were created:
  - Profile
  - Follower
  - Post
  - Like
  - Comment
  - Event
  - Reply
  - Poll (this model could ultimately not be implemented on the front-end)

-   Entity Relationship Diagram:
    ![Entity Relationship Diagram](./docs/readme/images/ux/entity_relationship_diagram.png)

## __Technologies Used__

### ***Languages Used***

-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### ***Frameworks, Libraries & Programs Used***
1. [Django:](https://www.djangoproject.com/)
    - Django was used to create the web application.

1. [Django Rest Framework:](https://www.django-rest-framework.org/)
    - The Django rest framework was used to simplify the process between the back and front ends.

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

- Screenshots are provided for the Profiles app, testing was carried out equally for all other apps, and is noted below. 

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

#### **Followers App**
- List View (Read, Create if logged in)
- List View (Read if not logged in)
- Detail View (Read, Delete if owner)
- Detail View (Read if not owner)
- Detail View (Read if not logged in)

#### **Posts App**
- List View (Read, Create if logged in)
- List View (Read if not logged in)
- Detail View (Read, Update, Delete if owner)
- Detail View (Read if not owner)
- Detail View (Read if not logged in)

#### **Likes App**
- List View (Read, Create if logged in)
- List View (Read if not logged in)
- Detail View (Read, Delete if owner)
- Detail View (Read if not owner)
- Detail View (Read if not logged in)

#### **Comments App**
- List View (Read, Create if logged in)
- List View (Read if not logged in)
- Detail View (Read, Update, Delete if owner)
- Detail View (Read if not owner)
- Detail View (Read if not logged in)

#### **Events App**
- List View (Read, Create if logged in)
- List View (Read if not logged in)
- Detail View (Read, Update, Delete if owner)
- Detail View (Read if not owner)
- Detail View (Read if not logged in)

#### **Replies App**
- List View (Read, Create if logged in)
- List View (Read if not logged in)
- Detail View (Read, Delete if owner)
- Detail View (Read if not owner)
- Detail View (Read if not logged in)

#### **Polls App**
- List View (Read, Create if logged in)
- List View (Read if not logged in)
- Detail View (Read, Update, Delete if owner)
- Detail View (Read if not owner)
- Detail View (Read if not logged in)

### ***Fixed Bugs***

#### Event Date Bug:
- When editing an event on the front-end app via the EventEditForm the date field was not populated with the existing date previously created by the user via the EventCreateForm. 

- On further inspection in the console, this error was caused by the date format not being the same as the form required, as I had applied a DATE_FORMAT in the back-end API settings to make the date more human-friendly and readable e.g. 01/05/2023. 
![Event Dates Bug](./docs/readme/images/testing/bug_date_events.png)

- As [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/date) states, this format comes from the browser and can not be changed. 

- In order to avoid this issue, the date format was reverted to the required `yyyy-MM-dd` format. As a future implementation, a workaround could be to convert the format from one to the other with JavaScript as required.

#### Database Bugs:
- I had recurring bugs with my database, with there being a disconnect between the migrated models and existing data in the database.

- As an example, I would get a ProgrammingError, saying that `content` on `polls` didn't exist:
![Programming Error Bug](./docs/readme/images/testing/bug_programming_error.png)

- However, when checking the database, the `content` field on `polls` did indeed exist:
![Database Existing Fields](./docs/readme/images/testing/bug_exisitng_fields.png)

- The solution ultimately was to either reset the database on [Elephant SQL](https://www.elephantsql.com/) or delete it entirely, create a new instance and connect it up to the API via env.py and Heroku config vars. Followed by migrating all the models again, and deploying to Heroku. 

- This re-ocurring issue caused a lot of time to be wasted both on having to reset the database and recreate the lost data.

### ***Known Bugs***

#### Default Image Bug
- When creating an event there is an error on the front-end regarding the default image. When a user tries to create an event but doesn't upload an image, the default image specified on the back-end should apply. However, the form throws an error:
    ![Default Image Bug Front End](/docs/readme/images/testing/bug_default_image_front_end.png)

- However, this error doesn't occur on the back-end and the default image is applied without issue:
    ![Default Image Bug Back End](/docs/readme/images/testing/bug_default_image_back_end.png)

- Despite using the identical code as on the Moments Walkthrough on posts, checking that Cloudinary was connected up properly, searching on Google and Slack, and asking tutor support, no solution was found.

- The workaround was to include an image required info text on the form to ensure users would always select an image.

#### Poll and Discussion Bug
- A poll and discussion model were created on the back-end to be used with events. Though the back-end functionality exists and doesn't cause any issues, the front-end functionality was impossible to implement. My assumption was that the choice fields on polls was causing an issue and that my front-end code was not correct. However, when implementing the discussion on events, which is identical to comments on posts, the same error appeared and nothing could be done about it.

- Recurring front-end TypeError:
    ![Poll Bug Error](/docs/readme/images/testing/bug_poll_error.png)

- Front-end displaying data correctly when created in the back-end:
    ![Poll Bug Back End Data](/docs/readme/images/testing/bug_poll_back_end_data.png)

- Ability to create the data in the back-end: 
    ![Poll Bug Back End Functionality](/docs/readme/images/testing/bug_poll_back_end_functionality.png)

- Ultimately the poll and discussion functionality was therefore removed.

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

- And last but not least, my husband [Antoine Masson](https://www.linkedin.com/in/antoine-masson-55b65094/) for helping me through the stressful moments and for supporting us financially while I make this big career change. 
