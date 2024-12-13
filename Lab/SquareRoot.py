"""
Algorithm: Square Root Calculation 
Input: N -> real number 
Output: r -> number such that r * r ~= N

1. Choose an arbitrary number r between 1 and N
2. If N - e <= r*r <= N + e, with e being very small (e.g., 0.000000001), then the result is r.
3. Otherwise, set r = (r + N/r)/2
4. Go back to step 2
"""

from random import uniform

E = 0.00000001


def sqrt_(N):
    assert N >= 0
    r = uniform(0, N)
    while True:
        if abs(N - r * r) < E:
            return r
        r = (r + N / r) / 2


def main():
    print("Enter CTRL+C/D or a negative number to exit")
    while True:
        num = float(input("sqrt> "))
        if num < 0:
            break
        print(sqrt_(num))


if __name__ == "__main__":
    main()
