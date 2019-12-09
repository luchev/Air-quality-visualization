from src.enums.enums import Parameter, Station
from datetime import datetime


class Parser:
    def __init__(self):
        self.data = []

    @staticmethod
    def convert_enum_key_list_to_enum_value_list(items: list, enum_type):
        """
        Convert a list of Enum keys to a list of Enum values
        If the provided list contains invalid objects return empty list

        IMPORTANT: Works only with IntEnums which have All key, as the ones in this project
        """
        out = []
        for i in items:
            if isinstance(i, enum_type):
                out.append(i.value)
            else:
                return []
        if enum_type.All.value in out:
            out = list(map(int, enum_type))
            out.remove(enum_type.All.value)
        return out

    @staticmethod
    def convert_station_list(station: list) -> list:
        """
        Convert a list of Station enums to a list of ints
        If the provided list contains invalid objects return empty list
        """
        return Parser.convert_enum_key_list_to_enum_value_list(station, Station)

    @staticmethod
    def convert_parameter_list(parameter: list) -> list:
        """
        Convert a list of Parameter enums to a list of ints
        If the provided list contains invalid objects return empty list
        """
        return Parser.convert_enum_key_list_to_enum_value_list(parameter, Parameter)

    def get(self, stations: list, parameters: list,
            start: datetime = None, end: datetime = None) -> list:
        """
        Given a datetime, a list of stations and a list of parameters
        return the data which matches these parameters for these stations and
        that time

        If no end date is provided the assumed end date is the same day, i.e the given period is 1 day
        """
        stations = self.convert_station_list(stations)
        parameters = self.convert_parameter_list(parameters)
        # Filter for stations and parameters
        filtered = [x for x in self.data if x[1] in stations and x[2] in parameters]
        if start is None:
            return filtered
        if end is None:
            end = start
        return [x for x in filtered if start <= x[0] <= end]
