# 1. Write a program that can find area of a triangle. It should take base and height as
# an input from user and using that it should print an area of a triangle
print("计算三角形的面积小程序")
base=input("Enter base 底边长度:")
height=input("Enter height 高度:")
area=(1/2)*float(base)*float(height)
print("三角形的面积是:",area)
# 2. Write a program that takes file name with extension as an input and
# prints just the file name without extension (you can assume that file extensions
# are always 3 character long)

file_name = input("输入带后缀的文件名:")
print("不带后缀的文件名（去除最后4个字符）:",file_name[:len(file_name)-4])