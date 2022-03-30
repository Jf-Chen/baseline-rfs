# ======================
# exampler commands on miniImageNet
# ======================

# supervised pre-training
python train_supervised.py --trial pretrain --model_path ./model_path --tb_path ./tb_path --data_root ./data_root --num_workers 2

# distillation
# setting '-a 1.0' should give simimlar performance
python train_distillation.py -r 0.5 -a 0.5 --path_t /path/to/teacher.pth --trial born1 --model_path /path/to/save --tb_path /path/to/tensorboard --data_root ./data_root

# evaluation
python eval_fewshot.py --model_path /path/to/student.pth --data_root /path/to/data_root

# 修改后必须确保运行时的当前目录是rfs-master