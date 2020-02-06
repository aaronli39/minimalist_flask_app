# minimalist_flask_app
This repository mimics the Flask setup I was taught to use, and I think is the most clear way of learning Flask. The bare minimum to run this Flask app would be just to have `app.py` and run the commands below. The folders exist just for reference.

# Setup
I was taught to use virtual environments so that we can install Flask to these environments and not worry about
updating files and having incompatibility issues. Assuming python3 is installed:
* `sudo apt install python3-pip`
* `sudo apt install python3-venv` installs the virtual environment package
* `python3 -m venv ~/venv` This creates a virtual environment directory located in the home folder called venv
* `. ~/venv/bin/activate` activates the virtual environment
* `pip install wheel` installs wheel
* `pip install Flask` installs Flask. You would pip install any other required packages: such as requests, etc
* Now, you can go into this cloned repository, and run `python app.py` which will run the app on the local server and you can see the debugging. `python3 app.py` may be needed if the first command doesnt work.
