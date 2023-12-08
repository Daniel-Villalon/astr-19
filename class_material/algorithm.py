def quicksort(list):
  if len(list) <= 1:
    return list 
  
  pivot = list[0]
  lessThen_p = []
  moreThan_p = []

  for value in list[1:]:
    if value <= pivot:
      lessThen_p.append(value)
    else:
      moreThan_p.append(value)
    
  return quicksort(lessThen_p) + [pivot] + quicksort(moreThan_p)
      
    


l = [1, 3, 1, 4, 2, 6, 5, 2]
print(quicksort(l))