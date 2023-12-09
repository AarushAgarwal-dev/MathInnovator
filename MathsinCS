def hybrid_sort(data):
  """
  Sorts a list of numbers in ascending order using a hybrid approach of Bubble Sort and Quick Sort.

  Args:
    data: A list of numbers.

  Returns:
    A new list containing the sorted numbers.
  """
  if len(data) <= 10:
    # Use Bubble Sort for small lists
    return bubble_sort(data)
  else:
    # Use Quick Sort for larger lists
    return quick_sort(data)

def bubble_sort(data):
  """
  Sorts a list of numbers in ascending order using the Bubble Sort algorithm.

  Args:
    data: A list of numbers.

  Returns:
    A new list containing the sorted numbers.
  """
  sorted_data = data[:]
  swapped = True
  while swapped:
    swapped = False
    for i in range(len(sorted_data) - 1):
      if sorted_data[i] > sorted_data[i + 1]:
        sorted_data[i], sorted_data[i + 1] = sorted_data[i + 1], sorted_data[i]
        swapped = True
  return sorted_data

def quick_sort(data):
  """
  Sorts a list of numbers in ascending order using the Quick Sort algorithm.

  Args:
    data: A list of numbers.

  Returns:
    A new list containing the sorted numbers.
  """
  if len(data) <= 1:
    return data
  pivot = data[0]
  left = [x for x in data[1:] if x <= pivot]
  right = [x for x in data[1:] if x > pivot]
  return quick_sort(left) + [pivot] + quick_sort(right)

unsorted_data = [4, 2, 7, 5, 1]
sorted_data = hybrid_sort(unsorted_data)

print("Unsorted data:", unsorted_data)
print("Sorted data:", sorted_data)
