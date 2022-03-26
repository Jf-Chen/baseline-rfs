pip3 install tensorboardX
echo "tensorboardX installed"
echo "current path is:"
echo $PWD

chmod +777 /content/baseline-rfs/rfs-master/scripts/prepare.py 
python /content/baseline-rfs/rfs-master/scripts/prepare.py  --tar_from_path /content/drive/MyDrive/easy/easy-datasets.tar  --tar_to_floder ./data_root  --tar_type tar

echo "dataset ready"