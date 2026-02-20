#!/bin/bash

###############################################
pass_pwd=$(dirname $(pwd))
pass_name="$pass_pwd/Porespy/MEANSTAN${VN}"
path_list="model/list_model"
path_model="model/model.pkl"
path_testmap="data_1"


# ---- Execute Python code ----
python3 code_make_model.py "$path_list" "$path_model"
#python3 code_transform.py "$path_model" "$path_testmap"
#python3 code_pred.py "$path_testmap"