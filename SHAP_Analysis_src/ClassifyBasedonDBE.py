


class ClassifyBasedonDBE:
    def __init__(self):
        pass

    def CalculateDBE_O_C(self, data):
        data['DBE_O_C'] = (data['DBE'] - data['O']) / data['C']
        
    def filterUnsaturatedOxidation1(self, data):
        self.CalculateDBE_O_C(data)
        condition_dbe = (data['DBE_O_C'] >= 0) & (data['DBE_O_C'] <= 1)
        condition_nosc = (data['NOSC'] >= 0) & (data['NOSC'] <= 2.5)
        data_unsaturated_oxidation = data[
            condition_dbe & condition_nosc
        ]
        data_unsaturated_oxidation.drop(columns ='DBE_O_C')
        return data_unsaturated_oxidation

    def filterUnsaturatedreduced2(self, data):
        self.CalculateDBE_O_C(data)
        condition_dbe = (data['DBE_O_C'] >= 0) & (data['DBE_O_C'] <= 1)
        condition_nosc = (data['NOSC'] >= -2.5) & (data['NOSC'] <= 0)
        data_unsaturated_reduced = data[
            condition_dbe & condition_nosc
        ]
        data_unsaturated_reduced.drop(columns ='DBE_O_C')
        return data_unsaturated_reduced

    def filterSaturatedreduced3(self, data):
        self.CalculateDBE_O_C(data)
        condition_dbe = (data['DBE_O_C'] >= -1) & (data['DBE_O_C'] <= 0)
        condition_nosc = (data['NOSC'] >= -2.5) & (data['NOSC'] <= 0)
        dataSaturatedreduce = data[condition_dbe & condition_nosc]
        dataSaturatedreduce.drop(columns ='DBE_O_C')
        return dataSaturatedreduce

    def filterSaturatedoxidation4(self, data):
        self.CalculateDBE_O_C(data)
        condition_dbe = (data['DBE_O_C'] >= -1) & (data['DBE_O_C'] <= 0 )
        condition_nosc = (data['NOSC'] >= 0) & (data['NOSC'] <= 2.5)
        data_saturatedoxidation = data[condition_dbe & condition_nosc]
        data_saturatedoxidation.drop(columns ='DBE_O_C')
        return data_saturatedoxidation
