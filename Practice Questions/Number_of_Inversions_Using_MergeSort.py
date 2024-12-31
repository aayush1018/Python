# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:09:34 2024

@author: Aayush
"""

def merge_and_counter (arr, temp_arr, left, mid, right):
    #merge two subarrays and count inversions
    i = left # strating index for left subarray
    j = mid+1 # starting index for right subarray
    k = left # starting index to be sorted
    inv_count =0 # initialize inversion count
    
    #merge the two subarrays while counting inversions
    while i<= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            #There are mid - i inversions, because all remaining elements in left subarray
            # (arr[i], arr[i+1], ..., arr[mid]) are greater than arr[j]
            temp_arr[k] = arr[j]
            inv_count += (mid - i +1)
            j += 1
        k += 1
        # copy reamining elements of left subarray if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i+=1
        k+=1
    while j<= right:
        temp_arr[k] = arr[j]
        j+=1
        k+=1
    for i in range (left, right + 1):
        arr[i] = temp_arr[i]
    return inv_count

def merge_sort_and_count ( arr, temp_arr, left, right):
    "Sorting the array and counting inversing using merge sort"
    inv_count = 0
    if left < right:
        mid = (left+right) //2
        # count inversions on left half
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        #count inversions on right half
        inv_count += merge_sort_and_count(arr, temp_arr, mid+1, right)
        #  count inversiong during merging of the two halves
        inv_count += merge_and_counter(arr, temp_arr, left, mid, right)
        
    return inv_count

def main():
    
    n = int(input())
    user_input = input()
    array = list(map(int,user_input.split()))
    if len(array) !=n:
        print(len(array))
    temp_array = [0] *n
    inversion_count = merge_sort_and_count(array, temp_array, 0, n-1)
    print(inversion_count)
    
if __name__ == "__main__":
    main()
    