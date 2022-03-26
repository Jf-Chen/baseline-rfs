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
    
if not os.path.exists(args.tar_to_floder):
    print("args.tar_to_floder not exist,now create")
    os.makedirs(args.tar_to_floder) 

shutil.unpack_archive(args.tar_from_path, args.tar_to_floder,args.tar_type)

# 创建其他文件夹
model_path="./model_path"
if not os.path.exists(model_path):
    print("./model_path not exist,now create")
    os.makedirs(model_path) 

tensorboard_logger="./tb_path"
if not os.path.exists(model_path):
    print("./tb_path not exist,now create")
    os.makedirs(tensorboard_logger) 
    
data_root="./data_root"
if not os.path.exists(model_path):
    print("./data_root not exist,now create")
    os.makedirs(data_root) 
    

    




