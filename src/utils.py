import pandas as pd
import os

def load_csv(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    return pd.read_csv(filepath, on_bad_lines="skip")