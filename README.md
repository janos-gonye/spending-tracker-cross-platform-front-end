# Spending Tracker Cross Platform Front End

This small application written in [Python](https://python.org) and [Kivy](https://kivy.org) helps you **track your expenses**.
You can clone it, build your own instance for many platforms [supported by Kivy](https://kivy.org/#download) and you'll be able to track your expenses *without any major (or minor) company monitoring what you spend your money on*.

> You can find the corresponding back end application [here](https://github.com/janos-gonye/spending-tracker-api).

#### What you can do with it
 - Create categories and subcategories of any category.
 - Add transactions to categories.
 - Merge categories into one another.
 - Show statistics and export it to JSON format which sent automatically to your registered email address.
 - Users can register by email address which must be confirmed. So your friends, family members or girlfriend can use it, too.

> *Please note, it's just a hobby project, not an enterprise application.*  
> *Though, I think you knew this... :-)*

## Setup for development on Ubuntu (basically any Linux)

Navigate to the directory you'd like to store the application in
```bash
cd /<path>/<to>/<your>/<projects>/<directory>
```

Clone the project  
Project name is optional. Default: 'spending-tracker-cross-platform-front-end'
```bash
git clone https://github.com/janos-gonye/spending-tracker-cross-platform-front-end.git <project-name>
cd ./<project-name>
```

Create and activate your virtual environment  
*Only works with Python 3...*
```bash
sudo apt-get install virtualenv
virtualenv -p python3 <virtual-environment-name>
source ./<virtual-environment-name>/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Run program
```bash
python ./app/main.py
```

## Configuration
First time you run the application, you need to configure which server to connect to.  
You can do this by navigating to the *Settings*, selecting the *protocol* and setting the *host name* and *port* input fields.

## Some Pictures from the application (some are out-of-date)
> New style is comming...  


![Login Screen](https://raw.githubusercontent.com/janos-gonye/spending-tracker-cross-platform-front-end/master/screenshots/login_screen.png) 
 
![Registration Screen](https://raw.githubusercontent.com/janos-gonye/spending-tracker-cross-platform-front-end/master/screenshots/registration_screen.png) 
 
![Settings Screen](https://raw.githubusercontent.com/janos-gonye/spending-tracker-cross-platform-front-end/master/screenshots/settings_screen.png) 
 
![Main Screen](https://raw.githubusercontent.com/janos-gonye/spending-tracker-cross-platform-front-end/master/screenshots/main_screen.png) 
 
![Category List Screen](https://raw.githubusercontent.com/janos-gonye/spending-tracker-cross-platform-front-end/master/screenshots/category_list_screen.png) 
 
![Create Category Screen](https://raw.githubusercontent.com/janos-gonye/spending-tracker-cross-platform-front-end/master/screenshots/create_category_screen.png) 
 
![Transaction List Screen](https://raw.githubusercontent.com/janos-gonye/spending-tracker-cross-platform-front-end/master/screenshots/transaction_list_screen.png) 
 
![Popup](https://raw.githubusercontent.com/janos-gonye/spending-tracker-cross-platform-front-end/master/screenshots/popup.png) 
 
![Statistics Screen](https://raw.githubusercontent.com/janos-gonye/spending-tracker-cross-platform-front-end/master/screenshots/statistics_screen.png)


<hr>
<br>

*Thanks for reading,*  
*Johnny*
