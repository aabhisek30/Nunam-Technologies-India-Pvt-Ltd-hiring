""""This file combine different sheet of excel file and make new csv"""
import cProfile
import pstats
from functools import wraps
import pandas as pd

def profile(output_file="cprofile.txt",sort_by='cumulative',lines_to_print=None,strip_dirs=False):
    """This function returns cprofile of the function"""
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            _output_file = output_file or func.__name__ + '.prof'
            p_r = cProfile.Profile()
            p_r.enable()
            retval = func(*args, **kwargs)
            p_r.disable()
            #pr.dump_stats(_output_file)

            with open(_output_file, 'a+') as file:
                p_s = pstats.Stats(p_r, stream=file)
                if strip_dirs:
                    p_s.strip_dirs()
                if isinstance(sort_by, (tuple, list)):
                    p_s.sort_stats(*sort_by)
                else:
                    p_s.sort_stats(sort_by)
                p_s.print_stats(func)
                p_s.print_stats(lines_to_print)
            return retval

        return wrapper

    return inner

Detail_67_file = ["Detail_67_1_1", "Detail_67_1_1_1", "Detail_67_1_1_2", "Detail_67_1_1_3", \
"Detail_67_1_1_4", "Detail_67_1_1_5", "Detail_67_1_1_6"]
DetailVol_67_file = ['DetailVol_67_1_1', 'DetailVol_67_1_1_1', 'DetailVol_67_1_1_2', \
'DetailVol_67_1_1_3', 'DetailVol_67_1_1_4', 'DetailVol_67_1_1_5', 'DetailVol_67_1_1_6']
DetailTemp_67_file = ['DetailTemp_67_1_1', 'DetailTemp_67_1_1_1', 'DetailTemp_67_1_1_2',\
'DetailTemp_67_1_1_3', 'DetailTemp_67_1_1_4','DetailTemp_67_1_1_5', 'DetailTemp_67_1_1_6']
# For detail and detail vol
@profile()
def combine(file_name,combined_data):
    """This function combines all the sheet for detail and detail vol"""
    for name in file_name:
        print(name)
        temp = pd.read_excel("data.xlsx",sheet_name=name)
        combined_data = combined_data.append(temp,verify_integrity=True,ignore_index=True)
    return combined_data
data = pd.read_excel("data.xlsx",sheet_name=Detail_67_file[0],nrows=1)
combined_data_1 = pd.DataFrame(columns = data.columns)
combine(Detail_67_file,combined_data_1).to_csv("detail.csv",index=True)

data = pd.read_excel("data.xlsx",sheet_name=DetailVol_67_file[0],nrows=1)
combined_data_2 = pd.DataFrame(columns = data.columns)
combine(DetailVol_67_file,combined_data_2).to_csv("detailVol.csv",index=True)

#For temp
@profile()
def combine_temp(file_name,combined_data):
    """This function combines all the sheet for detail temp"""
    for index,value in enumerate(file_name):
        if index in [0,1,2]:
            print(value)
            temp = pd.read_excel("data.xlsx",sheet_name=value)
            combined_data = combined_data.append(temp,verify_integrity=True,ignore_index=True)
        else:
            print(value)
            temp = pd.read_excel("data_1.xlsx",sheet_name=value)
            combined_data = combined_data.append(temp,verify_integrity=True,ignore_index=True)
    return combined_data

data = pd.read_excel("data.xlsx",sheet_name=DetailTemp_67_file[0],nrows=1)
combined_data_3 = pd.DataFrame(columns = data.columns)
combine_temp(DetailTemp_67_file,combined_data_3).to_csv("detailTemp.csv",index=True)
