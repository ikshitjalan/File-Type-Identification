import pandas as pd
import csv
import re

# Output class for searching each extension provided by input and result in output.txt
class Output:

    # Method which will run everytime while creating a new object
    def __init__(self):
        self.fileNames = ['binaryTree.cpp','output1.a$','ml.r','roman.php','avc.c'] #static input
        self.data= pd.DataFrame() 
        self.extensionsInput=[] 
        self.fileExtensions = 'DFileIdentification.csv'  # Dataset


    # Take input from user and print it on console
    def takeInput(self):
        self.fileNames = []
        inputString = input("Enter a list of filenames separated by comma \n (For eg:- file1.php , file2.r , file3.cpp):-")
        print("\n")
        self.fileNames = inputString.split(',')
        print("user list of filenames is", self.fileNames)

    # Write input data into "input.csv" file
    def writeFile(self):
        with open ("input.csv","w+") as inputData:
            writer = csv.writer(inputData)
            writer.writerow(["file_name"])
            for file in self.fileNames:
                writer.writerow([file])

    # Read input.csv file and store all extensions into "extensionsInput" list
    def readFile(self):
        self.data=pd.read_csv(self.fileExtensions,encoding='mac_roman')
        inputData =pd.read_csv('input.csv')
        inputList=inputData['file_name'].tolist()

        for i in inputList:
            self.extensionsInput.append('.'+i.split('.')[1])

    # Check each extension format is valid or not
    def check(self,extension):
        regexp = re.compile('[^0-9a-zA-Z]+')
        if extension.isdecimal():       # Contains only numbers or not
            return 0
        elif regexp.search(extension):  # Contains any special symbol or not
            return 0
        elif len(extension)==0:         # Contains any letter or not
            return 0
        else:
            return 1

    # Search each extension in dataset and write its information in "output.txt" file
    def searchFile(self):
        self.writeFile()
        self.readFile()
        self.f = open("output.txt", "w")  # Output file
        myData = dict()
        myData=self.data.to_dict(orient='records')    # Converting whole data to list of dictionaries
        for i in self.extensionsInput:
            if self.check(i[1:]):
                for j in range(len(myData)):
                    if myData[j]["Title"].lower()==i:
                        for key,value in myData[j].items():
                            self.f.write(key+ " : " + value + "\n")   # Writing into "output.txt" file
                        self.f.write("\n")
                        break
                    else:
                        if j==len(myData)-1:
                            self.f.write("Extension not found in data"+"\n"+"\n")    # If extension is not found in data
            else :
                self.f.write("Not valid extension!"+"\n"+"\n")                       # If extension is not valid
        self.f.close() #Close output file
#Uncomment the below code to run the script       
# obj = Output()
# obj.takeInput()
# obj.searchFile()




