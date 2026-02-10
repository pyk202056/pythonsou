from datetime import datetime

# 입력 함수
def inputfunc():
    # [사번, 이름, 기본급, 입사년도]
    datas = [
        [1, "강나루", 1500000, 2010],
        [2, "이바다", 2200000, 2018],
        [3, "박하늘", 3200000, 2005],
        [4, "최구름", 1800000, 2022],
    ]
    return datas


# 처리 함수
def processfunc(datas):
    current_year = datetime.now().year
    count = 0

    print("사번  이름    기본급    근무년수  근속수당  공제액    수령액")
    print("-" * 60)

    for emp in datas:
        sabun, name, base_pay, hire_year = emp

        # 근무년수
        work_years = current_year - hire_year

        # 근속수당
        if work_years <= 3:
            bonus = 150000
        elif work_years <= 8:
            bonus = 450000
        else:
            bonus = 1000000

        # 급여액
        salary = base_pay + bonus

        # 공제세율
        if salary >= 3000000:
            tax_rate = 0.5
        elif salary >= 2000000:
            tax_rate = 0.3
        else:
            tax_rate = 0.15

        # 공제액, 수령액
        tax = int(salary * tax_rate)
        receive = salary - tax

        print(f"{sabun:<4} {name:<6} {base_pay:<9} {work_years:<8} {bonus:<9} {tax:<8} {receive}")

        count += 1

    print("\n처리 건수 :", count, "건")


# 메인 실행부
datas = inputfunc()
processfunc(datas)
