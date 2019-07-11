#!/usr/bin/env python
# coding: utf-8

# # Lax Sod experiments
# All data is available in the repository

# In[1]:




import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



from machine_learning import *
from notebook_network_size import find_best_network_size_notebook, try_best_network_sizes
from train_single_network import train_single_network
from lax_sod_data import get_lax_sod_data, make_folders

import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = ""


def get_lax_sod_network():
    return [12, 12, 10, 12, 10, 12, 10, 10, 12,1]

if __name__ == '__main__':
    make_folders()

    import argparse

    parser = argparse.ArgumentParser(description='Compute airfoil case (with QMC points)')


    parser.add_argument('--functional_name',
                        default=None,
                        help='The functional to use options: (q<k> or EK<k> for k=1,2,3)')

    args = parser.parse_args()
    functional_name = args.functional_name

    lax_sod_network = get_lax_sod_network()


    parameters, data_per_func, parameters_qmc, data_per_func_qmc = get_lax_sod_data_mc()






    for force_name in data_per_func.keys():
        if functional_name is  None or (force_name.lower() == functional_name.lower()):
            train_single_network(parameters=parameters,
                                 samples=data_per_func[force_name],
                                 base_title='Lax Sod Tube MC %s' % force_name,
                                 network = airfoils_network,
                                 monte_carlo_parameters = parameters_qmc,
                                 monte_carlo_values = data_per_func_qmc[force_name])
