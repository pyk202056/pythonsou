import MySQLdb

config = { 'host': '127.0.0.1', 'user':'root', 'password':'123', 'database':'test','port':3306,'charset':'utf8'}

def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        
        jikno=int(input("직원번호 입력 : "))
        jikname=str(input("직원명 입력: "))
        sql ="""
    	select j.jikwonno as 직원번호 ,j.jikwonname as 직원명, b.buserno as 부서명, b.busertel as 부서전화, j.jikwonjik as 직급, j.jikwongen as 성별
	    from jikwon j
	    inner join buser b
	    on j.busernum=b.buserno
	    where j.jikwonno='{0}' and j.jikwonname='{1}'
        """.format(jikno, jikname)

        cursor.execute(sql)

        datas = cursor.fetchall()
        # print(datas)

        if len(datas)== 0:
            print("다시 입력하세요")
            return 
    
        for jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen in datas:
            print(jikwonno, jikwonname, busername,busertel, jikwonjik, jikwongen)

    except Exception as e:
        print ('err: ', e)
    finally:
        cursor.close()
        conn.close()

if __name__=="__main__":
    chulbal()