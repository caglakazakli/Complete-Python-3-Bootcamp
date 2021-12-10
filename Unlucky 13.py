def sum13(nums):
  
  my_sum=sum(nums)
  
  for i in range(len(nums)):
    
    if nums[i]==13:
      
      my_sum-=nums[i]
      
      if i != len(nums)-1:
      
        my_sum-=nums[i+1]
        
      else:
        
        continue
      
    else:
      
      continue
      
  return my_sum    
  
    
      
