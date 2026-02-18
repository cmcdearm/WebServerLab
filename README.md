# WebServerLab
learning the basics of socket programming for TCP connections in Python 

### Project Overview
This project implements a simple HTTP web server in Python, it supports:
* serving static HTML files
* returning 404 for missing files
  
### File Structure 
WebServerLab

│

├── WebServer.py          # Original HTTP server implementation

├── WebServer_Multi.py    # Multithreaded HTTP server implementation

├── HelloWorld.html       # Example HTML file to serve

└── README.md             # Project documentation

### Environment Info
Python version: Python 3.10+
Tested on: Linux (Ubuntu)
Uses only standard Python libraries:
* socket
* threading
* sys

No external dependencies required.
If you’re on macOS or Windows, adjust accordingly.

### How to Run the Server
```
python WebServer.py
```
The terminal should display
'Ready to serve...'
opening a browser on the same machine, you can visit:
http://127.0.0.1:6789/HelloWorld.html

### Testing 404 Response
To test error handling, request a file that does not exist:
http://127.0.0.1:6789/SuperRealFile.html

The server will respond with 
'404 Not Found'

### Multithreading Design
For the Multithreading version of the web server, we use Python's `threading` module.
* The main thread will listen for incoming TCP connections
* Each client's connection is handled in a separate thread
* Each request/response pair uses its own TCP connection
With this, we can handle multiple clients simultaneously.
