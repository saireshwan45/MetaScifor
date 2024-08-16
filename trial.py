# class Evenodd:
#     def __init__(self,num):
#         self.num = num
#     def oddeven(self):
#         if self.num % 2 == 0:
#             return "Even Number"
#         else:
#             return "Odd number"
# run = Evenodd(3)
# print(run.oddeven())
from django.template.defaultfilters import length

# start_num = int(input("Enter a starting number?"))
# stop_num = int(input("Enter a stopping number?"))
# list1 = []
# for i in range(start_num,stop_num+1):
#     if i % 2 == 0:
#         list1.append(i)
# print(list1)




#Armstrong Number
#
# input_value = int(input("Enter a number?"))
# input_str = str(input_value)
# length1 = len(input_str)
# armstrong_number = 0
# for num in input_str:
#     armstrong_number += int(num) ** length1
# if armstrong_number == input_value:
#         print("Armstrong")
# else:
#         print("Not Armstrong")



#
def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
arr = [21,12,42,13,41,421,553,643,7,36,3]
bubble_sort(arr)
print("Sorted array is :")
for i in range(len(arr)):
    print(arr[i],end=",")




#
# a = int(input("Enter a number?"))
# b = int(input("Enter a number?"))
# print("Before swapped value of a is:",a)
# print("Before swapped value of b is:",b)
# # 1#a,b = b,a #Tuple Unpacking
# # 2#using a temp variable:
# # #temp = a
# # # a = b
# # # b = temp
# # 3#Using arithmetic Operations
# # # a = a+b
# # # b = a-b
# # # a = a-b
# #4-Using XOR
# #a = a ^ b
# #b = a ^ b
# #a = a ^ b
# print("After swapped value of a is:",a)
# print("After swapped value of b is:",b)





































