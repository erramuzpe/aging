from __future__ import absolute_import, division, print_function

import os
import aging as ag
import scipy.io as sio
import numpy as np

data_path = os.path.join(ag.__path__[0], 'data')
aging_data_dir = os.path.join(data_path, 'subjects')
container_data_dir = os.path.join(data_path, 'container_data')  # ID_subj,FCpil
mod_data_dir = os.path.join(data_path, 'mods')


life_span_path = "/home/asier/Desktop/AGING/life_span_paolo"
life_span2_path = "/home/asier/Desktop/AGING/life_span2"


def silent_remove(filename):
    try:
        os.remove(filename)
    except OSError:
        pass


def add_info_from_file(info_file, old_or_young='old'):

    for i in range(len(info_file[old_or_young+'Info'])):
        dr = os.path.join(aging_data_dir,
                          info_file[old_or_young+'Info'][i][0][0])
        try:
            np.savetxt(os.path.join(dr, 'age.txt'),
                       info_file[old_or_young+'Age'][i][0][0],
                       fmt='%s')
            np.savetxt(os.path.join(dr, 'gender.txt'),
                       info_file[old_or_young+'Sex'][i][0],
                       fmt='%s')
        except:
            print('Failed {}'.format(info_file[old_or_young+'Info'][i][0][0]))


def copy_full_tree(src, dst):
    from distutils.dir_util import copy_tree
    for root, dirs, files in os.walk(src):
        for dr in dirs:
            os.makedirs(os.path.join(dst, dr))
    copy_tree(src, dst)


# Module for data preparation (OLD)
def order_data_old():
    copy_full_tree(life_span2_path, aging_data_dir)

    info = sio.loadmat(os.path.join(aging_data_dir, 'partecipantsInfo_v2.mat'))

    add_info_from_file(info, 'old')
    add_info_from_file(info, 'young')

    for file in os.listdir(aging_data_dir):
        if file.endswith(".mat") or file.endswith(".xls"):
            os.remove(os.path.join(aging_data_dir, file))

    for root, dirs, files in os.walk(aging_data_dir):
        for file in files:
            if file.endswith('networks.mat'):
                os.rename(os.path.join(root, file),
                          os.path.join(root, 'time_series.mat'))

    copy_full_tree(life_span_path, aging_data_dir)


# Module for data preparation (NEW) - Modify the OLD one
def order_data_new():

    gsr_sc = '/home/asier/Desktop/aging_final_data/sc_networks'
    gsr_fc = '/home/asier/Desktop/aging_final_data/ts_gsr'

    dst_dir = os.listdir(aging_data_dir)
    dst_dir.sort()

    src_dir_sc = os.listdir(gsr_sc)
    src_dir_sc.sort()

    # src_dir_sc = os.listdir(gsr_sc)
    # src_dir_sc.sort()
    # src_dir_sc == src_dir_fc == True

    for i, file in enumerate(src_dir_sc):
        print(file)
        dst_path = os.path.join(aging_data_dir, dst_dir[i], 'time_series.npy')
        if not os.path.exists(dst_path):
            fc_matrix = np.loadtxt(os.path.join(gsr_fc, file), dtype='float32')
            np.save(os.path.join(aging_data_dir,
                                 dst_dir[i],
                                 'time_series.npy'), fc_matrix)
            silent_remove(os.path.join(aging_data_dir,
                                       dst_dir[i],
                                       'time_series.mat'))

        dst_path = os.path.join(aging_data_dir, dst_dir[i], 'fiber_num.npy')
        if not os.path.exists(dst_path):
            sc_matrix = np.loadtxt(os.path.join(gsr_sc, file), dtype='int16')
            np.save(os.path.join(aging_data_dir,
                                 dst_dir[i],
                                 'fiber_num'), sc_matrix)
            silent_remove(os.path.join(aging_data_dir,
                                       dst_dir[i],
                                       'fiber_num.mat'))


def create_motion_info():
    import csv

    dst_dir = os.listdir(aging_data_dir)
    dst_dir.sort()
    src = '/home/asier/Desktop/aging_final_data/'

    file = os.path.join(src, 'life_span_motion_variables.csv')

    with open(file, 'r') as csvfile:
        spamreader = csv.reader(csvfile)
        for i, row in enumerate(spamreader):
            if row[0] != 'Code':
                dst_path = os.path.join(aging_data_dir, dst_dir[i])
                np.save(os.path.join(dst_path, 'fmri_motion'), row[1])
                np.save(os.path.join(dst_path, 'dti_motion'), row[2])


def create_motion_containers():

    dst_dir = os.listdir(aging_data_dir)
    dst_dir.sort()

    fmri_motion = np.zeros(len(dst_dir))
    dti_motion = np.zeros(len(dst_dir))

    for i, dst in enumerate(dst_dir):
        dst_path = os.path.join(aging_data_dir, dst)
        fmri_motion[i] = np.load(os.path.join(dst_path,
                                              'fmri_motion.npy')).tolist()
        dti_motion[i] = np.load(os.path.join(dst_path,
                                             'dti_motion.npy')).tolist()

    np.save(os.path.join(container_data_dir, 'fmri_motion'), fmri_motion)
    np.save(os.path.join(container_data_dir, 'dti_motion'), dti_motion)
