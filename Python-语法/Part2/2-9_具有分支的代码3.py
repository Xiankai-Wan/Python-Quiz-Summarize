# 练习：使用多个返回值编写自己的函数
# cylinder_surface_area 函数用于计算实心或空心圆柱的表面积。has_top_and_bottom 参数是 True 或 False 取决于圆柱体是实心还是空心。实心圆柱体的表面积包括顶部和底部的面积
#
# 重新构建该函数定义，使其在函数体中具有两个 return 语句。

def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        return side_area + (3.14 * radius ** 2)*2
    else:
        return 3.14 * radius ** 2
        
