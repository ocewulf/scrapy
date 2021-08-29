import copy

lst1 = ["金毛狮王", "紫衫龙王", "青翼蝠王", "白眉鹰王",["段誉", "乔峰", "金轮法王"]]
# lst2 = lst1
# 浅拷贝
# lst2 = lst1[:]
# lst2 = lst1.copy()
# 深拷贝
lst2 = copy.deepcopy(lst1)
# lst1.append("张无忌")
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))