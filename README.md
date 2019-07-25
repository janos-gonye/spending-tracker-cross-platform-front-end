# Spending Tracker Cross Platform Front End

This small application written in [Python](https://python.org) and [Kivy](https://kivy.org) helps you **track your expenses**.
You can clone it, build your own instance for many platforms [supported by Kivy](https://kivy.org/#download) and you'll be able to track your expenses *without any major (or minor) company monitoring what you spend your money on*.

> You can find the corresponding back end application [here](https://github.com/janos-gonye/spending-tracker-api).

#### What you can do with it
 - Create categories and subcategories of any category.
 - Add transactions to categories.
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

## Setup for development on Windows
> Coming soon...


## Configuration
First time you run the application, you need to configure which server to connect to.  
You can do this by navigating to the *Settings*, selecting the *protocol* and setting the *host name* and *port* input fields.

## Pictures from the application
> Coming soon...  
> New style is comming soon...


<hr>
<br>

*Thanks for reading,*  
*Johnny*
