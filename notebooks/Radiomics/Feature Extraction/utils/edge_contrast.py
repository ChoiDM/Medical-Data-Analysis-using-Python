import numpy as np
from scipy import ndimage
from skimage import morphology, measure
from skimage.filters import roberts, sobel, scharr, prewitt



def get_slice_extent(img_mask_array, slice_num):
    cnt = 0
    slice_start = 0
    slice_end = 0
    
    for slice in range(slice_num):
        if np.max(img_mask_array[:,:,slice]) != 0:
            if slice_start == 0:
                slice_start = slice
            else:
                slice_end = slice
            cnt += 1
    
    return cnt, slice_start, slice_end


def get_edge_contrast(img_array, img_mask_array, slice_num):
    edge_contrast_array = []
    
    cnt, slice_start, slice_end = get_slice_extent(img_mask_array, slice_num)
    
    for slice in range(slice_start, slice_end+1):
        mask_array = img_mask_array[:,:,slice]
        
        # Remove small objects.
        threshold = 10
        y = morphology.remove_small_objects(mask_array, threshold + 1)

        # Fill holes.
        y = ndimage.binary_closing(y, structure=np.ones((2, 2)))
        y = morphology.remove_small_holes(y, min_size=512, connectivity=3)
        
        # Find edge
        edge_sobel = sobel(y)
        
        # Get masked gradient img
        gradient_img = np.gradient(img_array[:,:,slice])
        masked_gradient_array = np.multiply(gradient_img, y)
        
        # Get edge contrast img
        final_edge_contrast_x = np.multiply(masked_gradient_array[0], edge_sobel)
        final_edge_contrast_y = np.multiply(masked_gradient_array[1], edge_sobel)
        final_edge_contrast = np.sqrt(final_edge_contrast_x**2 + final_edge_contrast_y**2)
        
        edge_contrast_array.append(final_edge_contrast)
    
    return edge_contrast_array


def remove_top10(edge_contrast_array):
    contrast_list = edge_contrast_array[edge_contrast_array!=0]
    size = contrast_list.size

    index_top10 = int(size*0.9)
    contrast_list_sorted = sorted(contrast_list)
    contrast_list_top10 = contrast_list_sorted[:index_top10]
    contrast_list_top10 = np.array(contrast_list_top10)
    
    return contrast_list, index_top10, contrast_list_top10


def calc_avg_ec(contrast_list, contrast_list_top10, index_top10):
    contrast_list_sorted = sorted(contrast_list)
    
    index_lower75 = int(index_top10*0.75)
    index_lower50 = int(index_top10*0.50)
    index_lower25 = int(index_top10*0.25)

    contrast_list_lower75 = np.array(contrast_list_sorted[:index_lower75])
    contrast_list_lower50 = np.array(contrast_list_sorted[:index_lower50])
    contrast_list_lower25 = np.array(contrast_list_sorted[:index_lower25])

    avg_ec_100 = np.mean(contrast_list_top10)
    avg_ec_75 = np.mean(contrast_list_lower75)
    avg_ec_50 = np.mean(contrast_list_lower50)
    avg_ec_25 = np.mean(contrast_list_lower25)
    
    return avg_ec_100, avg_ec_75, avg_ec_50, avg_ec_25