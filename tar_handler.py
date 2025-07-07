import tarfile
import tempfile
import os
import cfgrib
from data_set_handler import ds_to_excel


def access_tar(tarname):
    with tempfile.TemporaryDirectory() as tempdir:
        with tarfile.open(tarname) as tar:
            tar.extractall(path=tempdir)
        grib_files = [os.path.join(tempdir,f) for f in os.listdir(tempdir)]

        for grib_file in grib_files:
            datasets = cfgrib.open_datasets(grib_file)
            for i in range(len(datasets)):
                file_name=grib_file.split('\\')[-1]
                ds_to_excel(datasets[i],f".\\data\\{file_name}_{i}.xls")


if __name__ == "__main__":
    #read tar
    tar_name = ".\\data\\HARM43_V1_P1_2025061822.tar"
    access_tar(tar_name)
