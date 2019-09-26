
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
   if int_list == None:
      raise ValueError
   if len(int_list) <= 1:
      return int_list
   if type(int_list[1]) != list:
      int_list = [int_list, [len(int_list)]]
      int_list[1][0] = int_list[0][-1]
      del int_list[0][-1]
   int_list[1].append(int_list[0][-1])
   del int_list[0][-1]
   if int_list[0]== []:
       int_list = int_list[1]
       return int_list
   return reverse_rec(int_list)


   pass


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
       raise ValueError
   mid = (low + high) // 2
   if len(int_list) == 1 and int_list[0] != target:
       return None
   if target not in int_list:
       return None
   if int_list[mid] == target:
       return mid
   if int_list[mid] > target:
       high = mid
   else:
       low = mid
   return bin_search(target, low, high, int_list)


   pass



int_list = [2, 3, 6, 9, 14, 21, 22, 23, 34, 35, 45, 46, 47, 48]

#x = max_list_iter(list_lint)
y = reverse_rec([1,2,3]),
z = bin_search(22, 0, len(int_list) - 1, int_list)