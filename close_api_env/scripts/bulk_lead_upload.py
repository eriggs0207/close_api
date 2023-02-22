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
csv = df.to_dict('records')

#function to format lead from row of csv per API request body
def lead_from_csv(row):
    lead = {'name': row['Company'], 'contacts': []}

    lead[f"custom.cf_{str(uuid.uuid4().hex)}"] = row[f"{headers[4]}"]
    lead[f"custom.cf_{str(uuid.uuid4().hex)}"] = row[f"{headers[5]}"]

    address = {}
    if f"{headers[6]}" in row:
        address['state'] = row[f"{headers[6]}"]
    if len(address):
        lead['addresses'] = [address]

    return lead

#function to format contacts from row of csv per API request body
def contact_from_csv(row):
    contact = {}
    if f"{headers[1]}" in row:
        contact['name'] = row[f"{headers[1]}"]

    phones = []
    if f"{headers[3]}" in row:
        phones.append({'phone': row[f"{headers[3]}"], 'type': 'office'})
    if len(phones):
        contact['phones'] = phones

    emails = []
    if f"{headers[2]}" in row:
        emails.append({'email': row[f"{headers[2]}"], 'type': 'office'})
    if len(emails):
        contact['emails'] = emails

    return contact

#group company to contacts
grouped_lead = {}

for row in csv:
    lead = lead_from_csv(row)
    contacts = contact_from_csv(row)

    if lead['name'] not in grouped_lead:
        grouped_lead[lead['name']] = lead

    if len(grouped_lead[lead['name']]):
        grouped_lead[lead['name']]['contacts'].append(contacts)
    else:
        grouped_lead[lead['name']]['contacts'] = contacts


#convert leads to JSON and change nan values to null
for value in grouped_lead.values():
    json_dict = json.dumps(value, ignore_nan=True)
    data = json.loads(json_dict)
    api = Client(config.api_key)
    import ipdb; ipdb.set_trace()

    response = api.post('lead', data=data)
    print(response)

#find_leads
api = Client(config.api_key)
response = api.get(
            'lead',
            params={
                'query': '',
                '_fields': 'custom'
            },
        )
