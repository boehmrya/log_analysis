# Udacity Project 3: Logs Analysis
This project reports three different statistics from the news database.  First, it prints out the top three articles by number of views.  Second, it outputs the top three authors by number of views.  Third, it prints out days on which more than one percent of requests led to errors.  For each statistic, there are two corresponding functions, one that fetches the records from the database, and another that prints out the results in an appropriate, formatted manner.  Finally, a main function runs all three output functions.

## Usage
Install VirtualBox - https://www.virtualbox.org/wiki/Downloads
Install Vagrant - https://www.vagrantup.com/downloads.html
Run `vagrant up` from inside the vagrant subdirectory to build the environment
Run  `psql -d news -f newsdata.sql` from inside the vagrant subdirectory to import the news database
Run `python logAnalysis.py` to run the report and output the statistics. Each stat will be separated by a line break.

## Dependencies
* VirtualBox
* vagrant
* PostgreSQL
* psycopg2
