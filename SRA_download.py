import os
# import re
# import logging
import multiprocessing as mp
import subprocess
import pandas as pd


def work(cmd):
    return subprocess.call(cmd, shell=True)


def main():

    list_file_dir = '/media/luolab/ZA1BTJWV/SRA_downloads/SRR_Acc_List.txt'
    list = pd.read_csv(list_file_dir, header=None, squeeze=True)

    dst = '/media/luolab/ZA1BTJWV/ncbi/'

    cmd_download = []
    for _, s in list.iteritems():
        if not os.path.exists(os.path.join(dst, '_'.join([s, '1.fastq.gz']))):
            cmd_this_download = 'fastq-dump --split-files -gzip ' + s
            cmd_download.append(cmd_this_download)

    pool = mp.Pool(16)
    pool.map(work, cmd_download)


if __name__ == '__main__':
    main()
