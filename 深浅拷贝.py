lst1 = ["金毛狮王", "紫衫龙王", "青翼蝠王", "白眉鹰王"]
# lst2 = lst1
lst2 = lst1[:]
lst1.append("张无忌")
print(lst2)
print(id(lst1))
print(id(lst2))