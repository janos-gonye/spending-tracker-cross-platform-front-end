# Spending Tracker Cross Platform Front End

This small application written in [Python](https://python.org) and [Kivy](https://kivy.org) aims to help you **track your expenses**.
You can clone it, build your instance for many platforms [supported by Kivy](https://kivy.org/#download), and you will be able to track your expenses *with no corporation monitoring your outgoings*.

> You find the related back-end application [here](https://github.com/janos-gonye/spending-tracker-api).

### What to use it for:
- Create an arbitrary number of categories and subcategories.
- Add transactions of the expense categories.
- Merge categories.
- List transactions by category.
- Show statistics and export them, which sent automatically to your registered email address.
- Users can register by email address. So your friends, relatives, and loved ones can use it, too.

## Setup for development

Navigate to the directory where you would like to store the application
```bash
cd /<path>/<to>/<your>/<projects>/<directory>
```

Clone the project  
'spending-tracker-cross-platform-front-end'
```bash
git clone https://github.com/janos-gonye/spending-tracker-cross-platform-front-end.git
cd ./spending-tracker-cross-platform-front-end
```

Create and activate your virtual environment  
*Only works with Python 3...*
```bash
sudo apt-get install virtualenv
virtualenv -p python3 venv
source ./venv/bin/activate
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
The first time you run the application, you need to configure to which server to connect.
You can achieve this by navigating to the *Settings*, selecting the *protocol* and setting the *host name* and *port* input fields.

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
