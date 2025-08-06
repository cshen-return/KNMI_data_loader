from enum import Enum, unique

@unique
class HarmonieParameter(Enum):
    """
    An Enum for Harmonie model parameters, storing the numerical ID,
    descriptive name, and abbreviation.
    """

    def __init__(self, id, description, abbreviation):
        self.id = id
        self.description = description
        self.abbreviation = abbreviation


    # Define the members
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

    @classmethod
    def id_to_description(cls):
        return {member.id: member.description for member in cls}

    @classmethod
    def id_to_name(cls):
        return {member.id: member.name for member in cls}
#
# # Example usage
# print(id_to_description_map[11])
# print(id_to_description_map[52])

# # Example usage:
# print(HarmonieParameter.TMP.id)
# print(HarmonieParameter.TMP.description)
# print(HarmonieParameter.TMP.abbreviation)