from typing import List


def findStockSpans(prices: List[int]) -> List[int]:
    n = len(prices)
    ans = [1] * n
    st = [0]
    for i in range(1, n):
        while st and prices[st[-1]] < prices[i]:
            st.pop()
        if st:
            ans[i] += i - st[-1] - 1
        else:
            ans[i] += i
        st.append(i)
    return ans
