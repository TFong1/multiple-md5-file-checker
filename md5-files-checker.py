import hashlib
import pandas as pd

file_hashes = pd.read_csv("file-hashes.csv", index_col=0, squeeze=True).to_dict()

for k in file_hashes.keys():
    
    with open(k, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    
    if file_hashes[k] == file_hash.hexdigest():
        print("{} OK".format(k))
    else:
        print("{} No Match".format(k))

