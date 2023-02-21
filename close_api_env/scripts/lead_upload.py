import pandas as pd
import config
import simplejson as json
from closeio_api import Client
import uuid

#Create a dataframe using pandas from the csv that replaces the empty strings for nan value
df = pd.read_csv("close_api_env/data/Leads_Mock_Data.csv", skipinitialspace=True)
#Create a list of the headers in the csv
headers = list(df.columns)
#Create a collection of dictionaries for each row of the csv
data = df.to_dict('records')
#Group contacts info by companies and remove duplicates
grouped_lead = {}

for d in data:
    if d['Company'] in grouped_lead:
        grouped_lead[ d['Company']]['contact name'].append(d['Contact Name'])
        grouped_lead[ d['Company']]['email'].append(d['Contact Emails'])
        grouped_lead[ d['Company']]['phone'].append(d['Contact Phones'])
    else:
        grouped_lead[ d['Company']] = {'contact name': [d['Contact Name']], 'email': [d['Contact Emails']], 'phone': [d['Contact Phones']]}

#Create a function to format the data per the API docs POST request body for each lead
def lead_from_csv(data):
    new_lead = {'name': '', 'contacts': []}
    #iterate through keys and values of the grouped_leads
    for k, v in grouped_lead.items():
        #iterate through the csv rows
        for i in data:
            #lead name or company
            new_lead['name'] = k
            #custom fields with random uuid added to field 
            new_lead[f"custom.cf_{str(uuid.uuid4().hex)}"] = i['custom.Company Founded']
            new_lead[f"custom.cf_{str(uuid.uuid4().hex)}"] = i['custom.Company Revenue']

            #adress of company
            address = {}
            if i['Company'] == k:
                address['state'] = i[f"{headers[6]}"]
            if len(address):
                new_lead['addresses'] = [address]

            #list of contacts in lead
            contact = {}
            contact['name'] = i[f"{headers[1]}"]

            phones = []
            for p in v['phone']:
                phones.append({'phone': p, 'type': 'office'})
                if len(phones):
                    contact['phones'] = phones

            emails = []
            for e in v['email']:
                emails.append({'email': e, 'type': 'office'})
                if len(emails):
                    contact['emails'] = emails

            if len(contact):
                new_lead['contacts'] = [contact]


            return new_lead

lead = json.dumps(lead_from_csv(data), ignore_nan=True)
api = Client(config.api_key)
import ipdb; ipdb.set_trace()
response = api.post('lead', data=lead)
print(response)
