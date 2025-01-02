

class ClassifyBasedonElement:
    def __init__(self):
        pass
        
    def filter_CHO(self, data):
        dataCHO = data[
            (data['C'] > 0) &
            (data['H'] > 0) &
            (data['O'] > 0) &
            (data['N'] == 0) &
            (data['P'] == 0) &
            (data['S'] == 0)
            ]
        return dataCHO

    def filter_CHON(self, data):
        dataCHON = data[
            (data['C'] > 0) &
            (data['H'] > 0) &
            (data['O'] > 0) &
            (data['N'] > 0) &
            (data['P'] == 0) &
            (data['S'] == 0)
            ]
        return dataCHON

    def filter_CHOS(self, data):
        dataCHOS = data[
            (data['C'] > 0) &
            (data['H'] > 0) &
            (data['O'] > 0) &
            (data['N'] == 0) &
            (data['P'] == 0) &
            (data['S'] > 0)
            ]
        return dataCHOS

    def filter_CHONS(self, data):
        dataCHOS = data[
            (data['C'] > 0) &
            (data['H'] > 0) &
            (data['O'] > 0) &
            (data['N'] > 0) &
            (data['P'] == 0) &
            (data['S'] > 0)
            ]
        return dataCHOS

    def ClassifyBasedonElement(self, data):
        '''This part is used to classify the data into different part'''
        data_CHO = self.filter_CHO(data)
        data_CHON = self.filter_CHON(data)
        data_CHOS = self.filter_CHOS(data)
        data_CHONS = self.filter_CHONS(data)

        return data_CHO, data_CHON, data_CHOS, data_CHONS
