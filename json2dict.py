import json

def json2dict(filename):
    dict = []
    with open(filename, 'r', encoding='utf8') as f:
        for obj in f.readlines():
            if obj == '\n': # empty lines will cause format error of json decoder
                continue
            else:
                temp = json.loads(obj)
                print(temp)
                dict.append(temp)
    return dict

if __name__ == '__main__':
    filename = '分拣 垃圾_201512.txt'
    dict = json2dict(filename)
