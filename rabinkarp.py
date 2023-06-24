def bpow(a, b, p):
    """
    Calculates a^b mod p.

    Args:
      a: The base.
      b: The exponent.
      p: The modulus.

    Returns:
      a^b mod p.
    """

    ans = 1
    while b:
        if b & 1:
            ans = (ans * a) % p
        a = (a * a) % p
        b >>= 1
    return ans


def stringMatch(text, pattern):
    """
    Finds all occurrences of the pattern in the text.

    Args:
      text: The text string.
      pattern: The pattern string.

    Returns:
      A list of the indices of the occurrences of the pattern in the text.
    """

    ans = []
    p = 5381
    k = len(pattern)
    n = len(text)
    h = 0
    hw = 0
    for i in range(k):
        cvalue = ord(pattern[i]) - ord('a') + 1
        h = (h + (cvalue * bpow(26, k - i - 1, p)) % p) % p
        cvalue = ord(text[i]) - ord('a') + 1
        hw = (hw + (cvalue * bpow(26, k - i - 1, p)) % p) % p
    for i in range(k, n):
        if h == hw:
            flag = True
            for j in range(k):
                if pattern[j] != text[i - k + j]:
                    flag = False
                    break
            if flag:
                ans.append(i - k + 1)
        hw = (hw - (ord(text[i - k]) - ord('a') + 1)
              * bpow(26, k - 1, p) % p + 0 + p) % p
        hw = (hw * 26) % p
        cvalue = ord(text[i]) - ord('a') + 1
        hw = (hw + cvalue) % p
    return ans
