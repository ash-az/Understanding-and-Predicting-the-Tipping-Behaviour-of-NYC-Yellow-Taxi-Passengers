from urllib.request import urlretrieve
import os

# from the current `scripts` directory, go back one levels to the `Project 1` directory
output_relative_dir = 'data/raw/'

# check if it exists as it makedir will raise an error if it does exist
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)



URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv"   

# generate url
url = f'{URL_TEMPLATE}'
# generate output location and filename
output_dir = f"{output_relative_dir}/zone_lookup.csv"
# download
urlretrieve(url, output_dir) 
        
print("Completed zone lookup download")
