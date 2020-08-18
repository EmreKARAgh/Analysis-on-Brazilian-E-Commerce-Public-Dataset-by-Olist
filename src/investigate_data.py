# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:18:01 2020

@author: EmreKARA
"""

import pandas as pd
import os

def df_info(df):
    new_df = pd.DataFrame(index = df.columns)
    new_df['data_type'] = df.dtypes
    new_df['null_value_pct'] = df.isna().mean().round(4) * 100
    new_df['min_value'] = df.min()
    new_df['max_value'] = df.max()
    new_df['distinct_value_cnt'] = df.nunique()
    new_df.reset_index(inplace=True)
    new_df = new_df.rename(columns={'index':'column_name'})
    
    return new_df

        
ROOT_DIR = os.path.abspath(os.path.join(__file__, '..','..'))
DATA_DIR = os.path.abspath(os.path.join(ROOT_DIR, 'data'))
INFO_DIR = os.path.abspath(os.path.join(ROOT_DIR, 'data','info'))

csv_files = [f for f in os.listdir(DATA_DIR) if str(f).endswith('.csv')]

data_frames = {}
for file in csv_files:
    data_frames[file[:-4]] = pd.read_csv(os.path.join(DATA_DIR, file))

data_frame_infos = {}
for df in data_frames:
    # print(data_frames[df].describe(), end='\n---------------------------\n\n')
    # a = data_frames[df].describe()
    info = df_info(data_frames[df])
    data_frame_infos[df] = info
    info.to_csv(os.path.join(INFO_DIR,('info_'+df+'.csv')),index=False)