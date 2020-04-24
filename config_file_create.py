from configparser import ConfigParser

if __name__ == "__main__":
    
# This python file creates a configuartion file. Change the below directories for your application

config = ConfigParser()

# prepare_dataset.py configuration
config['prepare_dataset'] = {
    #Path To LIDC Dataset
    'LIDC_DICOM_PATH': '/data/notebook/shared/Media_AI_Company/LIDC-IDRI',
    # Directory to save the output files
    # Directory for masks
    'MASK_PATH':'/data/notebook/1_LUNG/data/Mask',
    # Directory for images
    'IMAGE_PATH':'/data/notebook/1_LUNG/data/Image',
    # To save images and mask that doesn't contain any nodule or cancer
    # These images will be used later to evaluate
    'CLEAN_PATH_IMAGE':'/data/notebook/1_LUNG/data/Clean/Image',
    'CLEAN_PATH_MASK':'/data/notebook/1_LUNG/data/Clean/Mask',
    # Mask Threshold is the np.sum(MASK) threshold. Some Masks are too small. We remove these small images,masks as they might act as outliers
    # The threshold 8 was decided by empirical evaluation. 
    'Mask_Threshold':8
}

config['pylidc'] = { 
    'confidence_level': 0.5,
    'padding_size': 512
}


with open('./lung.conf', 'w') as f:
      config.write(f)