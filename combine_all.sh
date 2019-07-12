#!/bin/bash

for f in Q1 Q2 Q3 EK1 EK2 EK3; 
do 
    bsub -W 120:00 -R 'rusage[mem=32000]' -N -B python learning_airfoils/python/combine_files.py /cluster/project/sam/klye/lax_sod_shock_tube_machine_learning/learning_lax_sod_$f ${f,,}  data/laxsod_$f;
done

for f in Q1 Q2 Q3 EK1 EK2 EK3; 
do 
    bsub -W 120:00 -R 'rusage[mem=32000]' -N -B python learning_airfoils/python/combine_files.py /cluster/project/sam/klye/lax_sod_shock_tube_machine_learning/learning_lax_sod_mc_$f ${f,,}  data/laxsod_mc_$f;
done
