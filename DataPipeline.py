import pandas as pd
import os

class file_directory:
    year = 0
    accident = ""
    vehicle = ""
    vevent = ""
    def __init__(self, year, acc, veh, vevent):
        self.year=year
        self.accident = acc
        self.vevent = vevent
        self.vehicle = veh





class pipeline:
    end_df = pd.DataFrame()
    
    file_directories = []

    df_list = {}

    def __init__(self, folders):
        self.create_directories(folders)
        
        

        for directory in self.file_directories:
            vehicledf = self.import_vehicle(directory.vehicle)
            veventdf = self.import_vevent(directory.vevent)

            accidentimport = self.import_accident(directory.accident)

            accidentdf = self.filter_moto(accidentimport, vehicledf)

            final_df = self.merge_dfs(accidentdf, vehicledf, veventdf)

            self.df_list[directory.year] = final_df



    def create_directories(self, folders):
        years = list(range(1987, 2024))
        
        #Create a file directory object for each folder and append them to the directories list
        for folder in folders:
            file_name = os.path.basename(folder)
            folder_year = 0
            for yr in years:
                if str(yr) in file_name:
                    folder_year = yr

            accident = f"{folder}\\accident.csv"
          
            vehicle = f"{folder}\\vehicle.csv"
            vevent = f"{folder}\\vevent.csv"

            directory = file_directory(folder_year, accident, vehicle, vevent)

            self.file_directories.append(directory)
                    
    
    
    def filter_moto(self, acc, veh):
        #returns the accident dataframe filtered to only inlcude accidents involving some form of motorcycle
        
        motorcycle_codes = [12,69,80,81,82,83,84,87,88,90,94,109,110,113,114,125,996]

        mask = veh['VPICBODYCLASS'].isin(motorcycle_codes)

        case_nums = veh['ST_CASE'][mask]

        df = acc['ST_CASE'].isin(case_nums)

        return acc[df]

    def merge_dfs(self, acc, veh, vevent):


        acc_veh = pd.merge(
            veh,
            acc,
            how = 'inner',
            on=["ST_CASE"]
        )
        df = pd.merge(
            acc_veh,
            vevent,
            how = 'inner',
            on=["ST_CASE", "VEH_NO"]
        )




        return df

    def import_accident(self, file_path):
        #returns a dataframe of the accident file with only the relevant features selected

        selected_cols = ["ST_CASE","VE_TOTAL", "VE_FORMS", "HOUR", "LGT_COND", "RUR_URB", "FUNC_SYS", 
                        "YEAR","HARM_EV", "MAN_COLL", "RELJCT2", "TYP_INT", "REL_ROAD", "WEATHER"]
        
        init_df = pd.read_csv(file_path, encoding='cp1252', low_memory=False)

        df = init_df[selected_cols].copy()

        return df

    def import_vehicle(self, file_path):
        selected_cols = ["ST_CASE", "VEH_NO", "OWNER", "MOD_YEAR","VPICBODYCLASS", "GVWR_FROM", "GVWR_TO",
                         "J_KNIFE", "TRAV_SP","DR_DRINK", "L_STATUS", "PREV_SPD",
                           "PREV_OTH", "SPEEDREL"]
        
        init_df = pd.read_csv(file_path, encoding='cp1252', low_memory=False)

        df = init_df[selected_cols].copy()

        return df
    
    
    
    def import_vevent(self, file_path):
        selected_cols = ["ST_CASE", "VEH_NO", "VNUMBER2"]

        init_df = pd.read_csv(file_path, encoding = 'cp1252', low_memory=False)

        df = init_df[selected_cols]

        return df
    



