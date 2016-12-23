# TSP
=========================
Project Summary Statement
=========================
This project was done to provide a solution to optimize the routes of a single pet sitter going to several pet sit locations.

========================
Requirements
========================
Python Version: Python v 2.7

Modules to install:
  PuLP
  urllib
  simplejson
  ssl
  math
  json
  csv
  time
  timeit

Other:
A google api key

========================
The Steps of the Process
========================
1. LeashTime provided map data of a single pet sitters locations in a text document in html format.
2. The html is parsed and lat_long coordinates are returned off all the necessary locations
3. Google Distance Matrix API is used to provide a complete distance matrix
4. The distance matrix is then passed through a route optimization algorithm which was created utilizing PuLP (a Linear Programming Solver)

================================
An In Depth Look Inside The Code
================================
- ["Main"] 
The Main runs 4 separated task files, this section will provide an indepth explaination of what happens inside of each of the files.

- ["File_Reader"]
This file provides two methods of file reading
  1. Method 1 is just a call to read the lines of a file
  2. Method 2 is to find files with a specified type within the current directory

- ["File_Parser"]
This file parses out the lat_long coordinates from "Customer_Map_For_1_Sitter_in_HTML.txt"
The txt document was created from a html document that was provided by LeashTime. LeashTime is a pet sitting management app for pet sitting services and it can be found here: https://leashtime.com/info/?q=node/22
The html file contains information about several different locations for different pet sitters, due to the limitation of google distance matrix api only the first 10 locations were taken. A complete distance matrix for 10 locations is 100 routes which is 100 elements which is the limit of one request from the api without being charged.

