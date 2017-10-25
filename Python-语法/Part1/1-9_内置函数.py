# 练习：len
# 使用字符串连接并且使用 len 函数计算查理全名的长度。（是的，她对父母的选择不满意！）将该长度存储在 name_length 变量中。不要忘记名字的不同部分之间需要添加空格！

given_name = "Charlotte"
middle_names = "Hippopotamus"
family_name = "Turner"

name_length = len(given_name + " " + middle_names + " " + family_name)
#todo: calculate how long this name is

driving_licence_character_limit = 28
print(name_length <= driving_licence_character_limit)
