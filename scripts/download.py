from urllib.request import urlretrieve
import os

# from the current `scripts` directory, go back one levels to the `Project 1` directory
output_relative_dir = 'data/raw/'

# check if it exists as it makedir will raise an error if it does exist
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)

YEAR = '2018'
MONTHS = range(1, 9)

URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"#year-month.parquet    


# check if 'raw' directory has already been downloaded into
if len(os.listdir(output_relative_dir)) <= 5:
    for month in MONTHS:
        # 0-fill i.e 1 -> 01, 2 -> 02, etc
        month = str(month).zfill(2) 
        print(f"Begin month {month}")
        
        # generate url
        url = f'{URL_TEMPLATE}{YEAR}-{month}.parquet'
        # generate output location and filename
        output_dir = f"{output_relative_dir}/{YEAR}-{month}.parquet"
        # download
        urlretrieve(url, output_dir) 
        
        print(f"Completed month {month}")
else:    
    print("Raw files have already been downloaded") 