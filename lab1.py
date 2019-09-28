
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""

   if int_list == None:                  #If the list doesn't exist a ValueError will be raised
      raise ValueError
   elif len(int_list) == 0:              #If there is nothing in the list then None is returned
       return None
   else:
       max = int_list[0]                 #Sets the max to the first value in the list
       for val in int_list:              #Goes through list comparing max to current value
           if max < val:                 #If the current value is greater than max then the max is changed to be the current value
              max = val
   return max                            #Returns the max of the list

   pass


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:                               #If the list doesn't exist a ValueError is raised
      raise ValueError
   if len(int_list) <= 1:                             #If the length if the list is 1 or less the list is returned as it is the reverse already
      return int_list
   if type(int_list[1]) != list:                      #Checks to see if the second element in the list is a list
      int_list = [int_list, [len(int_list)]]          #Makes the list into a list containing two lists. THe first being the original and the second an empty list
      int_list[1][0] = int_list[0][-1]                #Sets the first element of the second list to the last element of the original list
      del int_list[0][-1]                             #Deletes the the last element of the original list
   int_list[1].append(int_list[0][-1])                #Adds the last element of the original list to the end of the second list
   del int_list[0][-1]                                #Deletes the last element of the original list
   if int_list[0]== []:                               #If the original list is empty then the list become the second list which is the original list reversed
       int_list = int_list[1]
       return int_list                                #Returns the reversed list
   return reverse_rec(int_list)                       #Recursively calls the function to redo the process


   pass


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:                               #If the list doesn't exist a ValueError is raised
       raise ValueError
   mid = (low + high) // 2                            #Sets mid to the midpoint of high and low
   if int_list == []:                                 #Returns None if the list is empty
       return None
   if int_list[mid] == target:                        #If the mid is equal to the target to mid is returned
       return mid
   if mid == high and mid == low:                     #If the mid is equal to the high and the low then None is returned since it was already checked against the target
       return None
   if int_list[mid] > target:                         #Checks if the mid value of the list is greater than the target
       high = mid - 1                                 #The high value is changed to 1 below the mid value
       if high < 0:                                   #If the high value is negative it is changed back to 0
           high = 0
   else:
       low = mid + 1                                  #The low value is set to 1 above the mid value
   return bin_search(target, low, high, int_list)     #Recursively calls the function to repeat the process


   pass


