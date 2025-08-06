# KNMI Data Loader

## API
API downloader


## NC handler

in `nc_handler.py`, can process the `nc` file into one excel file in `data`folder. use `data_set_handler.py`
NOTE: if the table is too long, will only export top 10k rows


## tar handler

in `KNMI_tar_handler.py`, can process the `tar` file into multiple csv file in `data`folder
NOTE : if the table is too long, will only export top 10k rows