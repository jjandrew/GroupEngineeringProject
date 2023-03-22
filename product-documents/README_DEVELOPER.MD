# How to onboard for developers

## Requirements

In order to run the project all libraries, modules, and packages in the requirements.txt file need to be installed.

- This can be done from the base directory (the directory containing manage.py) using the command:
  - pip install -r requirements.txt

## Product Documents

This section of the project contains all of the design choices and reasoning for the project as well as the location of the buildings around campus. \
\
UML Diagrams for the models used throughout the project are also given here.

## Technical Documets

The technical documents are split into 4 sections:

- source-code
- static
- templates
- database.sql

### When first running the app:

To create a new gamekeeper go to /admin
Create an account in user's to be the gamekeeper
Create two groups: Gamekeeper and user

In python manage.py shell:

- from accounts.models import CustomUser
- from django.contrib.auth.models import Group
- user = CustomUser.objects.get(username='\<GameKeeperUsername>')
- user_group = Group.objects.get(name="Gamekeeper")
- user_group.user_set.add(user)

### source-code

This contains the code for the project. It has been created using the django framework with the core application being called "myapp".

#### myapp

This section of the project contains the settings.py, urls.py and views.py.

- settings.py
  - The INSTALLED_APPS section of this project contains the current apps that have been added. These include:
    - location
    - accounts
    - loginApp
    - submission
  - The ROOT_URLCONF constant defines where the base urls are searched for.
  - The TEMPLATES constant defines the directory to search for the templates in.
  - The DATABASES constant states what to call the database and where to store it in the NAME section.
  - The static files directory can be changed in the STATICFILES_DIRS constant. This is where the constant photos and css for use in the application can be found.
  - The MEDIA_URL states where to place the submitted photos in the application and will be where gamekeepers will validate photos from.
  - Several email constants are also defined here for use in sending emails if a user forgets their password.
- urls.py
  - States the URLs for each of the applications in the project.

#### accounts

This app is used to define the custom user model for use throughout the program.
The abnormal attributes of this model include:

- is_mod
  - Defines if a user is a moderator (game keeper)
- points
  - The number of points a user has (for displaying on leaderboard)
- email
  - Used to verify a player is who they say they are.

Tests are carried out on this user model in the tests.py file.

#### leaderboard

This is the application that ranks users based on score and buildings based on carbon footprint. \
The application sends the users returned from the database to the leaderboard UI and handles errors if less than 4 users are entered.

#### location

Currently does nothing

#### loginApp

Logs in and logs out a user in the views.py section. Also gives a user the option to sign up if a POST request is not sent which will forward them to the registration page. \
The form for logging in can be located in the forms.py section of this app.

#### signUp

A new user will be created in the views.py file. This uses the form found in forms.py and will perform a variety of checks on the data entered to make sure a user has a unique email, username and password is valid.

#### submission

This will be where a user can submit a photo of a room along with data about the room to calculate carbon statistics for a bulding. \
The form used for submission is located in forms.py and the information of these submissions will be stored in the database.

### static

This section of the project is split into css and images directories for use in the templates.

### templates

The templates that were used for the UI of the project. These are stored in the UI section of the templates tab and are named according to the application which the display.

### database.sql

This is an empty database which displays the format of the database created when the code "python technical-documnets/source-code/manage.py migrate" is run. \
This code will create a database using the models entered when executed from the base directory.

## Testing

Unit tests are entered in each of the applications tests.py file where applicable. \
To run the tests the command: ""python technical-documnets/source-code/manage.py test" can be run from the base directory.
