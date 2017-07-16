def sum13(nums):
    u=[]
    j=[]
    if len(nums)>0:                                          #this module take the indexes where 13 arrive as well the number come just after that
        for i in [i for i,x in enumerate(nums) if x==13]:
            u.append(i)
            u.append(i+1)
            
        if len(u)>0:                                     #This module is for test case if last value is 13 so it del the extra index entry from list "u"
          if max(u)==len(nums):
            u.remove(max(u))
            u.sort(reverse=True)
          
          i = 0                                             #This module is for when consecutive 13 value arrive so it delete duplicate entry in list "u"
          while i < len(u)-1:
            if u[i] == u[i+1]:
              del u[i]
            else:
              i = i+1
            
          for x in u:                                            #This loop give you the list of entry that you shopuld exclude in sum
            j.append(nums[x])
          
          return abs(sum(i for i in j)-sum(i for i in nums))      #This return the sum when there is 13 in array
        else:
          return (sum(i for i in nums))                         #This when there is no element = 13 in array
    else:
        return 0                                           #This when array in empty
            
            
    
