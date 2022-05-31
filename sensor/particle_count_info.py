from house_info import HouseInfo
from datetime import date

class ParticleData(HouseInfo):
    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(float(rec))
        return recs
