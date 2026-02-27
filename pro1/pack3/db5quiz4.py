# 문4)직원별 관리 고객 수 출력 (관리 고객이 없으면 출력에서 제외)
# 직원번호 직원명 관리 고객 수
# 1 홍길동 3
# 2 한송이 1

import MySQLdb
import pickle

with open('mydb.dat', mode = 'rb') as obj:
    config = pickle.load(obj)

def chulbal3():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        sql = """
        SELECT jikwonno AS 직원번호, jikwonname AS 직원명,
        COUNT(gogekdamsano) AS 관리고객수 
        FROM jikwon 
        inner JOIN gogek ON jikwonno=gogekdamsano 
        GROUP BY jikwonname
        """
    
        cursor.execute(sql)

        datas = cursor.fetchall()

        if len(datas)== 0:
            print("다시 입력하세요.")
            return   # sys.exit(0)
    
        for jikwonno, jikwonname, gogekdamsano in datas:
            print(jikwonno, jikwonname, gogekdamsano)

        print('인원수: ', str(len(datas)))

    except Exception as e:
        print ('err: ', e)
    finally:
        cursor.close()
        conn.close()

if __name__=="__main__":
    chulbal3()