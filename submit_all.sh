#!/bin/bash
# Submits alls script on euler. 

# Accept additional parameters from the command line. This could eg be "--only_missing"
additional_parameters=$@

# Abort on first error found
set -e

for q in Q1 Q2 Q3; 
do 
    python learning_airfoils/python/submit_all_pure_python_in_parallel.py --functional_name ${q} --script python/learning_lax_sod.py --number_of_widths 1 --number_of_depths 1 ${additional_parameters}; 
    python learning_airfoils/python/submit_all_pure_python_in_parallel.py --functional_name ${q} --script python/learning_lax_sod_mc.py --number_of_widths 1 --number_of_depths 1 ${additional_parameters}; 
done ; 

