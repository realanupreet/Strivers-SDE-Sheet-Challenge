def search(arr, target) :
    left,right=0, len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[left]<=arr[mid]:
            if target>arr[mid] or target<arr[left]:
                left=mid+1
            else:
                right=mid-1
        else:
            if target<arr[mid] or target>arr[right]:
                right=mid-1
            else:
                left=mid+1
    return -1