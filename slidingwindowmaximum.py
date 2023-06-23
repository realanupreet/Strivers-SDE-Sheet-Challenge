import collections

def maxSlidingWindow(arr, n, k):
  """
  Finds the maximum element in each sliding window of size k.

  Args:
    arr: The array of elements.
    n: The number of elements in the array.
    k: The size of the sliding window.

  Returns:
    A list of the maximum elements in each sliding window.
  """

  ans = []
  dq = collections.deque()
  for i in range(0, k):
    while dq and arr[dq[-1]] <= arr[i]:
      dq.pop()
    dq.append(i)
  ans.append(arr[dq[0]])
  for i in range(k, n):
    while dq and arr[dq[-1]] <= arr[i]:
      dq.pop()
    while dq and dq[0] <= i - k:
      dq.popleft()
    dq.append(i)
    ans.append(arr[dq[0]])
  return ans
