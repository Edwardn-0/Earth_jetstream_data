import pandas as pd

i = 0
year = 2010

def file_change():
    base = r'Database/Earth_speed_Data/OBS_SONDE_F00508_'
    body = {
        '20250518140221',
        '20250518140257',
        '20250518140329',
        '20250518140413',
        '20250518140454',
        '20250518140737'
    }
    return [f'{base}{bd}.csv'for bd in body]

def file_path():
    global data
    file = file_change()
    file = file[i]
    data = pd.read_csv(file, header=0, encoding='cp949')

def Find(data_name):
    knot_max = data['풍속(knot)'].max()
    gpm_max = data['고도(gpm)'].max()
    hPa_max = data['기압(hPa)'].max()
    deg_max = data['풍향(deg)'].max()
    return knot_max,gpm_max,hPa_max,deg_max

def search():
    result = Find(data)
    print(f'{year+i}년도 제트기류 속도: ')
    print(f'최대 풍속: {result[0]} m/s')
    print(f'고도: {result[1]} m')
    print(f'기압: {result[2]} hPa')
    print(f'풍향: {result[3]}')
    print('----------------------')

file_list = file_change()
for d in range(len(file_list)):
    file_path()
    search()
    i+=1