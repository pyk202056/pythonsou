import MySQLdb                 # MySQL / MariaDB 연결 라이브러리
import json                    # Python 객체 → JSON 문자열 변환용 모듈

conn = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="123",
    db="test",
    charset="utf8"
)

try:
    cur = conn.cursor() # 기본 커서 (결과가 tuple 형태로 반환됨)
    cur.execute("SELECT * FROM sangdata")

    # 컬럼명 가져오기
    columns = [col[0] for col in cur.description]
    # cur.description → 컬럼 정보
    # col[0] → 컬럼 이름만 추출

    rows = cur.fetchall()

    # tuple → dict 변환
    result = []
    for row in rows:
        row_dict = dict(zip(columns, row))  # 컬럼명과 값 묶기
        result.append(row_dict)

    # JSON 변환
    json_data = json.dumps(result, ensure_ascii=False, indent=2)
    # ensure_ascii=False → 한글 깨짐 방지
    # indent=2 → 보기 좋게 들여쓰기

    print(json_data)
finally:
    cur.close()
    conn.close()