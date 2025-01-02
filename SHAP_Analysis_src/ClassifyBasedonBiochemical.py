
class ClassifyBasedonBiochemical:
    def __init__(self):
        pass
        
    def sub1(self, data):
        conditionHC = (data['H/C'] >= 1.50) & (data['H/C'] <= 2.00)
        conditionOC = (data['O/C'] >= 0.52) & (data['O/C'] <= 0.67)
        dataGet = data[conditionOC & conditionHC]
        return dataGet
        
    def sub2(self, data):
        conditionHC = (data['H/C'] >= 1.50) & (data['H/C'] <= 2.20)
        conditionOC = (data['O/C'] >= 0) & (data['O/C'] <= 0.52)
        conditionN = (data['N'] == 0)
        dataGet = data[conditionOC & conditionHC & conditionN]
        return dataGet
        
    def sub3(self, data):
        conditionHC = (data['H/C'] >= 1.50) & (data['H/C'] <= 2.20)
        conditionOC = (data['O/C'] >= 0) & (data['O/C'] <= 0.52)
        conditionN = (data['N'] > 0)
        dataGet = data[conditionOC & conditionHC & conditionN]
        return dataGet
        
    def sub4(self, data):
        conditionHC = (data['H/C'] >= 0.50) & (data['H/C'] <= 1.50)
        conditionOC = (data['O/C'] >= 0.67) & (data['O/C'] <= 1.2)
        dataGet = data[conditionOC & conditionHC]
        return dataGet
        
    def sub5(self, data):
        conditionHC = (data['H/C'] >= 0.70) & (data['H/C'] <= 1.50)
        conditionOC = (data['O/C'] >= 0.10) & (data['O/C'] <= 0.67)
        dataGet = data[conditionOC & conditionHC]
        return dataGet
        
    def sub6(self, data):
        conditionHC = (data['H/C'] > 0.70) & (data['H/C'] < 1.50)
        conditionOC = (data['O/C'] > 0) & (data['O/C'] < 0.10)
        dataGet = data[conditionOC & conditionHC]
        return dataGet
        
    def sub7(self, data):
        conditionHC = (data['H/C'] > 0.20) & (data['H/C'] < 0.70)
        conditionOC = (data['O/C'] > 0) & (data['O/C'] < 0.67)
        dataGet = data[conditionOC & conditionHC]
        return dataGet
        
    def sub8(self, data):
        conditionHC = (data['H/C'] > 0) & (data['H/C'] < 0.50)
        conditionOC = (data['O/C'] > 0.67) & (data['O/C'] < 1.2)
        dataGet = data[conditionOC & conditionHC]
        return dataGet
        
    def ClassifyBasedonBiochemical(self, data):
        '''This part is used to classify the data into different part'''
        data_sub1 = self.sub1(data)
        data_sub2 = self.sub2(data)
        data_sub3 = self.sub3(data)
        data_sub4 = self.sub4(data)
        data_sub5 = self.sub5(data)
        data_sub6 = self.sub6(data)
        data_sub7 = self.sub7(data)
        data_sub8 = self.sub8(data)
        return data_sub1, data_sub2, data_sub3, data_sub4, data_sub5, data_sub6, data_sub7, data_sub8