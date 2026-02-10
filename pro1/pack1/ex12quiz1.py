# 문제 1
def inputfunc():
    datas = [
        [1, "강나루", 1500000, 2010],
        [2, "이바다", 2200000, 2018],
        [3, "박하늘", 3200000, 2005],
    ]
    return datas

def processfunc(datas):
    # datetime.now().year
    CURRENT_YEAR = 2026

    for data in datas:
        emp_no, name, base_pay, hire_year = data

        work_years = CURRENT_YEAR - hire_year

        if work_years <= 3:
            bonus = 150000
        elif work_years <= 8:
            bonus = 450000
        else:
            bonus = 1000000

        salary = base_pay + bonus

        if salary >= 3000000:
            tax_rate = 0.5
        elif salary >= 2000000:
            tax_rate = 0.3
        else:
            tax_rate = 0.15

        tax = int(salary * tax_rate)
        net_pay = salary - tax

        data.append(work_years)
        data.append(bonus)
        data.append(tax)
        data.append(net_pay)

    print("사번  이름    기본급    근무년수  근속수당  공제액    수령액")
    print("-" * 75)

    for d in datas:
        print(f"{d[0]:<4} {d[1]:<6} {d[2]:<8} {d[4]:<8} {d[5]:<8} {d[6]:<8} {d[7]}")

    print("-" * 75)
    print(f"처리 건수 : {len(datas)} 건")


datas = inputfunc()
processfunc(datas)

