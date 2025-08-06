from enum import Enum, unique

@unique
class TimeRangeIndicator(Enum):
    """
    An Enum for time range indicators, storing the numerical ID,
    and a descriptive range string.
    """

    def __init__(self, id, description):
        self.id = id
        self.description = description


    # Define the members
    INSTANTANEOUS = (0, "Instantaneous")
    ACCUMULATED_LIMITED = (2, "Accumulated over a limited period")
    ACCUMULATED_ENTIRE = (4, "Accumulated over the entire forecast period")

    @classmethod
    def id_to_description(cls):
        return {member.id: member.description for member in cls}

    @classmethod
    def id_to_name(cls):
        return {member.id: member.name for member in cls}
#
# # Example usage:
# print(TimeRangeIndicator.INSTANTANEOUS.range)
# print(TimeRangeIndicator.ACCUMULATED_LIMITED.id)
# print(TimeRangeIndicator.id_to_range_map[4])