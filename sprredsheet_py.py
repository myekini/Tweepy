import gspread
import pygsheets
import pandas as pd

#1 -- using gspread
s_p = gspread.service_account()
my_sh = s_p.open('twitter_users')
wk_sh = my_sh.worksheet("RealTimeBI")

#print("Rows: ", wk_sh.row_count)
#print("Column: ",wk_sh.col_count)

#getting the first cell
print(wk_sh.acell('A1').value)
#wk_sh.update('A2:A5', [['myekini'], ['hiddy'], ['shakede']])

# 2 -- using pygsheets/pandas
gc = pygsheets.authorize(service_file='service_account.json')
# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['John', 'Steve', 'Sarah']

#open the google spreadsheet
sh = gc.open('twitter_users')

wks = sh[0]

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(df,(1,1))