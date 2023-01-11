import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

from astropy.visualization import astropy_mpl_style
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
from astropy.visualization import make_lupton_rgb

from reproject import reproject_interp

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
    hdul_list = []
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
                hdul_list.append(hdul[1]) 
                zMax = np.max(image_data)
                max_values.append(zMax)

                #print(image_data.min())
                
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

    for image in list_of_images:
        print(image.shape)

    hdu1 = fits.open(images[0])[1]
    hdu2 = fits.open(images[1])[1]
    hdu3 = fits.open(images[2])[1]
    array1, footprint = reproject_interp(hdu2, hdu1.header)
    array2, footprint = reproject_interp(hdu3, hdu1.header)

    g = list_of_images[0]
    r = array1
    i = array2

    #g = list_of_images[0]
   
    rgb_default = make_lupton_rgb(i, r, g, Q=1, stretch=0.1)
    #plt.imshow(array, cmap='gray', norm=colors.LogNorm(vmin=minValue, vmax=maxValue))
    plt.imshow(rgb_default, origin='lower')
    plt.show()

    rgb_default = make_lupton_rgb(i, r, g, Q=1, stretch=0.5)
    #plt.imshow(array, cmap='gray', norm=colors.LogNorm(vmin=minValue, vmax=maxValue))
    plt.imshow(rgb_default, origin='lower')
    plt.show()
    
    rgb_default = make_lupton_rgb(i, r, g, Q=1, stretch=1.0)
    #plt.imshow(array, cmap='gray', norm=colors.LogNorm(vmin=minValue, vmax=maxValue))
    plt.imshow(rgb_default, origin='lower')
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