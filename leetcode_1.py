nums = [2,7,11,15]
target = 9

output=[]
def func():
    for i in nums:
        ind=nums.index(i)
        ind_2=ind+1
        output.append(ind)
        output.append(ind_2)
        summ=nums[ind]+nums[ind_2]
        if summ==target:
            return output

func()
print(output)