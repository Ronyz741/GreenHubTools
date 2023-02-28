import json

if __name__ == '__main__':
    file_path = 'C:/Users/10187/AppData/Roaming/GreenHub/config.json'
    file = open(file_path, 'r', encoding='utf-8')
    dic_data = json.load(file)
    file.close()

    try:
        remaining_time = int(input('请输入需要使用的时间(Enter默认为60分钟)：'))
    except:
        remaining_time = 60

    dic_data['today-use-minute']['minutes'] = remaining_time
    json_write = json.dumps(dic_data)

    file = open(file_path, 'w', encoding='utf-8')
    file.write(json_write)
    file.close()
