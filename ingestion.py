import pandas as pd # import pandas for general files 
import json # import json for json files 
import requests # import requests for web requests 
from google.cloud import bigquery # import bigquery for bigquery files
import xlrd # import xlrd for excel files, tab names 

### Section 1 
## importing excel workbook file 
xls = xlrd.open_workbook('data\\assignment_data.xls', on_demand=True)
## reviewing what tabs are within spreadsheet
sheet_name = xls.sheet_names()
## through that command user will discover there are two tabs: "Life expectancy at Birth" and "Deaths by Cancer in Europe"
tab1 = pd.read_excel('data\\assignment_data.xls', sheet_name="life_expectancy_at_birth")
tab2 = pd.read_excel('data\\assignment_data.xls', sheet_name='deaths_by_cancer_in_europe')
## check whether if the tabs were imported/assigned properly to its respective variable
print(tab1)
print(tab2)

### Section 2
## importing CMS dataset as 'apidataset' via the request module with get
apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/d5c76eb7-68a2-49f2-8b5d-ec1fd8842f60/data')
## setting the variable as a json file format
apiDataset = apiDataset.json()
## check whether if it was success
print(apiDataset)

### Section 3
## connecting to bigquery and creating a bigquery client with specific json key
client = bigquery.Client.from_service_account_json(r'bigquery\wenjin-504-d075a6d6de0f.json')
## querying public dataset 1
query_job = client.query("SELECT * FROM `bigquery-public-data.covid19_open_data.covid19_open_data` LIMIT 100")
## geting results of query 
results = query_job.result() 
## use "pip install db-dtypes if terminal says its not functioning"
## puting the results into dataframe as the variable bigquery1
bigquery1 = pd.DataFrame(results.to_dataframe()) 

client = bigquery.Client.from_service_account_json(r'bigquery\wenjin-504-d075a6d6de0f.json')
## querying public dataset 2
query_job = client.query("SELECT * FROM `bigquery-public-data.new_york_subway.stop_times` LIMIT 100")
## geting results of query 
results = query_job.result() 
## puting the results into dataframe as the variable bigquery2
bigquery2 = pd.DataFrame(results.to_dataframe()) 
## check whether if it was success
print(bigquery1, '/n', bigquery2)