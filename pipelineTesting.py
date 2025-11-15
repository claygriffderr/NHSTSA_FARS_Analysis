import os
import pandas as pd

from DataPipeline import pipeline

from MappingPipeline import mappingPipeline


folder_paths= [r"C:\Users\Clayg\OneDrive\Desktop\College\Fall 25 classes\Machine Learning\RawData\FARS2020NationalCSV",
               r"c:\Users\Clayg\OneDrive\Desktop\College\Fall 25 classes\Machine Learning\RawData\FARS2021NationalCSV",
               r"c:\Users\Clayg\OneDrive\Desktop\College\Fall 25 classes\Machine Learning\RawData\FARS2022NationalCSV"]


testPipeline = pipeline(folder_paths)

directory = testPipeline.df_list

df2020 = directory[2020]
df2021 = directory[2021]
df2022 = directory[2022]

df = pd.concat([df2020, df2021, df2022])

#col_list = df.columns.to_list()

#duplicate_count = len(col_list)%len(list(set(col_list)))

#print(col_list)

mapping = mappingPipeline()

df = mapping.assign_mappings(df)

print(df['TRAV_SP'].describe())


