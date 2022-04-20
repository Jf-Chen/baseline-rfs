pip3 install tensorboardX
echo "----tensorboardX installed"
echo "----current path is:"
echo $PWD

chmod +777 /content/baseline-rfs/rfs-master/scripts/prepare.py 
python /content/baseline-rfs/rfs-master/scripts/prepare.py  --tar_from_path /content/drive/MyDrive/rfs/miniImageNet.tar.gz  --tar_to_floder ./data_root  --tar_type tar --use_teacher

echo "----dataset ready"

# ======================
python train_distillation.py -r 0.5 -a 0.5 --path_t ./model_path/resnet12_miniImageNet_lr_0.05_decay_0.0005_trans_A_trial_pretrain/ckpt_epoch_100.pth --trial born1 --model_path ./model_path --tb_path ./tb_path --data_root ./data_root