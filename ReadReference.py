# python 3
# -*- coding: utf-8 -*-
# w_j1ahu1@163.com

import json
import pymysql

path = 'wikidata.json'

con = pymysql.connect(host="localhost", port=3306, user="root", passwd="mysqlrandow", db="wikidata", charset="utf8")
cur = con.cursor()

def insert_reference(json_data):
    for key in json_data['claims']:
        Claim_arrays = json_data['claims'][key]
        for c in Claim_arrays:
            if 'references' in c:
                for references_key in c['references']:
                    for snak_key in references_key['snaks']:
                        for r in references_key['snaks'][snak_key]:
                            id = json_data['id']
                            rhash = references_key['hash']
                            snaktype = r['snaktype']
                            properties=r['property']
                            datatype = r['datatype']
                            if 'datavalue' in r:
                                datavalue_value = json.dumps(r['datavalue']['value']).replace('\'','').replace('}','').replace('{','')
                                datavalue_type = r['datavalue']['type']
                            else:
                                datavalue_value = None
                                datavalue_type = None
                            temp = references_key['snaks-order']
                            res = ''
                            if temp:
                                for i in temp:
                                    res = res + i + ' '
                                snakorder = res
                            else:
                                snakorder = None
                            '''print('id:',id)
                            print('rhash:',rhash)
                            print(snaktype)
                            print(properties)
                            print(datatype)
                            print(datavalue_value)
                            print(datavalue_type)
                            print(snakorder)
                            print('---------------------------------------------------')'''
                            try:
                                sql = "insert into reference(id, rhash, snaktype, properties,datatype, datavalue_value, datavalue_type,snakorder) values('%s','%s','%s','%s','%s','%s','%s','%s');" % (
                                    id, rhash, snaktype, properties,datatype, datavalue_value, datavalue_type,snakorder)
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
                insert_reference(json_data)
    cur.close()
    con.close()
    print('Reference 存储成功!')

if __name__=='__main__':
    main()