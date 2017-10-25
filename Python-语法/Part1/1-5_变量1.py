# 练习：赋值和修改变量
# 现在该你尝试一下变量了，该练习中的注释（以 # 开头的行）具有创建和修改变量的说明。每个注释后都要按注释说明编写一行对应功能的代码。
#
# 请注意，此代码使用科学计数法定义大的数字。4.445e8 等于 4.445 * 10 ** 8，也等于 444500000.0。

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= 0.9
# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5
# print the new value of the reservoir_volume variable
print(reservoir_volume)
