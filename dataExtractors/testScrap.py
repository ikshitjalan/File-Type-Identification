#libraries needed for this file
import unittest
from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq  
import csv
from scrapClass import *
import pandas as pd

#This is the main class which contains the set up method along with different testing functions
class Test(unittest.TestCase):
    @classmethod
    #setUp phase where initially the object is created and all the data is made ready for testing.
    def setUpClass(self): 
        self.obj=Scrap()
        self.pageSoup_fileinfo=self.obj.soupFromUrl1()
        self.pageSoup_reviver=self.obj.soupFromUrl2()
        self.pageSoup_openwith=self.obj.soupFromUrl3()
        self.pageSoup_dotwhat=self.obj.soupFromUrl4()
        self.dataframe = pd.read_csv('DFileIdentification.csv',encoding='mac_roman')

    #Here we have tested the expected "TITLE" of the website we scraped from.
    def test_titleText(self):
         pageTitle_reviver = self.pageSoup_reviver.find('title').get_text()
         pageTitle_fileinfo = self.pageSoup_fileinfo.find('title').get_text()
         pageTitle_openwith = self.pageSoup_openwith.find('title').get_text().strip()
         pageTitle_dotwhat = self.pageSoup_dotwhat.find('title').get_text().strip()
         self.assertEqual('Developer File Extensions - Listing of software development files', pageTitle_dotwhat)
         self.assertEqual('Source Code', pageTitle_openwith)
         self.assertEqual('Developer File Formats', pageTitle_fileinfo)
         self.assertEqual('File Extensions Starting with A', pageTitle_reviver)
    
    #Here we have tested the expected any in between content in the respective website
    def test_contentExists(self):
         content_reviver = self.pageSoup_reviver.find("h1",{"class":"char"}).text
         content_fileinfo = self.pageSoup_fileinfo.find("h2",{"class":"circle"}).text.strip()
         content_openwith = self.pageSoup_openwith.find("span",{"id":"logo"}).text.strip()
         content_dotwhat = self.pageSoup_dotwhat.find("div",{"class":"popUpHead"}).h1.text.strip()
         self.assertEqual('DEVELOPER FILES',content_dotwhat)
         self.assertEqual('OpenWith.org',content_openwith)
         self.assertEqual('Developer Files',content_fileinfo)
         self.assertEqual('A',content_reviver)
    
    #Here we have tested the different row titles from the csv file to check if the file has been correctly written     
    def test_rowsData_reviver(self):
         self.assertEqual(len(self.obj.table_rows_2),174)
         self.assertEqual(self.dataframe["Title"][877].strip(),".a")
         self.assertEqual(self.dataframe["Title"][923].strip(),".acf")
         self.assertEqual(self.dataframe["Title"][1051].strip(),".azz")
    
    #Here we have tested the different row titles from the csv file to check if the file has been correctly written     
    def test_rowsData_fileinfo(self):
         self.assertEqual(len(self.obj.table_rows_1),877)
         self.assertEqual(self.dataframe["Title"][0].strip(),".lgo")
         self.assertEqual(self.dataframe["Title"][200].strip(),".rdlc")
         self.assertEqual(self.dataframe["Title"][470].strip(),".defs")
         self.assertEqual(self.dataframe["Title"][776].strip(),".td")
    
    #Here we have tested the different row titles from the csv file to check if the file has been correctly written      
    def test_csvData_openwith(self):
         self.assertEqual(len(self.obj.table_rows_3),33)
         self.assertEqual(self.dataframe["Title"][1223].strip(),".CS")
         self.assertEqual(self.dataframe["Title"][1231].strip(),".PL")
         self.assertEqual(self.dataframe["Title"][1237].strip(),".ASP")
         self.assertEqual(self.dataframe["Title"][1252].strip(),".XAML")
    
    #Here we have tested the different row titles from the csv file to check if the file has been correctly written          
    def test_csvdata_dotwhat(self):
         self.assertEqual(len(self.obj.table_rows_4),168)
         self.assertEqual(self.dataframe["Title"][1052].strip(),".CS")
         self.assertEqual(self.dataframe["Title"][1073].strip(),".ASMX")
         self.assertEqual(self.dataframe["Title"][1106].strip(),".FPA")
         self.assertEqual(self.dataframe["Title"][1175].strip(),".QX")
       
#unittest.main() creates a new TestProgram object, whose initializer then goes ahead and runs the unit tests.
if __name__ == '__main__':
   unittest.main()