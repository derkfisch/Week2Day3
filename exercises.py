###Question 1


nums = [1, 3, 5, 7, 8]
new_num = []
for num in nums:
    if num:
        new_num.append(-num)
print(new_num)
        

####Question 2


# Hint: Look at the string methods! -- help(str)
sentence = "My phone number is (555)555-4321"

split_list = sentence.split(' ')

print(split_list)

nums = []

for num in split_list:
    if num.isdigit:
        nums.append(num)
print(nums)
 
    
#another code I tried to give back the numbers is

sentence2 = "My phone number is (555) 555 4321"
for nums2 in sentence2.split(' '):
    if nums2.isdigit():
        print(nums2)




####Question 3


digits = '123'

nums3=[]

for digit in digits:
    if digit.isdigit():
        digit = int(digit) + 1
        nums3.append(digit)
        
print(nums3)