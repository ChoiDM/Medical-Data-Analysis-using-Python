import os
import SimpleITK as sitk

def n4correction(input_img):
    '''
    :param input_img: numpy array format
    :return: n4 bias field corrected image with numpy array format
    '''
    
    inputImage = sitk.GetImageFromArray(input_img)
    maskImage = sitk.OtsuThreshold(inputImage, 0, 1, 200)

    inputImage = sitk.Cast(inputImage, sitk.sitkFloat32)
    corrector = sitk.N4BiasFieldCorrectionImageFilter()

    output = corrector.Execute(inputImage, maskImage)
    output = sitk.GetArrayFromImage(output)

    return output
