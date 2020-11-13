# class Queue():
#     def __init__(self):
#         self.queue=[]

#     def enqueue(number):

#     def dequeue

#     def peek
#     def is_empty()


def removeDuplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(len(nums)): 
    	print(i,j)
    	print ("checking if they are the same:",nums[j],nums[i])
    	if nums[j] != nums[i]:
            i+=1
    	nums[i] = nums[j]
    return i + 1 