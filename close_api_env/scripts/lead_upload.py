import pandas as pd

#Create a dataframe using pandas from the csv that replaces the empty strings for nan value
df = pd.read_csv("close_api_env/data/Leads_Mock_Data.csv", skipinitialspace=True)
#Create a list of the headers in the csv
headers = list(df.columns)
#Create a collection of dictionaries for each row of the csv
data = df.to_dict('records')
#Create a list of companies to get rid of duplicates
companies = set([ d['Company'] for d in data ])
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
    for k, v in grouped_lead.items():
        for i in data:
            new_lead['name'] = k

            custom = {}
            if f"{headers[4]}" in i:
                custom['founded'] = i[f"{headers[4]}"]
            if f"{headers[5]}" in i:
                custom['revenue'] = i[f"{headers[5]}"]
            if len(custom):
                new_lead['custom'] = custom

            address = {}
            if 'address' in i:
                address['address'] = i['address']
            if 'city' in i:
                address['city'] = i['city']
            if f"{headers[6]}" in i:
                address['state'] = i[f"{headers[6]}"]
            if 'zip' in i:
                address['zipcode'] = i['zip']
            if 'country' in i:
                address['country'] = i['country']
            if len(address):
                new_lead['addresses'] = [address]


            contact = {}
            contact['name'] = v['contact name']

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

            import ipdb; ipdb.set_trace()

            return new_lead


print(lead_from_csv(data))
