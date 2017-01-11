#simplejson
#pulp

#Read The Files
from File_Reader import *
txtfile=Get1TxtFileData("Customer_Map_For_1_Sitter_in_HTML.txt")
linedata = txtfile.readandreturnlist()

#Parse and Return Lat Long
from File_Parser import *
parsing = FileParse(linedata)
locations = parsing.latlon()

#Locations -> Google Api -> Distance Matrix
from distancematrixmaker import *
matrix = matrixmaker(locations)
distancematrix = matrix.matrix()


#Executor
from tspsolver import *
entered = tspsolve(distancematrix)
print entered.runtsp()
