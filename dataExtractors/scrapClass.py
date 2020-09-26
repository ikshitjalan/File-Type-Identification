#libraries needed for this file
from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq  
import requests
import re
import numpy as np

#This is the main class which contains all the functions implemented for scrapping different websites.
class Scrap:
    #contructor to initialise the file and headers of the file
    def __init__(self):
        self.outFilename = "DfileIdentification.csv"
        self.headers =  "title,category,fileType,description,applications,reference \n"
        self.table_rows_1=[]
        self.table_rows_2=[]
        self.table_rows_3=[]
        self.table_rows_4=[]

    #function to retrieve the html page of the website "fileinfo" and to set the data of the html page into table_rows_1
    def soupFromUrl1(self):
        try:
            uClient = uReq("https://fileinfo.com/filetypes/developer-all")
            pageSoup = soup(uClient.read(), "html.parser")
            uClient.close()
            table = pageSoup.find("tbody")
            table_rows_1 = table.findAll("tr")
            self.table_rows_1=table_rows_1
            return pageSoup

        except requests.exceptions.RequestException as e:  
            raise SystemExit(e)
            
    #function to write data of "fileinfo" website into the csv file
    #Here firstly, opening the file
    #then writing the data into the file
    #and closing the file
    def writeData1(self):
        try:
            f = open(self.outFilename, "w",encoding="utf-8")
        except IOError:
            raise IOError(self.outFilename)


        f.write(self.headers)

        for row in self.table_rows_1:
            ref = "https://fileinfo.com/"+row.td.a.get('href')
            uInside = uReq(ref)
            pageInsideSoup = soup(uInside.read(),"html.parser")
            uInside.close()
            title = row.a.text
            trTags = row.findAll("td")
            fileType = trTags[1].text.strip()
            listCat = pageInsideSoup.select("tr td a")
            category = listCat[0].text.strip()
            desc = pageInsideSoup.find("div",{"class":"infoBox"}).p.text
            apps = pageInsideSoup.findAll("a",attrs = {"rel" : "nofollow","target" : "_blank"})
            applications = []
            for app in apps:
                applications.append(app.text)
            appColumn = '|'.join([str(elem) for elem in applications]) 
            if(len(appColumn)==0):
                appColumn = "Empty"
            f.write(title.lower() + ", " +category+", "+ fileType + ", " +desc.strip().replace(",", ".")+ ", " + appColumn.strip() +", " + ref +"\n")
        f.close()

    #function to retrieve the html page of the website "reviversoft" and to set the data of the html page into table_rows_2    
    def soupFromUrl2(self):
        try:
            uClient = uReq("https://www.reviversoft.com/file-extensions/?char=a")
            page_soup = soup(uClient.read(), "html.parser")
            uClient.close()
            table_rows = page_soup.find_all("li",{"class":"dll_li"})
            self.table_rows_2=table_rows
            return page_soup

        except requests.exceptions.RequestException as e:  
            raise SystemExit(e)

    #function to write data of "reviversoft" into the csv file
    #Here firstly, opening the file
    #then writing the data into the file
    #and closing the file
    def writeData2(self):
        try:
            f = open(self.outFilename, "a",encoding="utf-8")
        except IOError:
            raise IOError(self.outFilename)

        for row in self.table_rows_2:
            res = "https://www.reviversoft.com"+row.a.get('href')
            uInside = uReq(res)
            pageInsideSoup = soup(uInside.read(),"html.parser")
            uInside.close()
            title = pageInsideSoup.find("h1",{"class":"ext"}).text.replace('File Extension','')
            divTag = pageInsideSoup.find("div",{"class":"ext_desc"}).findChildren()
            category = divTag[0].text.replace("Developer:","").replace(",","").strip()
            types = divTag[2].text.replace("File type:","").replace(",","").strip()
            divTag2 = pageInsideSoup.find("div",{"class":"left_side"}).findChildren()
            desc = divTag2[2].text.strip()
            apps = pageInsideSoup.find_all("div",{"class":"prog_title"})
            if(len(types) == 0):
                types = "N/A"
            if(len(category) == 0):
                category = "N/A"
            if(len(desc) == 0):
                desc = "N/A"
            txts = []
            for txt in apps:
                txts.append(txt.text)
            listToStr = '|'.join([str(elem).strip() for elem in txts])
            f.write(title + ", " +category+", "+ types.replace(",","") + ", " +desc.replace(",", "")+", "+ listToStr +", " + res +"\n")
        f.close()

    #function to retrieve the html page of the website "openwith" and to set the data of the html page into table_rows_3
    def soupFromUrl3(self):
        try:
            uClient = uReq("https://www.openwith.org/categories/source-code")
            pageSoup = soup(uClient.read(), "html.parser")
            uClient.close()
            containers1 = pageSoup.findAll("tr", {"class": "file-extension-odd"})
            containers2 = pageSoup.findAll("tr", {"class": "file-extension-even"})
            containers = np.concatenate((containers1, containers2))
            result=containers.flatten()       
            table_rows=[]
            for i in range(1, len(result)):
                if i % 5 == 1:
                    table_rows.append(result[i])
            self.table_rows_3=table_rows
            return pageSoup

        except requests.exceptions.RequestException as e:  
            raise SystemExit(e)

    #function to write data of "openwith" website into the csv file
    #Here firstly, opening the file
    #then writing the data into the file
    #and closing the file
    def writeData3(self):
        try:
            f = open(self.outFilename, "a",encoding="utf-8")

        except IOError:
            raise IOError(self.outFilename)


        for row in self.table_rows_3:
            title=row.a.text.strip()
            ref = "https://www.openwith.org"+ row.a.get('href')
            uInside = uReq(ref)
            pageInsideSoup=soup(uInside.read(),"html.parser")
            uInside.close()
            ftype="Developer File"
            typeInside = pageInsideSoup.select('div#content')
            codeType=typeInside[0].h1.text.replace(".","").split(' ')
            codeType=codeType[0]+' '+codeType[1]
            desc = typeInside[0].findAll("div",{"class":"filext-content"})
            realdesc = desc[1].text
            realdesc = realdesc.replace("\t", "").replace("\r", "").replace("\n", "").replace('</ br>',"").replace(r"\([^()]*\)","")
            realdesc = realdesc.split('(')
            realdesc=realdesc[0].strip()
            application = typeInside[0].findAll("div",{"class","filext-app-name"})
            app=application[0].a.text.strip()
            f.write(title + ", " + ftype + ", " + codeType + ", " + realdesc.replace(",", "") + ", " + app.replace(",", "") + ", " + ref + "\n")

        f.close()

    #function to retrieve the html page of the website "dotwhat" and to set the data of the html page into table_rows_4    
    def soupFromUrl4(self):
        try:
            uClient = uReq("http://dotwhat.net/type/developer-files")
            pageSoup = soup(uClient.read(), "html.parser")
            uClient.close()
            table_rows = pageSoup.find_all("a",href = re.compile('file/extension/'))
            self.table_rows_4=table_rows
            return pageSoup

        except requests.exceptions.RequestException as e:  
            raise SystemExit(e)

    #function to write data of "dotwhat" website into the csv file
    #Here firstly, opening the file
    #then writing the data into the file
    #and closing the file
    def writeData4(self):
        try:
            f = open(self.outFilename, "a",encoding="utf-8")
        except IOError:
            raise IOError(self.outFilename)


        for row in self.table_rows_4:
            res = "http://dotwhat.net"+row.get('href')
            uInside = uReq(res)
            pageInsideSoup = soup(uInside.read(),"html.parser")
            uInside.close()
            title = pageInsideSoup.find("div","popUpHead2L").h1.text.replace('File Extension','')
            types = pageInsideSoup.find("div","popUpHead2L").h2.text
            category = pageInsideSoup.find("a",href = re.compile('/type/')).text
            apps = pageInsideSoup.findAll("div",{"class":"dtl-box-soft-title"})
            txts = []
            for txt in apps:
                txts.append(txt.text)
            article = pageInsideSoup.find("article")
            paras = article.find_all("p")
            if(paras == []):
                desc = ""
            else:
                desc = paras[2].text.replace("Answer: Files which are given the ", "").replace("If you are aware of any additional file formats that use the ","").replace(" please let us know.","").strip() +  paras[3].text.strip()
            listToStr = ' '.join([str(elem) for elem in txts])
            if(len(desc)==0):
                desc = "Empty"
            f.write(title + ", " +category+", "+ types + ", " +desc.replace(",", "")+", "+ listToStr +", " + res +"\n")
        f.close()

#Uncomment the below code to run the script
#obj=Scrap()

#obj.soupFromUrl1()
#obj.writeData1()

#obj.soupFromUrl2()
#obj.writeData2()

#obj.soupFromUrl3()
#obj.writeData3()

#obj.soupFromUrl4()
#obj.writeData4()

