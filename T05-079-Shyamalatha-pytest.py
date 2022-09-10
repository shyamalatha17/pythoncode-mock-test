# 1. Implement palindrome using iterator(for loop) and generator mechanism.
#
# Steps to be followed:
#
# 1.1. input from user
# 2. reverse number using generator
#     2.1 first create a function reverse no and pass the number for reverse
#     2.2 use while loop till number would be 0
#     2.3 yield the rem
# 3. create a function for collecting no from separate digit
# 4. check user input and reversed no same or not
#     4.1 if same then its palindrome
#     4.2 else not a paindrome

# print("Enter the no for checking the number is palindrome or not")
# inp = int(input(": "))
#
# def seperating_digit(num):
#     while num > 0:
#         rem = num % 10
#         num = num // 10
#         yield rem
#
# def reverse_num(user):
#     reverse_digit = 0
#     for i in seperating_digit(user):
#         reverse_digit = (reverse_digit * 10) + i
#     return reverse_digit
#
# if inp == reverse_num(inp):
#      print("the no is palindrome")
# else:
#      print("not a palindrome no.")


# print("--------------------------Program 2 ----------------------------------")
# print("""2. Sum of 2 digits into output
# n1 = 1234 # int(input("Enter number1 :" ))
# n2 = 9999 # int(input("Enter number2 :" ))
# Output: 9+1 2+9 3+9 4+9
# 10 + 11 + 12 + 13 = 46""")

# print()
# n1 = int(input("Enter the first numbers: "))
# n2 = int(input("Enter the first numbers: "))
#
# list_n1 = [i for i in seperating_digit(n1)]
# list_n2 = [i for i in seperating_digit(n2)]
#
# list_n1.sort()
# list_n2.sort()
#
# total = []
#
# for no_1, no_2 in zip(list_n1, list_n2):
#     print(f" {no_1} + {no_2}", end=",")
#     total.append(no_1 + no_2)
#
# print()
# for i in total:
#     if i == total[-1]:
#         print(i)
#     else:
#         print(f" {i} +", end="  ")
#
# print(f"{sum(total)}")

# print("--------------------------Program 3 ----------------------------------")
# print("""3. st = "ab@#cd!ef"
#    Reverse string considering only alphabets. Symbols should not be reversed
#    # Output: fe@#dc!ba""")

# st = "ab@#cd!ef"
#
#
# # convert string into list
# listSample = list(st)
#
# i = 0
# j = len(listSample) - 1
#
# while i < j:
#     if not listSample[i].isalpha():
#         i += 1
#     elif not listSample[j].isalpha():
#         j -= 1
#     else:
#         # swap the element in the list
#         # if both elements are alphabets
#         listSample[i], listSample[j] = listSample[j], listSample[i]
#         i += 1
#         j -= 1
#
# # convert list into string
# # by concatinating each element in the list
# strOut = ''.join(listSample)
# print(strOut)

# program(----------------4---------------------)
#
# 4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
#    #findout elements duplicate count output in  dict format


# some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
# occurrences_of_char = {}
#
# for i in some_list:
#     if i not in occurrences_of_char:
#         occurrences_of_char[i] = 1
#     else:
#         occurrences_of_char[i] += 1
#
# print(occurrences_of_char)
#
# new_dict = {}
# for k, v in occurrences_of_char.items():
#     if v <= 1:
#         pass
#     else:
#         new_dict[k] = v
#
# print(new_dict)


# program(----------------5----------------------)
5. # t1 = (1, 2, 3, "a", "c")
   # t2 = ("b", "d", 9, 8, 7)
   # Output: (10,10,10,"ab","cd")


# t1 = (1, 2, 3, "a", "c")
# t2 = ("b", "d", 9, 8, 7)
#
#
# def sort_ele_of_diff_types_t1(inp):
#     strs = list(filter(lambda x: type(x) == str, inp))
#     ints = list(filter(lambda x: type(x) == int, inp))
#
#     output = sorted(ints) + sorted(strs)
#     return output
#

# def sort_ele_of_diff_types(inp):
#     strs = list(filter(lambda x: type(x) == str, inp))
#     ints = list(filter(lambda x: type(x) == int, inp))
#
#     output = sorted(ints, reverse=True) + sorted(strs)
#     return output
#
#
# list_of_t1 = sort_ele_of_diff_types_t1(t1)
# list_of_t2 = sort_ele_of_diff_types(t2)
#
# for t_1, t_2 in zip(list_of_t1, list_of_t2):
#     print(t_1 + t_2)

6  #Write a Python program to remove leading zeros from an IP address.
			  # inp = "216.08.094.196"
			# o/p =  216.8.94.196

# inp = "216.08.094.196"
# def removing_leading_zeros(user_input):
#     list_of_inputs = user_input.split(".")
#     result = []
#     for each_ele in list_of_inputs:
#         result.append(each_ele.lstrip("0"))
#     print(".".join(result))
#
# removing_leading_zeros(inp)

# program(----------------7--------------------)
# 7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
   #output= [1,2,3,4,5,6,7,8,9,10]

# # input list
# l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
#
# # output list
# output = []
#
# # function used for removing nested
# # lists in python using recursion
# def reemovNestings(l):
#     for i in l:
#         if type(i) == list:
#             reemovNestings(i)
#         else:
#             output.append(i)
# # Driver code
# print('The original list: ', l)
# reemovNestings(l)
# print('The list after removing nesting: ', output)

# Program(----------8-----------)
# Load sample content in text file.
# Read data and find
# 1.No of lines in file
# 2. No of words in each line
# 3.No of chars in each line
# 4.No of vowels and consonants
# 5.No of special chars linewise and total

with open("_02_ Variables/sample.txt", "r") as file:
    file_content = file.read()
    print("the no. of lines in file is ",  len(file_content.split("\n")))
    words_count = 0
    chars_count = 0
    vowels = 0
    consonant = 0
    for i in file_content.split("\n"):
        for j in i.split(" "):
            if not j.isalpha() and not j.isalnum():
                continue
            else:
                words_count += 1

        for j in i:
            if not j.isalpha() and not j.isalnum():
                continue
            else:
                chars_count += 1

        for j in i:
            if j.lower() in "aeiou":
                vowels += 1
            else:
                consonant += 1

    print("the total words in file is ", words_count)
    print("the total words in file is ", chars_count)
    print("the total vowels in file is ", vowels)
    print("the total consonant in file is ", consonant)
