
# coding: utf-8

# In[3]:


import requests
import json
import pandas as pd
import datetime


# In[4]:


base_url = 'https://clinicaltrials.gov/api/query/study_fields?expr=breast+cancer'


# In[5]:


extract_fields = [
    'StartDate',
    'NCTId',
    'BriefTitle',
    'Condition',
    'InterventionName',
    'InterventionType',
    'LastKnownStatus',
    'StudyPopulation',
    'StudyType'
]


# In[6]:


query = f'{base_url}&fields={",".join(extract_fields)}&max_rnk=1000&fmt=json'
print(query)


# In[7]:


results = requests.get(query)
results_json =  json.loads(results.content)
print(results_json)


# In[8]:


# This is quite a flat JSON structure, so can be loaded into a DataFrame
df = pd.DataFrame(results_json['StudyFieldsResponse']['StudyFields'])


# In[9]:


#df['StartDate'] = pd.to_datetime(df.StartDate)
df = df.sort_values(by='StartDate', ascending=False)
print(df.head(10))

