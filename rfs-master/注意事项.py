"""
1. 无法用easy的dataset，因此需要单独下载rfs的dataset
2. 从dropbox下载文件时，不应该点开某个文件再复制链接，
    而应该直接在文件的选择页面，右键文件复制链接，然后wget url
    如 
    !wget -O /content/baseline-rfs/miniImageNet.tar.gz https://www.dropbox.com/sh/6yd1ygtyc3yd981/AABVeEqzC08YQv4UZk7lNHvya?dl=0&preview=miniImageNet.tar.gz
"""