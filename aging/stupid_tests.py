#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:50:26 2017

@author: asier
"""


from scipy.io import loadmat
a = loadmat('/home/asier/Desktop/AGING/Asier/modules_20_60_FC_SC.mat')

nMod = 20

modules_idx = modules_info[nMod-1, :nMod]-1  # -1 due to 0 indexing

FC_Mod = np.empty((nMod, nMod, len(ID_subj)), dtype='float32')
SC_Mod = np.empty((nMod, nMod, len(ID_subj)), dtype='float32')




for i, j in product(range(nMod), range(nMod)):
    if modules_idx[i].shape[0] == 1 or modules_idx[j].shape[0] == 1:
        idx_i, idx_j = sq(modules_idx[i]), sq(modules_idx[j])
    else:
        idx_i, idx_j = np.ix_(sq(modules_idx[i]), sq(modules_idx[j]))

    _A = FC_matrix[idx_i, idx_j, :]
    while _A.ndim != 1:
        _A = np.sum(_A, 0)
    FC_Mod[i, j, :] = _A
    FC_Mod[j, i, :] = FC_Mod[i, j, :]

FC_Mod[0,0,0]

age

 g=[17.446574999999999,
 14.035615999999999,
 12.641095999999999,
 16.339725999999999,
 14.276712000000000,
 18.134246999999998,
 11.454795000000001,
 16.227397000000000,
 14.419178000000000,
 16.682192000000001,
 12.221918000000001,
 16.005479000000001,
 10.887670999999999,
 73.158904000000007,
 70.057534000000004,
 63.457534000000003,
 69.926027000000005,
 67.654794999999993,
 60.690410999999997,
 64.210959000000003,
 64.720547999999994,
 66.975341999999998,
 70.104110000000006,
 64.471232999999998,
 75.558903999999998,
 71.016437999999994,
 46.515067999999999,
 23.005479000000001,
 19.547944999999999,
 50.808219000000001,
 55.989041000000000,
 59.939726000000000,
 20.183561999999998,
 18.942466000000000,
 29.553425000000001,
 24.923287999999999,
 24.328766999999999,
 43.317807999999999,
 43.835616000000002,
 38.479452000000002,
 21.257534000000000,
 46.178082000000003,
 33.473973000000001,
 27.873972999999999,
 24.789041000000001,
 31.194521000000002,
 42.139726000000003,
 21.457533999999999,
 20.994520999999999,
 42.005479000000001,
 27.484932000000001,
 35.786301000000002,
 28.821918000000000,
 34.816437999999998,
 27.610959000000001,
 31.035616000000001,
 26.493151000000001,
 24.775341999999998,
 27.073972999999999,
 27.172602999999999,
 25.079452000000000,
 18.230136999999999,
 44.739725999999997,
 31.073972999999999,
 33.531506999999998,
 18.854794999999999,
 39.334246999999998,
 47.197260000000000,
 38.890411000000000,
 71.358903999999995,
 51.673972999999997,
 53.172603000000002,
 57.347945000000003,
 57.876711999999998,
 59.057533999999997,
 49.123288000000002,
 50.142465999999999,
 47.928767000000001,
 54.309589000000003,
 56.345205000000000,
 52.432876999999998,
 57.186301000000000,
 51.030137000000003,
 52.265752999999997,
 51.115068000000001,
 72.819177999999994,
 70.635615999999999,
 25.378081999999999,
 21.953424999999999,
 24.087671000000000,
 27.723288000000000,
 30.589041000000002,
 61.761643999999997,
 76.019177999999997,
 78.246575000000007,
 65.564384000000004,
 60.852055000000000,
 65.043835999999999,
 70.553425000000004,
 73.339725999999999,
 60.298630000000003,
 68.435615999999996,
 77.054794999999999,
 72.364384000000001,
 61.394520999999997,
 68.361643999999998,
 78.084931999999995,
 66.739726000000005,
 64.739726000000005,
 76.608219000000005,
 74.227396999999996,
 62.579999999999998,
  71.329999999999998,
  64.079999999999998,
  69.670000000000002,
  77.750000000000000,
  80.670000000000002,
  77.829999999999998,
  70.829999999999998,
  80.329999999999998,
  67.579999999999998,
  67.250000000000000,
  71.420000000000002,
  64.000000000000000,
  62.250000000000000,
  61.583333333333336,
  63.583333333333336,
  65.666666666666671,
  63.166666666666664,
  74.583333333333329,
  69.416666666666671,
  74.916666666666671,
  24.250000000000000,
  18.583333333333332,
  20.583333333333332,
  22.666666666666668,
  22.666666666666668,
  19.500000000000000,
  22.083333333333332,
  20.000000000000000,
  22.166666666666668,
  17.416666666666668,
  17.500000000000000,
  20.250000000000000,
  19.250000000000000,
  19.829999999999998,
  21.670000000000002,
  25.166666666666668,
  22.670000000000002,
  22.420000000000002,
  22.000000000000000,
  22.420000000000002,
  23.170000000000002,
  20.829999999999998,
  20.329999999999998,
 ]