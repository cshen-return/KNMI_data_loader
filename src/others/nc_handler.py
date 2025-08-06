import xarray as xr # pip install xarray netCDF4 (for nc files) cfgrib (for grib files (within the tar))

from data_set_handler import ds_to_excel


def access_nc_file(file):
    # Load dataset
    ds = xr.open_dataset(file)
    ds_to_excel(ds,".\\data\\nc_data.xlsx")




if __name__ == "__main__":
    # download_file()

    #read nc
    filename = ".\\data\\KMDS__OPER_P___10M_OBS_L2_202506190000.nc"
    nc_ds=access_nc_file(filename)
