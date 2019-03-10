# Medical Data Analysis using Python



This repository contains...

## 1. Basic
- 'Dicom to Nifti' : convert dicom file(.dcm) to nifti file(.nifti) using [dicom2nifti](https://github.com/icometrix/dicom2nifti).
- 'Working with Dicom File' : get numpy array from dicom file(.dcm) using [pydicom](https://pydicom.github.io/pydicom/stable/index.html#) and [SimpleITK](https://github.com/SimpleITK/SimpleITK) and save array to dicom file.
- 'Working with Nifti File' : get numpy array from nifti file(.nii) using [nibabel](https://nipy.org/nibabel/) and SimpleITK and save array to nifti file.

## 2. Preprocessing
- Voxel Size Resampling
- Registration
- White-stripe Normalization
- N4 Bias Correction

## 3. Radiomics - Feature Extraction 
- Extract radiomic features using [pyradiomics](https://pyradiomics.readthedocs.io/en/latest/)
- Extract edge contrast features.
