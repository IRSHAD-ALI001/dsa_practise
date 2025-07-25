############sellection sort############

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr  


# print(selection_sort([64, 25, 12, 22, 11]))  # Output: [11, 12, 22, 25, 64] 
# time complexity #
#  worst case O(n^2), space complexity O(1)
# best case O(n^2), average case O(n^2)



# #############bubble sort############
# backward bubble sort
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr


#  front bubble sort
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n-2, -1, -1):
#         isswapped = False
#         for j in range(0,i+1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 isswapped = True
#         if not isswapped:
#             break   
#     return   arr

#print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # Output: [11, 12, 22, 25, 34, 64, 90]
# time complexity #
#  worst case O(n^2), space complexity O(1)     
# best case O(n), average case O(n^2)





# #############insertion sort############ 
# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1, n):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
# print(insertion_sort([12, 11, 13, 5, 6]))  # Output: [5, 6, 11, 12, 13]
# # time complexity #
# #  worst case O(n^2), space complexity O(1)         
# # best case O(n), average case O(n^2)






####################################    merge sort ####################################
# def merge_array(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])#extend can be used here result.extend(right[j:]),right[j:] will add all the elements from j to the end of right
#             j += 1
#     if i< len(left):
#         while i< len(left):
#             result.append(left[i])
#             i += 1
#     if j < len(right):
#         while j < len(right):
#             result.append(right[j])
#             j += 1  

#     return result

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])
#     return merge_array(left_half, right_half)


# print(merge_sort([38, 27, 43, 3, 9, 82, 10]))  # Output: [3, 9, 10, 27, 38, 43, 82]
# time complexity #     
# #  worst case O(n log n), space complexity O(n)
# # best case O(n log n), average case O(n log n)   
# # Merge sort is a stable sort, meaning it maintains the relative order of equal elements.
# # It is also a divide-and-conquer algorithm, which splits the array into halves, sorts each half, and then merges them back together.     









####################################    quick sort ####################################
#using 2 list 
#def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + arr[len(arr)//2] + quick_sort(right)          

# complexity # time complexity #
# #  worst case O(n^2), space complexity O(n)     
# 
# 
#   

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array
        pi = partition(arr, low, high)

        # Recursively sort the two halves
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Pivot element
    i = low - 1        # Index of smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    # Place pivot at the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)






def quick_sort(arr, low, high):
    if low < high:
        # Partition using first element as pivot
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[low]  # Use first element as pivot
    i = low + 1

    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Place pivot in correct position
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

# Example usage
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)





def quick_sort(arr, low, high):
    if low < high:
        pi = hoare_partition(arr, low, high)
        quick_sort(arr, low, pi)
        quick_sort(arr, pi + 1, high)

def hoare_partition(arr, low, high):
    pivot = arr[low]
    print(f"\nHoare partition with pivot {pivot} at index {low}")
    i = low - 1
    j = high + 1

    while True:
        # Move i to the right
        while True:
            i += 1
            if arr[i] >= pivot:
                break

        # Move j to the left
        while True:
            j -= 1
            if arr[j] <= pivot:
                break

        if i >= j:
            print(f"Partition point at index {j}: {arr}")
            return j

        arr[i], arr[j] = arr[j], arr[i]
        print(f"Swapped {arr[i]} and {arr[j]}: {arr}")

# Example
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("\nSorted array:", arr)




