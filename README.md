# Numan-hiring
code written for internship task

## Task 1 - Create 3 separate '.csv'* files named 'detail.csv', 'detailVol.csv' and 'detailTemp.csv'.

1. Combine all the data in sheets named like "Detail_67_" only, among the two data files provided, and save into 'detail.csv'
2. Combine all the data in sheets named like "DetailVol_67_" only, among the two data files provided, and save into 'detailVol.csv'
3. Combine all the data in sheets named like "DetailTemp_67_" only, among the two data files provided, and save into 'detailTemp.csv' Provide attention to the column 'Record Index' which provided index values to avoid mismatching the rows while combining multiple files.

4. Input file - data.xlsx and data_1.xlsx
5. file name - file_combine.py
6. Run on command prompt - python file_combine_py
7. output file - detail.csv, detailTemp.csv, detailVol.csv, cprofile.txt


## Task 2 - Apply down-sampling method to reduce the sampling rate to 1 sample/minute. Appy the same to 'detail.csv', 'detailVol.csv' and 'detailTemp.csv' and creating 3 files named 'detailDownsampled.csv', 'detailVolDownsampled.csv' and 'detailTempDownsampled.csv'

1. Input file - detail.csv, detailTemp.csv, detailVol.csv
2. file name - down_sampling.py
3. Run on command prompt - python down_sampling.py
4. output file - detailDownsampled.csv, detailVolDownsampled.csv','detailTempDownsampled.csv', cprofile.txt

## Task 3 - Apply low pass filter technique for noise removal on the data set for 'detailVolDownsampled.csv' and show the distribution of the dataset through visualization, also provide explanation of the same.

1. Input file - detailVolDownsampled.csv'
2. file name - low_pass_filter.ipynb
3. output file - cprofile.txt

## Task 4 - Run profile for all the functions; use cProfile for Python for profiling of individual functions.

1. Function for cprofile is written in all files.
2. output file - cprofile.txt

