import os
import numpy as np

def get_lax_sod_network():
    return [12, 12, 10, 12, 10, 12, 10, 10, 12,1]

def get_lax_sod_data_inner():

    data_path = os.environ.get("LAX_SOD_REPO_PATH", "../lax_sod_tube")

    qmc_points = np.loadtxt(os.path.join(data_path, "parameters/parameters_sobol_X.txt"))




    forces = np.loadtxt(os.path.join(data_path, "functionals/average_functionals_sobol_2048.txt"))


    data_per_func = {}



    force_names = [*[f'q{k+1}' for k in range(3)],
                   *[f'EK{k+1}' for k in range(3)]]


    for n, force_name in enumerate(force_names):
        data_per_func[force_name] = forces[:, n]

    return qmc_points, data_per_func
def get_lax_sod_data():


    qmc_points, qmc_values = get_lax_sod_data_inner()
    mc_params, mc_values = get_lax_sod_data_mc_inner()
    return qmc_points, qmc_values, mc_params, mc_values


def get_lax_sod_data_mc_inner():

    data_path = os.environ.get("LAX_SOD_REPO_PATH", "../lax_sod_tube")

    mc_points = np.loadtxt(os.path.join(data_path, "parameters/parameters_mc_X.txt"))




    forces = np.loadtxt(os.path.join(data_path, "functionals/average_functionals_mc_2048.txt"))



    data_per_func = {}



    force_names = [*[f'q{k+1}' for k in range(3)],
                   *[f'EK{k+1}' for k in range(3)]]


    for n, force_name in enumerate(force_names):
        data_per_func[force_name] = forces[:, n]
    
    return mc_points, data_per_func
def get_lax_sod_data_mc():

    mc_params, mc_values = get_lax_sod_data_mc_inner()
    qmc_params, qmc_values = get_lax_sod_data_inner()
    return mc_params, mc_values, qmc_params, qmc_values


def make_folders():
    folders = ['img', 'img_tikz', 'tables', 'results']

    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)
