from enum import Enum, unique

@unique
class LevelType(Enum):
    """
    An Enum for WMO/HIRLAM level types, storing the numerical ID,
    descriptive name, and units.
    """

    def __init__(self, id, description, units=None):
        self.id = id
        self.description = description
        self.units = units


    # Define the members
    ISOBARIC = (100, "Isobaric level", "hPa")
    MSL = (103, "Specified altitude above mean sea level", "m")
    AGL = (105, "Specified height above ground", "m")
    HYBRID = (109, "Hybrid level")
    ENTIRE_ATMOSPHERE = (200, "Entire atmosphere (considered as a single layer)")

    @classmethod
    def id_to_description(cls):
        return {member.id: member.description for member in cls}

    @classmethod
    def id_to_name(cls):
        return {member.id: member.name for member in cls}

# # Example usage:
# print(LevelType.MSL.description)
# print(LevelType.AGL.units)
# print(LevelType.id_to_description_map[100])