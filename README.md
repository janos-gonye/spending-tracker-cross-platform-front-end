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

<hr>
<br>

*Thanks for reading,*  
*Johnny*
