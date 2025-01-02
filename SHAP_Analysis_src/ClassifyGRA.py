


import pandas as pd


class ClassifyGRA(object):
    def __init__(self):
        self.columns_name = ['meas.m/z', 'formula', 'intens', 'neu.m/z', 'theor.m/z', 'err.ppm', 'RI', 'O/C', 'H/C', 'DBE', 'NOSC', 'AI_mod', 'S/N', 'C', 'H', 'N', 'O', 'P', 'S', '(DBE-O)/C', 'H/Cwa', 'O/Cwa', 'DBEwa', 'AImod', 'NOSCwa', 'MW', 'MWwa']

    def Activity(self,data1, data2):
        '''condition1:data1有，data2无'''
        common1 = pd.merge(data1, data2, on=['formula'], how="left", indicator=True)
        Part1_only_in_data1 = common1[common1['_merge'] == 'left_only'].drop(columns=['_merge'])
        Part1_only_in_data1 = Part1_only_in_data1.iloc[:,:27]

        '''condition2:data1和data2都有 & data2['intens']/data1['intens'] <0.5'''
        common2 = pd.merge(data1, data2, on=['formula'],suffixes=('_data1','_data2'))
        condition = (common2['intens_data2'] / common2['intens_data1']) < 0.5
        intens_smallthan_05 = common2[condition]
        Part2_intens_smallthan05 = intens_smallthan_05.iloc[:, :27]
        '''Part1 and Part2'''
        Part1_only_in_data1.columns = self.columns_name
        Part2_intens_smallthan05.columns = self.columns_name
        Activity_data = pd.concat([Part1_only_in_data1, Part2_intens_smallthan05], ignore_index=True).drop_duplicates()
        return Activity_data


    def Generate(self,data1, data2):
        '''condition1: data1没有，data2有'''
        common1 = pd.merge(data2, data1, on=['formula'], how="left", indicator=True)
        Part1_only_in_data2 = common1[common1["_merge"] == "left_only"].drop(columns=["_merge"])
        Part1_only_in_data2 = Part1_only_in_data2.iloc[:,:27]

        '''condition2: data1和data2都有 & data2['intens']/data1['intens'] > 2'''
        common2 = pd.merge(data1, data2, on=['formula'],suffixes=('_data1','_data2'))
        condition = (common2['intens_data2'] / common2['intens_data1']) > 2
        intens_bigthan_2 = common2[condition]
        Part2_intens_biggerthan2 = intens_bigthan_2.iloc[:,:27]


        '''Part1 and Part2'''
        Part1_only_in_data2.columns = self.columns_name
        Part2_intens_biggerthan2.columns = self.columns_name
        Generate_data = pd.concat([Part1_only_in_data2, Part2_intens_biggerthan2], ignore_index=True).drop_duplicates()

        return Generate_data

    def Resistance(self,data1, data2):
        '''反应前后都有 并且 data2['intens']/data1['intens'] - 【0.5-2】 '''
        common = pd.merge(data1, data2, on=['formula'], how='inner', suffixes=('_data1', '_data2'))
        condition = ((common['intens_data2'] / common['intens_data1']) <= 2) & (
                    (common['intens_data2'] / common['intens_data1']) >= 0.5)
        Resistance_data = common[condition]
        Resistance_data = Resistance_data.iloc[:, :27]
        Resistance_data.columns = self.columns_name
        return Resistance_data














