## Problem Statement
Find the n most popular repositories of a given organization on Github (Eg:[https://github.com/google](https://github.com/google)) based on the number of forks. For each such repo find the top m committees and their commit counts.

**My Approach**

I have used the PyGithub package in python which essentially uses the Github API and Github Search API appropriately.

**Setting Up**

Create a virtual environment to avoid any dependency issues

    $ virtualenv --python=python3.6 venv
    $ source venv/bin/activate

Install the python package

    (venv)$ pip install PyGithub

Generate an OAuth token for your hithub account and insert it in line #4 in the code.

Run the program 

    (venv)$ python almabase.py

Enter the variables prompted accordingly. There might be a throttling issue if the requests go above the 5000 limit per hour. There might be a slight selay when the parameters m and n are higher.

The code is hosted at 
https://goutham8449.pythonanywhere.com/almabase/default/getCommittees/

sample request : 
https://goutham8449.pythonanywhere.com/almabase/default/getCommittees/?company_name=google&n=3&m=2
