# APIexample
A simple API server written in bottle that shows GET and POST requests, and a client that interacts with it. 

## Usage
To use, run the server.py file with Python 3. The syscollector.py can be run in either Python 2 or 3, but requires you to change the url to wherever the server is being hosted otherwise it will give errors. To make it easer to tell the difference between multiple tests sent on a single machine, syscollector.py also prompts for a message to send along with the system information.

## Technologies used
The bottle framework is used to create the server. The database is made in SQLite. Data is collected using the process module. While the requests package would have been much easier to implement the post request in syscollector.py, I instead chose to not assume anything about the machine it is being run on and opted to use only the standard libraries of http and urllib. 
