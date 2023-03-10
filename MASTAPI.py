

from astroquery.mast import Observations
from astropy.time import Time

start_date = "2022-12-22 00:00:00"
end_date = "2022-12-23 00:00:00"
start_date_mjd = Time(start_date, format='iso', scale='utc').mjd
end_date_mjd = Time(end_date, format='iso', scale='utc').mjd

#obs_table = Observations.query_region("322.49324 12.16683")
metaDATA = Observations.get_metadata('observations')


#for meta in metaDATA:
#    print(meta)

#print(obs_table[:10])  

#filters = ['F115W','F356W','F444W']
single_obs = Observations.query_criteria(dataRights = 'PUBLIC', obs_collection='JWST', t_obs_release = [start_date_mjd,end_date_mjd], instrument_name = 'Nircam', calib_level = 3)
targets = []
download_path = '/home/pat/repos/JWSTViewer/test-images/'
for obs in single_obs:
    print("Size: ", obs['jpegURL'])
    coordinate = [obs['s_ra'],obs['s_dec']]
    if not coordinate in targets:
        targets.append(coordinate)
    result = Observations.download_file(obs['jpegURL'],local_path = (download_path+obs['obs_id']+'.jpg'))
    print(result)
    #print(obs['s_ra'],obs['s_dec'])
    #print(obs['obs_id'])


print("Targets: ", targets)
data_products = Observations.get_product_list(single_obs)

print("Hellllooooo")
#print(data_products.keys)
for key in data_products[0].keys():
    print(key)
    print(data_products[0][key])

for data in data_products:
    #print("Keys: ",data.keys)
    if 'w_i2d.fits' in data['productFilename']:
        print(data["obs_id"])
        product = data["dataURI"]
        
        print(product)


        #result = Observations.download_file(product)   

        #print(result)


"""

dataproduct_type = 'SCIENCE'
obs_collection='HST'

filters='F606W'

instrument_name='ACS/WFC'

proposal_id=['12062']

dataRights='PUBLIC'

sci_start_time=">=2021-01-01 00:00:00
"""

