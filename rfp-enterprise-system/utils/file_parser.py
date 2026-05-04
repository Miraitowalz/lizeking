
import pandas as pd

def parse_file(file):
    df = pd.read_excel(file.file)
    return df.iloc[:,0].dropna().tolist()
