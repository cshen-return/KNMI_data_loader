# KNMI Data Loader

## API
API downloader


## NC handler

in `nc_handler.py`, can process the `nc` file into one excel file in `data`folder. use `data_set_handler.py`
NOTE: if the table is too long, will only export top 10k rows


## tar handler

in `KNMI_tar_handler.py`, can process the `tar` file into multiple csv file in `data`folder
NOTE : if the table is too long, will only export top 10k rows

#important to know:

### meta data that have been mapped:

#### indicatorOfParameter_str

The value is a field in the meta file

The abbreviation of the name can be found in the file name

The detailed string can be found in the data table's column name


    PMSL = (1, "Pressure altitude above mean sea level", "PMSL")
    PSRF = (1, "Pressure height above ground", "PSRF")
    GP = (6, "Geopotential", "GP")
    TMP = (11, "Temperature", "TMP")
    ISBA = (11, "Temperature of nature tile (from 18-11-24)", "ISBA")
    DPT = (17, "Dew-point temperature", "DPT")
    VIS = (20, "Visibility", "VIS")
    UGRD = (33, "u-component of wind", "UGRD")
    VGRD = (34, "v-component of wind", "VGRD")
    RH = (52, "Relative humidity", "RH")
    APCP = (61, "Total precipitation", "APCP")
    WEASD = (65, "Water equivalent of accumulated snow depth", "WEASD")
    SD = (66, "Snow depth", "SD")
    MIXHT = (67, "Mixed layer depth", "MIXHT")
    TCDC = (71, "Total cloud cover", "TCDC")
    LCDC = (73, "Low cloud cover", "LCDC")
    MCDC = (74, "Medium cloud cover", "MCDC")
    HCDC = (75, "High cloud cover", "HCDC")
    LAND = (81, "Landcover Proportion", "LAND")
    NSWRS = (111, "Net short-wave radiation flux (surface)", "NSWRS")
    NLWRS = (112, "Net long-wave radiation flux (surface)", "NLWRS")
    GRAD = (117, "Global radiation flux", "GRAD")
    SHTFL = (122, "Sensible heat flux", "SHTFL")
    LHTFL = (132, "Latent heat flux through evaporation", "LHTFL")
    CSULF = (162, "U-momentum of gusts out of the model", "CSULF")
    CSDLF = (163, "V-momentum of gusts out of the model", "CSDLF")
    LPSX_CUM = (181, "(Cumulative sum) Rain", "LPSX")
    LPSX = (181, "Rain", "LPSX")
    HGTY_CUM = (184, "(Cumulative sum) Snow", "HGTY")
    HGTY = (184, "Snow", "HGTY")
    ICNG = (186, "Cloud base", "ICNG")
    ICWAT_CUM = (201, "(Cumulative sum) Graupel", "ICWAT")
    ICWAT = (201, "Graupel", "ICWAT")
    ICWAT_COL = (201, "(Column integrated) Graupel", "ICWAT_COL")
    MIXLY = (209, "Lightning", "MIXLY")


#### indicatorOfTypeOfLevel_str

The value is a field in the meta file

    ISOBARIC = (100, "Isobaric level", "hPa")
    MSL = (103, "Specified altitude above mean sea level", "m")
    AGL = (105, "Specified height above ground", "m")
    HYBRID = (109, "Hybrid level")
    ENTIRE_ATMOSPHERE = (200, "Entire atmosphere (considered as a single layer)")

#### timeRangeIndicator_str

The value is a field in the meta file

    INSTANTANEOUS = (0, "Instantaneous")
    ACCUMULATED_LIMITED = (2, "Accumulated over a limited period")
    ACCUMULATED_ENTIRE = (4, "Accumulated over the entire forecast period")

