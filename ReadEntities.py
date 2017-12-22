# python 3
# -*- coding: utf-8 -*-
# w_j1ahu1@163.com

import json
import pymysql

path = 'wikidata.json'

con = pymysql.connect(host="localhost", port=3306, user="root", passwd="mysqlrandow", db="wikidata", charset="utf8")
cur = con.cursor()

def insert_entities(json_data):
    id = json_data['id']
    etype = json_data['type']
    if 'zh-hans' in json_data['labels']:
        cnlabels = json_data['labels']['zh-hans']['value']
    elif 'zh' in json_data['labels']:
        cnlabels = json_data['labels']['zh']['value']
    elif 'zh-cn' in json_data['labels']:
        cnlabels = json_data['labels']['zh-cn']['value']
    else:
        cnlabels = None

    if 'en' in json_data['labels']:
        enlabels = json_data['labels']['en']['value']
    else:
        enlabels = None

    if 'zh-hans' in json_data['descriptions']:
        descriptions = str(json_data['descriptions']['zh-hans']['value']).replace('\'', '')
    elif 'zh' in json_data['descriptions']:
        descriptions = str(json_data['descriptions']['zh']['value']).replace('\'', '')
    elif 'zh-cn' in json_data['descriptions']:
        descriptions = str(json_data['descriptions']['zh-cn']['value']).replace('\'', '')
    else:
        descriptions = None

    if 'en' in json_data['aliases']:
        temp = json_data['aliases']['en']
        res = ""
        if temp:
            for i in temp:
                res = res + i.get('value') + '  or  '
            aliases = res.replace('\'', '')
        else:
            aliases = None
    elif 'zh-hans' in json_data['aliases']:
        temp = json_data['aliases']['zh-hans']
        res = ""
        if temp:
            for i in temp:
                res = res + i.get('value') + '  or  '
            aliases = res.replace('\'', '')
        else:
            aliases = None
    elif 'zh' in json_data['aliases']:
        temp = json_data['aliases']['zh']
        res = ""
        if temp:
            for i in temp:
                res = res + i.get('value') + '  or  '
            aliases = res.replace('\'', '')
        else:
            aliases = None
    elif 'zh-cn' in json_data['aliases']:
        temp = json_data['aliases']['zh-cn']
        res = ""
        if temp:
            for i in temp:
                res = res + i.get('value') + '  or  '
            aliases = res.replace('\'', '')
        else:
            aliases = None
    else:
        aliases = None

    if enlabels:
        enlabels = enlabels.replace("'", "`")
    if cnlabels:
        cnlabels = cnlabels.replace("'", "`")

    '''print('id:', id)
    print('type:',etype)
    print(cnlabels)
    print(enlabels)
    print(descriptions)
    print(aliases)
    print('----------------------------')'''
    try:
        sql = "insert into entities(id,etype,cnlabels,enlabels,descriptions,aliases) values('%s','%s','%s','%s','%s','%s');" % (
            id, etype, cnlabels, enlabels, descriptions, aliases)
        cur.execute(sql)
        con.commit()
    except pymysql.err.InternalError:
        pass

def main():
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            if line[0] == '[':
                continue
            elif line[0] == ']':
                break
            else:
                line = line[:-2]
                json_data = json.loads(line)
                insert_entities(json_data)
    cur.close()
    con.close()
    print('Entities 存储成功!')

if __name__=='__main__':
    main()