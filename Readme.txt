With the enormous number of languages and file types used for writing logical source or for data purposes,
it is very important for to effectively identify and categorize a file into its type.
And this has to be done solely based on Extension and Name of the file itself.

Execution Flow for above problem statement:
	1. Extract data from four different data sources using python script and store it in the DFileIdentification.csv file.
	2. Implement the program file classOutput.py and take filenames as input from the user. Make a list of filenames and create an input.csv file.
	3. Read input.csv and store all extensions in a list. Check each extension whether it is valid or not.
	4. After validating an extension, search each in the DFileIdentification.csv file.
	5. After the particular row has been found from data, write it in the output.txt file in a user-readable format.
	6. Create custom unit test cases of each method of classOutput.py by unittest framework in python.
	7. Validate each test case by running the testing script and check if any of the test case fails or not.

REPO:
	1. Folder - DataExtractors :
		This folder contains the files used in scrapping data from the different data sources.
		It also contains the Unit testing of the scrapClass script.
	   File Names : DfileIdentification.csv, scrapClass.py, testScrap.py

	2. Folder - Documentation :
		This folder contains the documentation required for the project.
		1. Deliverable 1
		2. Summary and Execution Flow

	3. Folder - ExtensionSearch :
		This folder contains the file which takes an input and creates a text file in which it returns 
		the output as required by the problem statement in deliverable 2.
		It also contains the file used for unit testing the classOutput file.
	   File Names : classOutput.py, testOutput.py, DfileIdentification.csv, input.csv, output.txt

	4. DfileIdentification.csv : Contains all the data of various extensions which is extracted from different data sources.
