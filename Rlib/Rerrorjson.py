import json

def errorjson(errorcode:dict):
    """
    `errorcode` : dict 형식, json코드로 들어가야함.
        
    `_file` : file 위치 선언. 없는 경우. 실행 위치에 파일 생김
        
    ex. `_file = 'test\\'`
    """
        
    try:
        with open(file='./Rerror.json', mode='r', encoding='utf-8') as json_file:
            existing_data = json.load(json_file)
            existing_data['data'].append(errorcode)
    except FileNotFoundError:
        existing_data = {'data': [errorcode]}
        
    with open(file='./Rerror.json', mode='w', encoding='utf-8') as json_file:
        json.dump(existing_data, json_file)