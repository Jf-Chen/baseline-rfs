import os
import shutil 
import tarfile
import argparse

parser = argparse.ArgumentParser(description="prepare datasets", formatter_class=argparse.RawTextHelpFormatter)

# parser.add_argument("--dataset_name", type=str, default="miniImageNet", help="dataset name")
parser.add_argument("--tar_from_path", type=str, default="/content/drive/MyDrive/easy/easy-datasets.tar", help="提取路径")
parser.add_argument("--tar_to_floder", type=str, default="", help="解压位置")
parser.add_argument("--tar_type", type=str, default="tar", help="解压位置")

try :
    get_ipython()
    args = parser.parse_args(args=[])
except :
    args = parser.parse_args()
    

shutil.unpack_archive(args.tar_from_path, args.tar_to_floder,args.tar_type)





