# common function that can be used by many files in project

import os
import sys
import numpy as np
import pandas as pd
from src.exception import Custom__exception
# for creating pkl file
import dill

def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise Custom__exception(e, sys)
