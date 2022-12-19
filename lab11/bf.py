import json

def BF(input):
    a=len(input)
    b=len(input[0])
    result_0123=[[]]
    list_append_len=[]
    
    for p in range(b): 
      list_append_len.append(p)
      
    class Solution(object):
       def permute(self, nums):
          result = []
          self.permute_util(nums,0,[],result)
          return result
       def permute_util(self,given_list,start,curr,result):
          if start > len(given_list)-1:
             result.append(curr)
             return
          for i in range(start,len(given_list)):
            self.swap(given_list,start,start+(i-start)) 
            self.permute_util(given_list,start+1,curr+[given_list[start]],result)
            self.swap(given_list, start, start + (i - start))
       def swap(self,nums,index1,index2):
          temp = nums[index1]
          nums[index1] = nums[index2]
          nums[index2] = temp
    result_0123=Solution().permute(list_append_len)
    
    a=len(result_0123)
    b=len(result_0123[0])
    
    result_job=[]
    for m in range(a):
      result_job.append([])
      for n in range(b):
        result_job[m].append(input[n][result_0123[m][n]])
    
    cost=(sum(result_job[0])+1)
    for t in range(a):
      if sum(result_job[t])<cost:
        cost=sum(result_job[t])
        assignment=result_0123[t]
      else:
        pass
    return assignment, cost


with open('input.json', 'r') as inputFile:
    data = json.load(inputFile) 
    for key in data:
        input = data[key]
        assignment, cost = BF(input)

        print('Question: ' + str(key))
        print('Assignment:', assignment)
        print('Cost:', cost)
        print()