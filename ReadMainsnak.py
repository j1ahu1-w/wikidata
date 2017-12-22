# python 3
# -*- coding: utf-8 -*-
# w_j1ahu1@163.com

import json
import pymysql

path = 'wikidata.json'

con = pymysql.connect(host="localhost", port=3306, user="root", passwd="mysqlrandow", db="wikidata", charset="utf8")
cur = con.cursor()

def insert_mainsnak(json_data):
    for key in json_data['claims']:
        Claim_arrays = json_data['claims'][key]
        for c in Claim_arrays:
            id = json_data['id']
            snaktype = c['mainsnak']['snaktype']
            properties = c['mainsnak']['property']
            datatype = c['mainsnak']['datatype']
            if 'datavalue' in c['mainsnak']:
                datavalue_value = json.dumps(c['mainsnak']['datavalue']['value']).replace('\'', '').replace('}','').replace('{','')
                datavalue_type = c['mainsnak']['datavalue']['type']
            else:
                datavalue_value = None
                datavalue_type = None

            '''print('id:',id)
            print(snaktype)
            print(properties)
            print(datatype)
            print(datavalue_value)
            print(datavalue_type)
            print('---------------------------------------------------')'''
            try:
                sql = "insert into mainsnak(id, snaktype, properties, datatype, datavalue_value, datavalue_type) values('%s','%s','%s','%s','%s','%s');" % (
                    id, snaktype, properties, datatype, datavalue_value, datavalue_type)
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
                insert_mainsnak(json_data)
    cur.close()
    con.close()
    print('MainSnak 存储成功!')

if __name__=='__main__':
    main()