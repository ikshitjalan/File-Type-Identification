import unittest
from classOutput import Output
import csv
import pandas as pd
# import time

#STEP 1:
      #-> comment the object in classOutput file to test methods
#STEP 2:
      #-> run python script in cli
#STEP 3:
      #custon input->  binaryTree.cpp,output1.a$,ml.r,roman.php,avc.c  ->to clear tests
      
#Test class for classOutput class
class TestOutput(unittest.TestCase):

    #Method run implicitly before every unit test method
    def setUp(self):
        self.obj = Output() #Create obj of classOutput
        self.expected = ['Title : .cpp', 'Title : .r', 'Title : .PHP', 'Type :  PHP File']
        self.extList = ['.cpp', '.a$', '.r', '.php', '.c']
        self.fileNames = ['binaryTree.cpp','output1.a$','ml.r','roman.php','avc.c']

    #Test for input fileNames 
    def test_takeInput(self):
        self.obj.takeInput() #input-> binaryTree.cpp,output1.a$,ml.r,roman.php,avc.c  -->to clear test
        self.assertEqual(self.obj.fileNames,self.fileNames)

    #Test for write fileNames in 'input.csv'
    def test_writeFile(self):
        self.obj.writeFile()
        dataframe = pd.read_csv('input.csv',encoding='mac_roman')
        extensions = []
        for i,file in enumerate(dataframe['file_name']):
            extensions.append(file)
        self.assertEqual(extensions,self.fileNames) #Extensions written in input.csv check

    #Test for read fileNames from 'input.csv' created above
    def test_readFile(self):
        self.obj.readFile()
        self.assertEqual(len(self.obj.data),1253) #No of rows in DFileIdentification.csv check
        self.assertEqual(len(self.obj.data.columns),6) #No of columns in DFileIdentification.csv check
        self.assertEqual(self.obj.data.iloc[0]['Title'],".lgo") #First extension in DFileIdentification.csv check
        self.assertEqual(self.obj.data.iloc[617]['Title'],".rise") #Random extension in DFileIdentification.csv check
        self.assertEqual(self.obj.data.iloc[1252]['Title'],".XAML") #Last extension in DFileIdentification.csv check
        extensionsList = []
        for ext in self.obj.fileNames:
            extensionsList.append('.'+ext.split('.')[1])
        self.assertEqual(extensionsList,self.extList) #Extensions read from input.csv check

    #Test for each extension's input expression 
    def test_check(self):
        self.assertEqual(self.obj.check('cpp'),1) #Extension expression valid check
        self.assertEqual(self.obj.check('cp.p'),0) #Extension expression invalid check
        self.assertEqual(self.obj.check('324'),0) #Extension expression invalid check
        self.assertEqual(self.obj.check('*a'),0) #Extension expression invalid check
        self.assertEqual(self.obj.check(''),0) #Extension expression invalid check

    #Test for searching file in 'DFileIdentification.csv'
    def test_searchFile(self):
        self.obj.searchFile()
        with open("output.txt", 'r+') as ans:
            linesToRead = [0,9,16,18]
            checkAns = []
            for position, line in enumerate(ans):
                if position in linesToRead:
                    checkAns.append(line.strip())
            self.assertEqual(checkAns,self.expected) #Output of extensions in output.txt check
            ans.close()
        
#Run script as main module
if __name__ == '__main__':
    unittest.main()
