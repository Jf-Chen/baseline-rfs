import os
import shutil 
import tarfile
import argparse

parser = argparse.ArgumentParser(description="prepare datasets", formatter_class=argparse.RawTextHelpFormatter)

# parser.add_argument("--dataset_name", type=str, default="miniImageNet", help="dataset name")
parser.add_argument("--tar_from_path", type=str, default="/content/drive/MyDrive/rfs/miniImageNet.tar.gz", help="提取路径")
parser.add_argument("--tar_to_floder", type=str, default="", help="解压位置")
parser.add_argument("--tar_type", type=str, default="tar", help="文件类型")
parser.add_argument("--use_teacher", action='store_true',  help="使用已经训练好的CE") # action='store_true',默认false
parser.add_argument("--teacher_from", type=str, default="/content/drive/MyDrive/rfs/teacher.tar", help="教师网络在teacher中的路径")
parser.add_argument("--teacher_to", type=str, default="/content/baseline-rfs/rfs-master", help="解压路径")
parser.add_argument("--teacher_type", type=str, default="tar", help="文件类型")

try :
    get_ipython()
    args = parser.parse_args(args=[])
except :
    args = parser.parse_args()

# 如果使用教师网络
if args.use_teacher:
    print("---- download pre-train teacher")
    shutil.unpack_archive(args.teacher_from ,"./",format=args.teacher_type) #默认解压到当前目录
    # 解压出来是/content/baseline-rfs/rfs-master/model_path/resnet12_miniImageNet_lr_0.05_decay_0.0005_trans_A_trial_pretrain，太长了
    # os.rename("./model_path/resnet12_miniImageNet_lr_0.05_decay_0.0005_trans_A_trial_pretrain","./model_path/teacher")
    
    
# 下载数据集

if not os.path.exists(args.tar_to_floder):
    print("--- args.tar_to_floder not exist,now create")
    os.makedirs(args.tar_to_floder) 

shutil.unpack_archive(args.tar_from_path, args.tar_to_floder,args.tar_type)

# 创建其他文件夹
model_path="./model_path"
if not os.path.exists(model_path):
    print("---- ./model_path not exist,now create")
    os.makedirs(model_path) 

tensorboard_logger="./tb_path"
if not os.path.exists(tensorboard_logger):
    print("----./tb_path not exist,now create")
    os.makedirs(tensorboard_logger) 
    
data_root="./data_root"
if not os.path.exists(data_root):
    print("---- ./data_root not exist,now create")
    os.makedirs(data_root) 
    







    

    




