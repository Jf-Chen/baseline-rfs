# ======================
# exampler commands on miniImageNet
# ======================

# ======================
# tb_path: tensorboardlogger path
# ======================
# supervised pre-training
python train_supervised.py --trial pretrain --model_path ./model_path --tb_path ./tb_path --data_root ./data_root --num_workers 2


# distillation
# ======================
# setting '-a 1.0' should give simimlar performance
# --path_t  teacher_model.pth path
# --model_path  /path/to/save
# --tb_path  /path/to/tensorboard
# --data_root  ./data_root
# ======================
python train_distillation.py -r 0.5 -a 0.5 --path_t ./model_path/resnet12_miniImageNet_lr_0.05_decay_0.0005_trans_A_trial_pretrain/ckpt_epoch_100.pth --trial born1 --model_path ./model_path --tb_path ./tb_path --data_root ./data_root

# evaluation
# ======================
# python eval_fewshot.py --model_path /path/to/student.pth --data_root /path/to/data_root
# ======================
python eval_fewshot.py --model_path /path/to/student.pth --data_root ./data_root --num_workers 2

# 修改后必须确保运行时的当前目录是rfs-master



