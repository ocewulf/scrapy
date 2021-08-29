salary = int(input("请输入您的工资："))

if salary < 2000:
    tax = 0;
elif salary <= 4000:
    tax = (salary - 2000)*0.03
elif salary <= 6000:
    tax = 2000*0.03 + (salary - 4000)*0.05
elif salary <= 10000:
    tax = 2000*0.03 + (2000*0.05) + (salary - 6000)*0.08
else:
    tax = 2000*0.03 + (2000*0.05) + (salary - 6000)*0.08 + (salary - 10000)*0.2
income = salary - tax
print("您的到手工资为：" + str(income) + "元")
