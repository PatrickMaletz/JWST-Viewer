import matplotlib.pyplot as plt

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

    for image in images:

       
        image_data = fits.getdata(image, ext=1)
        print(type(image_data))
        #fits.info(image)
        #print(image_data[0])
    
        with fits.open(image) as hdul:
                #hdul.info()
                #print(dir(hdul[0]))
                print(hdul[0].is_image)
                #print(image_data)

                image_data = hdul[1].data
                #print(image_data)
                
                try:
                    plt.figure()
                    plt.imshow(image_data, cmap='gray')
                    plt.colorbar()
                    plt.show()
                except:
                    print("Failed on: ", image)
        """    
             for level in hdul:
                print(level.header['DATE'])
                #print(level.data)
                
             
       

        """

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