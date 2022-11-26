### <요구사항-2> 반영 ###
import pymysql

#-------------mySQL 연결 끝
#-------------함수 시작
def servConnect(sel, sql) : ### <요구사항-3> 반영 ###
    config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : 'root1234',
    'database' : 'test_db2',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True
    }
    conn = pymysql.connect(**config)
    corr = conn.cursor()
    corr.execute(sql)
    if sel == 'alone' :
        None
    elif sel == 'commit' :
        conn.commit()
    elif sel == 'fetch' :
        rerult = corr.fetchall()
        corr.close()
        conn.close()
        return rerult
    corr.close()
    conn.close()

def inputFilter(par, stri) : #TableCrud.TableLoader, TableView.LookMerge 의 인수를 par의 갯수만큼 생성하며 int, str, float 형식으로 필터링 하는 함수
    try :
        tmp = []
        for i in range(len(par)) :
            if par[i] == 'int' :
                tpIn = input(f'{stri[i]}')
                try :
                    int(tpIn)
                except :
                    None
                tmp += [tpIn]
            elif par[i] == 'str' :
                tpIn = input(f'{stri[i]}')
                try :
                    str(tpIn)
                except :
                    None
                tmp += [tpIn]
            elif par[i] == 'flo' :
                tpIn = input(f'{stri[i]}')
                try :
                    round(float(tpIn),-2) 
                except :
                    None
                tmp += [tpIn]
        return tmp
    except Exception as e :
        print('inputFilter 오류 : ', e)


