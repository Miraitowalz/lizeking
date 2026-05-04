
import pandas as pd
import uuid

def write_excel(results):
    df = pd.DataFrame(results)
    filename = f"/mnt/data/result_{uuid.uuid4().hex}.xlsx"
    df.to_excel(filename, index=False)
    return filename
