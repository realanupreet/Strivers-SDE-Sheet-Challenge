def atoi(str):
  """
  Converts a string to an integer.

  Args:
    str: The string to be converted.

  Returns:
    The integer representation of the string.
  """

  if len(str) == 0:
    return 0

  def atoir(str, index):
    if index >= len(str):
      return 0

    cvalue = ord(str[index]) - ord('0')
    if cvalue >= 0 and cvalue <= 9:
      return cvalue
    return atoir(str, index + 1)

  res = atoir(str, 0)

  if str[0] == '-':
    res = -1 * res

  return res
