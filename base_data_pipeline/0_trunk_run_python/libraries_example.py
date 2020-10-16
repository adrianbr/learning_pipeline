#here is a built-in library. it comes packaged with the "python standard library" so you do not need to install it separately
import json
#there are hundreds of built in libraries but we do not want to import everything because python evaluates and compiles the code on import. Which may take time

#then there are installed libraries, which you need to grab from repositories
#you can use the command pip freeze to check what installed libraries you also have
#pip is the standard python package manager
#you can find the packages installable with pip on https://pypi.org/
"""typically the development process goes 
1. How do I do that? google - say, load from redshift to BQ
2. if no standard solutions, break it down into manageable steps such as 
unload from redshift
load to bigquery

or more granularly

authenticate to redshift
unload or select data
copy to local file (because we cannot tell redshift to SEND it to BQ, so we need to request it and then push it to google storage)
Authenticate to google storage
upload file to storage
create google "job" to read the data from storage into BQ
validate that data arrived in BQ

if copying incrementally, additionally

find suitable increment strategy (such as an incremental merge)
- how to keep track of what was loaded (last value)
- how to check what is new data
- how to update the dataset or append it (merge columns or increment columns)
implement strategy and use the previous pipeline to load the increments as per the strategy
scheduling considerations
data cleaning if necessary (data typing - fixing types messed in transport)

and last but not least
finxing beautiful corner cases (for example, 
a recent load was broken by that the milisecond was stored as float (which is an approximation) in MSSQL 
which lead to rounding errors which lead to forever-looping never ending copy job because it kept recopying the last 0.030 seconds of data.


so now uncomment this line and solve it as you can best. GOOGLE IS YOUR FRIEND
Look for docs that will tell you how to install this library (with pip or otherwise)
usual sources:  https://pypi.org/, github library project page

"""

#from fuzzywuzzy import fuzz
#percent_data_engineer = fuzz.ratio("Matthaus", "Data engineer")
#print(percent_data_engineer)


"""and the next ones - this is harder"""
#from google.cloud import bigquery
#from hubspot import HubSpot