class mappingPipeline:

    def __init__(self):
        self.RUR_URBmap = {}
        self.HARM_EVmap = {}
        self.LGT_CONDmap = {}
        self.WEATHERmap = {}
        self.OWNERmap = {}
        self.J_KNIFEmap = {}
        self.L_STATUSmap = {}
        self.SPEEDRELmap = {}



        self.RUR_URB_init()
        self.HARM_EV_init()
        self.LGT_COND_init()
        self.WEATHER_init()
        self.OWNER_init()
        self.J_KNIFE_init()
        self.L_STATUS_init()
        self.SPEEDREL_init()


        self.col_list = [('RUR_URB', self.RUR_URBmap) , ('HARM_EV', self.HARM_EVmap), ('LGT_COND', self.LGT_CONDmap), ('WEATHER', self.WEATHERmap),('OWNER', self.OWNERmap), ('J_KNIFE', self.J_KNIFEmap), ('L_STATUS', self.L_STATUSmap), ('SPEEDREL', self.SPEEDRELmap)]

        

    def assign_mappings(self,df):
        for pair in self.col_list:
            col_name = pair[0]
            col_map = pair[1]
            #validate col name:
            if col_name not in df.columns.tolist():
                print(f"Column not found {col_name}")
                break
            df[col_name] = df[col_name].map(col_map)

        #Each tuple in this list represents a column name and a list of values to be converted to 0 for "unknown"
        unknown_conversions = [("FUNC_SYS", [96,98,99]), ("TYP_INT", [98,99,11]), ("REL_ROAD", [9]), ("MOD_YEAR", [9998, 9999]), ("GVWR_FROM", [98,99]), ("GVWR_TO", [98,99]), ("TRAV_SP", [997,998,999]), ("PREV_SPD", [99,998]), ("PREV_OTH", [99,998]), ("VNUMBER2", [5555,9999])]

        #Sometimes it is easier to simply replace only the unknown values instead of remapping the whole column
        for pair in unknown_conversions:
            col_name = pair[0]
            unknown_vals = pair[1]
            if col_name not in df.columns.tolist():
                print(f"Column not found {col_name}")
                break

            df[col_name] = df[col_name].replace(unknown_vals, 999)

        #for a few columns 0 is already assigned so it has to be changed first
        df['HOUR'] = df["HOUR"].replace(99, 999)
        df['MAN_COLL'] = df['MAN_COLL'].replace(0,999)
        df['RELJCT2'] = df['RELJCT2'].replace(
            to_replace=[98, 99, 3],  
            value=[999, 999, 2])

        return df
        




    
    def RUR_URB_init(self):
        list_999 = [6,8,9]
        list_1 = [1]
        list_2 = [2]

        self.RUR_URBmap.update({val: 999 for val in list_999})
        self.RUR_URBmap.update({val: 1 for val in list_1})
        self.RUR_URBmap.update({val: 2 for val in list_2})

    def HARM_EV_init(self):
        list_999 = [91,93,98,99]
        list_1 = [20,21,23,24,25,26,30,33,44,46,50,52,57,59]
        list_2 = [17,32,34,35,48,41,42,58]
        list_3 = [14,19,38,39,40,43,45,53]
        list_4 = [12,11,10,15,16,18,49,54,55,72,74]

        self.HARM_EVmap.update({val: 999 for val in list_999})
        self.HARM_EVmap.update({val: 1 for val in list_1})
        self.HARM_EVmap.update({val: 2 for val in list_2})
        self.HARM_EVmap.update({val: 3 for val in list_3})
        self.HARM_EVmap.update({val: 4 for val in list_4})

    def LGT_COND_init(self):
        list_999 = [7,8,9]
        list_1 = [1]
        list_2 = [3,2,6]
        list_3 = [4,5]

        self.LGT_CONDmap.update({val: 999 for val in list_999})
        self.LGT_CONDmap.update({val: 1 for val in list_1})
        self.LGT_CONDmap.update({val: 2 for val in list_2})
        self.LGT_CONDmap.update({val: 3 for val in list_3})

    def WEATHER_init(self):
        list_999 = [8,98,99]
        list_1 = [1]
        list_2 = [6]
        list_3 = [2]
        list_4 = [5,10,7]
        list_5 = [12,11,3,4]

        self.WEATHERmap.update({val: 999 for val in list_999})
        self.WEATHERmap.update({val: 1 for val in list_1})
        self.WEATHERmap.update({val: 2 for val in list_2})
        self.WEATHERmap.update({val: 3 for val in list_3})
        self.WEATHERmap.update({val: 4 for val in list_4})
        self.WEATHERmap.update({val: 5 for val in list_5})

    def OWNER_init(self):
        list_999 = [9]
        list_1 = [5,0]
        list_2 = [1,2,3,4,6]

        self.OWNERmap.update({val: 999 for val in list_999})
        self.OWNERmap.update({val: 1 for val in list_1})
        self.OWNERmap.update({val: 2 for val in list_2})

    def J_KNIFE_init(self):
        list_999 = [0]
        list_1 = [1]
        list_2 = [2,3]

        self.J_KNIFEmap.update({val: 999 for val in list_999})
        self.J_KNIFEmap.update({val: 1 for val in list_1})
        self.J_KNIFEmap.update({val: 2 for val in list_2})

    def L_STATUS_init(self):
        list_999 = [9,7]
        list_1 = [6]
        list_2 = [0,1,2,3,4]

        self.L_STATUSmap.update({val: 999 for val in list_999})
        self.L_STATUSmap.update({val: 1 for val in list_1})
        self.L_STATUSmap.update({val: 2 for val in list_2})

    def SPEEDREL_init(self):
        list_999 = [8,9]
        list_1 = [3,4,5,6]
        list_2 = [0]

        self.SPEEDRELmap.update({val: 999 for val in list_999})
        self.SPEEDRELmap.update({val: 1 for val in list_1})
        self.SPEEDRELmap.update({val: 2 for val in list_2})

    
    