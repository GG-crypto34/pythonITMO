def binary_search(lst:list, target:int) -> tuple[int,int]:
    """
    Algorythm for binary search. Searching for target number in unsorted list
    of integers and returns tuple containing two integers: amount of comparison and target number.
    If list doesn't contain a target number, then it returns tuple containing two integers: -1 and target number.
    :param lst(list[int,int,int,...]): list of numbers
    :param target(int): target numeber for searching
    :return((int,int)): (amount of comparison/-1(when no target in list), target number)
    """

    lst = sorted(lst)
    lowi = 0
    midi = int((len(lst) / 2) + 1) - 1
    highti = len(lst) - 1
    cc = 0
    while lowi <= highti:
       cc += 1
       midi = (lowi + highti) // 2
       if lst[midi] == target:
          return (cc, target)
       elif lst[midi] < target:
          lowi = midi + 1
       elif lst[midi] > target:
          highti = midi - 1
    return (-1,target)

def seq_search(lst:list, target:int) -> tuple[int,int]:
    """
    Algorythm for sequence search. Searching for target number in unsorted list of integers. Returns tuple containing two integers:
    amount of comparison and target number. If there are no target nuber in list, then it returns
    tuple containing two integers: -1 and target number.
    :param lst(list[int,int,int,...]): list of numbers
    :param target(int): target numeber for searching
    :return((int,int)): (amount of comparison/-1(when no target in list), target number)
    """
    lst = sorted(lst)
    for i in range(len(lst)):
        if lst[i] == target: return (i+1,lst[i])
    return (-1,target)

def guess_number(target:int, ranges:tuple, mode:str) -> tuple[int, int]:
    """
    Function for guessing target number in two modes(Choose on use). Returns tuple containing two integers:
    amount of comparison and target number. If there are no target nuber in list, then it returns
    tuple containing two integers: -1 and target number.
    :param target(int): target numeber for searching
    :param ranges(tuple[int,int]): range of numbers to guess
    :param mode(str): mode of guessing("binary" or "seq")
    :return:
    """
    list1 = []
    if not isinstance(ranges, tuple) or not isinstance(ranges[0], int) or not isinstance(ranges[1], int) or not isinstance(target, int) or not isinstance(mode, str) or mode not in ("binary", "seq"):
        raise TypeError("invalid input")
    for x in range(ranges[0], ranges[1] + 1):
        list1.append(x)
    if mode == "binary":
        return binary_search(lst = list1, target=target)
    elif mode == "seq":
        return seq_search(lst = list1, target=target)

