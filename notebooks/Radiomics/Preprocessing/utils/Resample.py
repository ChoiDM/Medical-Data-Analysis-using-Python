import numpy as np
from glob import glob
import nibabel as nib
from scipy import ndimage
import os

def resample(image_array, origin_voxel_size, target_voxel = (1, 1, 1)):

    resize_factor = [o/t for o, t in zip(origin_voxel_size, target_voxel)]

    img_resampled = ndimage.interpolation.zoom(image_array, resize_factor,
                                                     mode = 'nearest')

    return img_resampled

def mask2binary(mask_array, threshold = 0.5):
    '''
    :param mask_array: numpy array; Resampled numpy array
    :return: mask_binary_img: numpy array with binary data
    '''
    mask_array_binary = np.copy(mask_array)

    mask_array_binary[mask_array_binary > threshold] = 1
    mask_array_binary[mask_array_binary <= threshold] = 0

    return mask_array_binary