
# README

# Close API Take Home

## Table of Contents

1. [Logic of the Script](#logic-of-the-script)
2. [Built With](#built-with)
- [Versions](#versions)
3. [Local Setup](#local-setup)
4. [Contributors](#contributors)

## Logic of the Script

This script takes in a CSV file and cleans the data in order for it to be stored correctly in Close CRM api.
In order to do that it first reads the CSV file using pandas and converts it into a dataframe(a version of a table).  Turning it into a dataframe eliminates the missing data and replaces it with NaN values.  Two functions take in a row of the CSV file as an argument and create leads and contacts.  Each row of the csv file is a contact and a lead can have many contacts. A dictionary is built to associate the leads with their contacts.  The dictionary of grouped_lead is converted into JSON and the NaN values are changed into Null which is JSON convention.  This dictionary is then iterated through and every lead in the CSV is created in the API when the script is run.  

## Built With

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white)


### Versions

This project uses `Python 3.11.1`


## Local Setup

* Fork this repository
* Clone your fork
* From the command line:
    * `source close_api_env/bin/activate`
    * `pip install pandas`
    * `pip install closeio`
* Run the script from the command line with `python3 close_api_env/scripts/bulk_lead_upload.py`.


## Contributors


<img src="https://avatars.githubusercontent.com/u/106836658?s=120&v=4" />

Erik Riggs | [Github](https://github.com/eriggs0207) | [LinkedIn](https://www.linkedin.com/in/erik-riggs/) |

##

[Back To Top](#back-end-repository-for-lunch-and-learn)
