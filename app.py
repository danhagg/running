import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import datetime

import pandas as pd

import xlrd
# import csv
# def csv_from_excel():
#     wb = xlrd.open_workbook('excel.xlsx')
#     sh = wb.sheet_by_name('all_combined')
#     a1 = sh.cell_value(rowx=0, colx=0)
#     a1_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(a1, wb.datemode))
#     print('datetime: %s' % a1_as_datetime)
#     your_csv_file = open('all.csv', 'w')
#     wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
#
#     for rownum in range(sh.nrows):
#         wr.writerow(sh.row_values(rownum))
#
#     your_csv_file.close()
#
# # runs the csv_from_excel function:
# csv_from_excel()


df = pd.read_csv('run_all.csv')
data_df = df[['date', 'type', 'rep-num', 'rep-len', 'pace', 'hr', 'temp']]
print(data_df)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Running Analysis'),

    html.Div(children='''
        EMTIR
    '''),

    dt.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in data_df.columns],
        data=data_df.to_dict('records'),
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
