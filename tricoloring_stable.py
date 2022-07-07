"""
https://stackoverflow.com/questions/44390698/tricoloring-an-array-of-integers

A zero-indexed array A consisting of N integers is given. A tricoloring of this array is a string consisting of N characters such that 
each character is either 'R' (meaning red), 'G' (green) or 'B' (blue). 
The Kth character of the string (where 0 ≤ K < N) denotes the color of Kth element of the array.

A tricoloring is stable if the sum of red elements is equal to the sum of green elements and to the sum of blue elements. 
A tricoloring does not necessarily use all three colors. The sum of elements of a color that is not used is assumed to be 0.

For example, consider array A such that
A[0] = 3    A[1] = 7    A[2] = 2    A[3] = 5    A[4] = 4
The string "RRGGB" is an example tricoloring of this array. It is not stable, because A[0] + A[1] = 10, A[2] + A[3] = 7, A[4] = 4 and 10 ≠ 7 ≠ 4. 

On the other hand, the tricoloring "RGBBR" is stable, because A[0] + A[4] = 7; A[1] = 7 and A[2] + A[3] = 7.
------------------------------------------------------------------------------------------------------------------------------------------
Write a function

function solution($A);
that, given a zero-indexed array A consisting of N integers, returns any stable tricoloring of this array. The function should return the string "impossible" if no stable tricoloring exists.

Assume that:

N is an integer within the range [0..18];
Each element of array A is an integer within the range [−100,000,000 .. 100,000,000].
For example, given array A such that

A[0] = 3    A[1] = 7    A[2] = 2    A[3] = 5    A[4] = 4
the function may return "RGBBR", as explained above. Given array A such that

A[0] = 3    A[1] = 6    A[2] = 9
the function should return "impossible".
"""

A = [
    # 3,
    # 7,
    # 5,
    # 4,
    # 2
    17,
    16,
    15,
    14,
    13,
    12,
    11,
    10,
    9,
    8,
    7,
    6,
    5,
    4,
    3,
    2,
    1,
    0,
    17,
    16,
    15,
    14,
    13,
    12,
    11,
    10,
    9,
    8,
    7,
    6,
    5,
    4,
    3,
    2,
    1,
    0,
    17,
    16,
    15,
    14,
    13,
    12,
    11,
    10,
    9,
    8,
    7,
    6,
    5,
    4,
    3,
    2,
    1,
    0,
]
cache = {}


def recurse(sumR: int, sumG: int, sumB: int, curAns: str, restArr: list) -> str:
    key = (sumR, sumG, sumB, "".join(str(i) for i in restArr))
    if key in cache:
        # print(key, cache[key])
        return cache[key]
    if len(restArr) == 0 and sumR == sumG == sumB:
        cache[key] = curAns
        return curAns
    elif len(restArr) == 0:
        cache[key] = None
        return None
    nextNum = restArr.pop()
    R = recurse(sumR + nextNum, sumG, sumB, curAns + "R", restArr[:])
    if R is not None and len(R) > 0:
        cache[key] = R
        return R
    G = recurse(sumR, sumG + nextNum, sumB, curAns + "G", restArr[:])
    if G is not None and len(G) > 0:
        cache[key] = G
        return G
    B = recurse(sumR, sumG, sumB + nextNum, curAns + "B", restArr[:])
    if B is not None and len(B) > 0:
        cache[key] = B
        return B
    cache[key] = None
    return None


def tricoloring(arr: list) -> str:
    total = sum(arr)
    if total % 3 != 0:
        return "impossible"
    arr.reverse()
    result = recurse(0, 0, 0, "", arr)
    if result is None:
        return "impossible"
    return result


print(tricoloring(A))
