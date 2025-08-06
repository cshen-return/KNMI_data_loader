import csv
import tarfile
import tempfile
import os
import cfgrib
import numpy as np
import pandas as pd

from data_set_handler import ds_to_excel
from eccodes import codes_grib_new_from_file,codes_get,codes_get_values,codes_release,codes_keys_iterator_new,codes_keys_iterator_next,codes_keys_iterator_delete,codes_keys_iterator_get_name,codes_get_array


def access_grib_file(grib_file:str,csv_file:str,value_keys:list,excluded:list):
    with open(grib_file, "rb") as f:
        while True: #loop over gid message from file
            gid = codes_grib_new_from_file(f)  # Get next GRIB message
            if gid is None:
                break

            metadata = {}
            try:
                # create a key iterator
                it = codes_keys_iterator_new(gid)
                while codes_keys_iterator_next(it):
                    key = codes_keys_iterator_get_name(it)
                    # print(key)
                    try:
                        if key in value_keys or key in excluded:
                            continue
                        try:
                            value = codes_get(gid, key)
                        except:
                            value = codes_get_array(gid, key)
                            print(f"meta {key} has {len(value)} values")
                        if isinstance(value,(int,float,str)):
                            metadata[key] = value
                        elif isinstance(value,np.ndarray):
                            if value.ndim == 0:
                                metadata[key] = value.item()
                            else:
                                metadata[key] = value.flatten().tolist()
                        elif isinstance(value, list) and all(isinstance(x, (int, float, str)) for x in value):
                            metadata[key] = value
                        else:
                            metadata[key] = value
                    except Exception as e:
                        print(f"error {e} for key {key}")
                        metadata[key] = None

                # Clean up
                codes_keys_iterator_delete(it)

                #write meta
                pd.DataFrame({k: pd.Series(v) for k, v in metadata.items()}).T.to_csv(f"{csv_file}_{gid}_meta.csv")

                # Get actual data values separately
                data = {}
                for col in value_keys:
                    data[col] = codes_get_array(gid,col)
                pd.DataFrame(data).to_csv(f"{csv_file}_{gid}_data.csv")

                print('all written')
            except Exception as e:
                print(f"error {e}")

            codes_release(gid)

    return None

def access_tar(tarname,path):
    full_tar_path = os.path.join(path, tarname)  # Ensures correct path across platforms

    os.makedirs(f"data\\{tarname}",exist_ok=True)
    with tarfile.open(full_tar_path, "r") as tar:
        for member in tar.getmembers():
            member_path = os.path.join(f"data\\{tarname}", member.name)
            if os.path.exists(member_path):
                continue
            tar.extract(member, path=f"data\\{tarname}")

    grib_files = [os.path.join(f"data\\{tarname}", f) for f in os.listdir(f"data\\{tarname}")]


    for grib_file in grib_files:
        csv_filename=grib_file.split('\\')[-1]
        access_grib_file(grib_file,f"data\\{csv_filename}",value_keys=['values','latitudes','longitudes'],excluded=['latLonValues'])
        #todo: to save into excel or csv?



if __name__ == "__main__":
    #read tar
    path= "./knmi_data/Harmonie-Arome_cy43/EPS Meteorological params"
    for tar_file in os.listdir(path):
        if tar_file.endswith(".tar"):
            access_tar(tar_file,path)

