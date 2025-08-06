import tarfile
import tempfile
import os
import cfgrib
from data_set_handler import ds_to_excel
from eccodes import GribFile

def access_tar(tarname,path):
    full_tar_path = os.path.join(path, tarname)  # Ensures correct path across platforms

    with tempfile.TemporaryDirectory() as tempdir:
        with tarfile.open(full_tar_path, "r") as tar:
            tar.extractall(path=tempdir)

        grib_files = [os.path.join(tempdir, f) for f in os.listdir(tempdir)]

        for grib_file in grib_files:
            #use eccode
            with GribFile(grib_file) as grib:
                for msg in grib:
                    print(msg['shortName'], msg['level'], msg.size())
                    values = msg['values']
                    coords = msg.keys()  # list available keys
            #use cfgrib
            datasets = cfgrib.open_datasets(grib_file)
            for i in range(len(datasets)):
                file_name=grib_file.split('\\')[-1]
                ds_to_excel(datasets[i],f"{path}\\{file_name}_{i}.xls")


if __name__ == "__main__":
    #read tar
    path= ".\data"
    for tar_file in os.listdir(path):
        access_tar(tar_file,path)

