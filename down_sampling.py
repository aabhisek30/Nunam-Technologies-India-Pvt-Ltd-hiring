"""This file decreases sampling rate of data from 1 sample/sec to 1 sample/min"""
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

@profile()
def down_sample(title,filename):
    """This function downsample time series data from sample/sec to sample/min using resample \
    function of pandas"""
    if title == "detail":
        data = pd.read_csv(filename, header=0, parse_dates=["Absolute Time"], \
        index_col="Record Index",
        squeeze=True).drop("Unnamed: 0",axis=1)
        resample = data.resample('T',on="Absolute Time").mean()
    else:
        data = pd.read_csv(filename, header=0, parse_dates=["Realtime"], index_col=\
        "Record ID", squeeze=True).drop("Unnamed: 0",axis=1)
        resample = data.resample('T',on="Realtime").mean()
    return resample
down_sample("detail","detail.csv").to_csv('detailDownsampled.csv',index=True)
down_sample("detailvol","detailVol.csv").to_csv('detailDownVolsampled.csv',index=True)
down_sample("detailtemp","detailTemp.csv").to_csv('detailDownTempsampled.csv',index=True)
