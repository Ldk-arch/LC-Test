#confing utf-8
def fun(i):
    standard = 3500  # 扣除标准为3500
    fiveInsurancesUp = 7662  # 五险一金缴纳上限为7662；超过部分就按7662缴纳
    endowmentInsurance = i * 0.08  # 养老保险
    medicare = i * 0.02  # 医疗保险
    unemploymentInsurance = i * 0.005  # 失业保险
    maternityInsurance = i * 0.006  # 生育保险
    employmentInjuryInsurance = i * 0.01  # 工伤保险
    HousingInsurance = i * 0.12  # 住房公积金

    fiveInsurances = endowmentInsurance + medicare + unemploymentInsurance + maternityInsurance + employmentInjuryInsurance + HousingInsurance
    #五险一金总金额

    if fiveInsurances > fiveInsurancesUp:
        fiveInsurances = fiveInsurancesUp

            #应缴纳个人所得税
    payable = i - fiveInsurances - standard
    if payable <= 0:
        nasui = 0
    else:
        if payable<1500:
            nasui = payable*0.03- 0
        elif payable >= 1500 and payable < 4500:
            nasui = (payable*0.1-105)
        elif payable >= 4500 and payable < 9000:
            nasui= (payable*0.2-555)
        elif payable >= 9000 and payable < 35000:
            nasui = (payable*0.25-1005)
        elif payable >= 35000 and payable < 55000:
            nasui= (payable*0.3-2002)
        elif payable >= 55000 and payable < 80000:
            nasui = payable*0.35-5505
        elif payable >= 80000:
            nasui = payable*0.45-13505

    return nasui

sum = 0
for i in range(10):
        monthMoney = float(input("月收入："))
        print('个人缴纳所得税：', fun(monthMoney))
        sum+= fun(monthMoney)


print('总纳税额：',sum)
C:\Users\10503\PycharmProjects\untitled\统计钞票数目.py