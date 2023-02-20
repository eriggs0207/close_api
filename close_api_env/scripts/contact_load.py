import csv

def lead_from_csv(data):
    lead = {'name': data['Company'], 'contacts': [], 'custom': {}}

    if data['Company'] in lead['name']:
        contact = {}
        if data['Contact Name'] in data:
            contact['name'] = data['Contact Name']
        if 'Title' in data:
            contact['title'] = data['Title']

        phones = []
        if data['Contact Phones'] in data:
            phones.append({'phone': data['Contact Phone'], 'type': 'office'})
        if len(phones):
            contact['phones'] = phones

        emails = []
        if data['Contact Emails'] in data:
            emails.append({'email': data['Contact Email'], 'type': 'office'})
        if len(emails):
            contact['emails'] = emails

        if len(contact):
            lead['contacts'] = [contact]


    return lead

with open("close_api_env/data/Leads_Mock_Data.csv") as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    headers = reader.fieldnames
    data = next(reader)

    grouped_lead = {}

    for row in reader:
        if row['Company'] in grouped_lead:
            grouped_lead[ row['Company']]['contact name'].append(row['Contact Name'])
            grouped_lead[ row['Company']]['email'].append(row['Contact Emails'])
            grouped_lead[ row['Company']]['phone'].append(row['Contact Phones'])
        else:
            grouped_lead[ row['Company']] = {'contact name': [row['Contact Name']], 'email': [row['Contact Emails']], 'phone': [row['Contact Phones']]}

    import ipdb; ipdb.set_trace()

    # print(type(lead))
    # for row in reader:
    #     leads['name'] = row[0]

    #     contacts.append(line)
    #
    # contact = [list(filter(None, lst)) for lst in contacts]
print(lead_from_csv(row))
