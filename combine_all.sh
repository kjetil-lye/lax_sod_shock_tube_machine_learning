#!/bin/bash

for f in Q1 Q2 Q3;
do 

    if [[ $f = "Q"* ]]
    then
	fname=${f,,}
    else
	fname=${f}
    fi

    bsub -W 120:00 -R 'rusage[mem=32000]' -N -B python learning_airfoils/python/combine_files.py /cluster/project/sam/klye/lax_sod_shock_tube_machine_learning_early_stopping/learning_lax_sod_$f ${fname}  data/laxsod_$f;
done

for f in Q1 Q2 Q3;
do
    if [[ $f = "Q"* ]]
    then
	fname=${f,,}
    else
	fname=${f}
    fi
 
    bsub -W 120:00 -R 'rusage[mem=32000]' -N -B python learning_airfoils/python/combine_files.py /cluster/project/sam/klye/lax_sod_shock_tube_machine_learning_early_stoppingx/learning_lax_sod_mc_$f ${fname}  data/laxsod_mc_$f;
done
