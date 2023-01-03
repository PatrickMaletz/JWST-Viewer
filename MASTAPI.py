

from astroquery.mast import Observations
from astropy.time import Time

start_date = "2022-12-16 00:00:00"
end_date = "2022-12-17 00:00:00"
start_date_mjd = Time(start_date, format='iso', scale='utc').mjd
end_date_mjd = Time(end_date, format='iso', scale='utc').mjd

#obs_table = Observations.query_region("322.49324 12.16683")
metaDATA = Observations.get_metadata('observations')


for meta in metaDATA:
    print(meta)

#print(obs_table[:10])  

single_obs = Observations.query_criteria(dataRights = 'PUBLIC', obs_collection='JWST', t_obs_release = [start_date_mjd,end_date_mjd], instrument_name = 'Nircam', calib_level = 3)

data_products = Observations.get_product_list(single_obs)

print(data_products)

for data in data_products:
    if 'i2d.jpg' in data['productFilename']:
        print(data['productFilename'])
        product = data["dataURI"]
        print(product)


        result = Observations.download_file(product)   

        print(result)


"""
data_product_1 = data_products[10]


for data in data_product_1:
    print(data)


product = data_product_1["dataURI"]

print(product)


result = Observations.download_file(product)   

print(result)



dataproduct_type = 'SCIENCE'
obs_collection='HST'

filters='F606W'

instrument_name='ACS/WFC'

proposal_id=['12062']

dataRights='PUBLIC'

sci_start_time=">=2021-01-01 00:00:00
"""

