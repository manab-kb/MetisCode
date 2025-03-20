# https://leetcode.com/problems/smallest-number-in-infinite-set/description/?envType=study-plan-v2&envId=leetcode-75

"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
"""


class SmallestInfiniteSet:
    def __init__(self):
        self.intSet = set(range(1, 1001))

    def popSmallest(self) -> int:
        smallestInt = min(self.intSet)
        self.intSet.remove(smallestInt)
        return smallestInt

    def addBack(self, num: int) -> None:
        self.intSet.add(num)
