import os
import pandas as pd

# allows us to not need to hardcode a filepath in.
# CWD will change depending on what folder our terminal is in when we run this code. 
# be sure to be OUTSIDE of the src directory when you run this code.

CWD = os.getcwd()

def read_csv(filepath):
    return pd.read_csv(f"{CWD}/{filepath}")

