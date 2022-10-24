# import necessary libraries
import pandas as pd
import os
import glob

# use glob to get all the csv files
# in the folder
path = os.getcwd()
#csv_files = glob.glob(os.path.join(path, "*.csv"))
csv_files = glob.glob(os.path.join(path, "DataFiles\*.csv"))

print(type(csv_files))
for fileName in csv_files:
    print(fileName)
csv_files_len = len(csv_files)
print("CSV files length=")
print(csv_files_len)

print("---------------------------------")
for i in range(1, len(csv_files)):
    print(csv_files[i])

print("-------------- df_one  -------------------")
df_one = pd.read_csv(csv_files[0], index_col=None, header=0)
df_one.columns.values[0:1] =["Title" ]
#print(df_one.info())
print(df_one.head(1111))

print("--------------  DF_two -------------------")
#df_two = pd.read_csv(csv_files[1], index_col=None, header=0)
#print(df_two.info())
#print(df_two.head(1111))

print("--------------  DF_three -------------------")

#df_one =pd.concat([df_one, df_two],axis=0,ignore_index=True)
#print(df_three.info())
#print(df_one.head(1111))

print("--------------  loop -------------------")

# loop over the list of csv files
#for f in csv_files:
for i in range(1, len(csv_files)  ):
    # read the csv file
    #df = pd.read_csv(f, index_col=None, header=0)
    df = pd.read_csv(csv_files[i], index_col=None, header=0)
    df.columns.values[0:1] = ["Title"]

    # print the location and filename
    print('Location:', csv_files[i])
    print('File Name:', csv_files[i].split("\\")[-1])

    # print the content
    #print('Content:')
    #print(df.info())
    #print(df.head(111))
    #print("----------------- Append ----------------------")
    #df_one =pd.concat([df_one, df],  ignore_index=True, verify_integrity= False)
    df_one = pd.concat([df_one, df], axis=0, ignore_index=True)
    #print(df_one.head(1111))

df_one.sort_values(by=['First Name', 'Last Name'], ascending=[True, True], na_position='first',inplace=True)

df_one.drop_duplicates(subset=["First Name", "Last Name", "E-mail Address"], inplace=True)
#df_one.drop_duplicates(subset=["First Name"], inplace=True)

print("----------------- Final ----------------------")
print(df_one.info())
print(df_one.head(1111))
df_one.to_csv('CSV_Output\contact.csv', index=False)