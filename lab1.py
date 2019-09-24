
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""

   if int_list == None:
      raise ValueError
   elif len(int_list) == 0:
       return None
   else:
       max = int_list[0]
       for val in int_list:
           if max < val:
              max = val
   return max

   pass

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   i = 0
   if int_list == None:
      raise ValueError
   if len(int_list) != 2:
      int_list = [int_list, [len(int_list)]]
      print(int_list)
      print(int_list[1])
      int_list[1][0] = int_list[0][-1]
      del int_list[0][-1]
      print(int_list)
   int_list[1].append(int_list[0][-1])
   del int_list[0][-1]
   print(int_list)
   if int_list[0]== []:
       int_list = int_list[1]
       print(int_list)
       return int_list
   else:
       reverse_rec(int_list)


   pass

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass



list_int = [1, 2, 3, 4]

#x = max_list_iter(list_lint)
y = reverse_rec(list_int)