import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

from astropy.visualization import astropy_mpl_style
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename


import os
# assign directory

# iterate over files in
# that directory


def main():
    
    plt.style.use(astropy_mpl_style)
    #image_file = get_pkg_data_filename('tutorials/FITS-images/HorseHead.fits')
    
    
    directory = '/home/pat/repos/JWSTViewer/test-images'
    images = get_files(directory)

    list_of_images = []
    max_values = []
    minValue = 0.1

    for image in images:

       
        image_data = fits.getdata(image, ext=1)
        print(type(image_data))
        #fits.info(image)
        #print(image_data[0])
    
        with fits.open(image) as hdul:
                hdul.info()
                print(dir(hdul.fileinfo))

                """
                hdr = hdul[0].header
                
                
                print(hdr)
                for head in hdr:
                    print(head)

                print("OBS_ID ",hdr['OBS_ID'])

                print(hdul[0].is_image)
                """
                #print(image_data)

                image_data = hdul[1].data
                image_data -= image_data.min()

                list_of_images.append(image_data)
                zMax = np.max(image_data)
                max_values.append(zMax)

                print(image_data.min())
                
                maxValue = image_data.max()
                #maxValue = 100
                """
                try:
                    plt.figure()
                    plt.imshow(image_data, cmap='gray', norm=colors.LogNorm(vmin=minValue, vmax=maxValue))
                    plt.axis('off')
                    #plt.colorbar()
                    plt.show()
                except:
                    print("Failed on: ", image)
                    """
    new_image = np.add(list_of_images[0],list_of_images[1])
    plt.figure()
    #plt.imshow(list_of_images[0], cmap='gray', norm=colors.LogNorm(vmin=minValue, vmax=list_of_images[0].max()))
    #plt.imshow(list_of_images[0], cmap='hot', vmin = minValue, vmax = 10)
    plt.imshow(list_of_images[1], cmap='RdGy', vmin = minValue, vmax = 100)
    
    plt.axis('off')
    #plt.colorbar()
    plt.show()
        
    return

def get_files(directory):
    files = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            files.append(f)

    return files
    


if __name__ == '__main__':
    main()