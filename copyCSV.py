import shutil 
import time

def _compute_dest_timestamp(src,dest):
    '''Generate a file name path with timestamp'''
    timestr = time.strftime("%Y-%m-%d-%H%M%S")
    return dest + timestr + "-" + src.split("\\")[-1]

def copy_csv_data(src, dest):
    '''Copy a file of data'''
    shutil.copy2(src, _compute_dest_timestamp(src, dest))