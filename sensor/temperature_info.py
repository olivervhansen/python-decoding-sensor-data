import re
from house_info import HouseInfo

# child class of HouseInfo


class TemperatureData(HouseInfo):
    def __convert_data(self, data):
        recs = []

        for rec in data:
            recs.append(int(rec, base=10))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("temperature", rec_area)
        return self.__convert_data(recs)
