# snaphabit

## Build Instructions
1. Install Python 3 (>= 3.8.1)
2. Use pip to setup virtual enviroment `python3 -m venv env`
3. Download dependencies using pip: `pip install -r requirements.txt`

## Executing the program
### Standalone Verison
The standalone program (CLI version) is in `main.py`.  
You can run the standalone program by calling `python3 ./main.py ./pathToInputFile.ics 6/14 outputFilename.ics`  
The first argument is the path to the ICS file, the second argument is the initial shift date in MM/DD format.  
The third argument is optional and is used to specify the filename of the resulting ICS file (default = out.ics).  

### Server Version
The program can also be interfaced through a web app through the `server.py` file.  
To launch the server, execute `python3 ./server.py`.  
Launch your browser to `localhost`. By default it runs on port 80.  

## Further notes
Although the script runs fine, there is scope for further improvement.  
For example:  
- Implement proper error checking outside args length (i.e. check if file exists)
- More test cases to ensure reliability
- Optimizations on the web app portion to ensure performance & scalability
- Refactor code for readability
