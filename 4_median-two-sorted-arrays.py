def findMedianSortedArrays(nums1, nums2):

    # rather than .extend, could have just written nums1 + nums2
    nums1.extend(nums2)
    nums1.sort()

    list_length = len(nums1)

    # if the list is even in length, there is no middle number
    # therefore, there will require 2 indexes to average together
    if (list_length % 2) == 0:

        # get the two indexes to average
        index1, index2 = (list_length//2) - 1, (list_length//2)

        # find the two numbers
        first_num = nums1[index1]
        second_num = nums1[index2]

        # return the average of the two numbers
        return (first_num + second_num) / 2

    # If the list is odd, the index is the floor division of the list    
    else:
        return nums1[list_length//2]

    

print(findMedianSortedArrays([1,2,3,4], [6,3,7,8,1]))
