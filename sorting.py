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



