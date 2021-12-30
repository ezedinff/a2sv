import unittest
from typing import List

"""
https://leetcode.com/problems/car-fleet/
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith 
car and speed[i] is the speed of the ith car (in miles per hour). 

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. 
The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., 
they are assumed to have the same position). 

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also 
a car fleet. 

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

 
Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3 Explanation: The cars starting at 10 and 8 
become a fleet, meeting each other at 12. The car starting at 0 doesn't catch up to any other car, so it is a fleet 
by itself. The cars starting at 5 (speed 3) and 3 (speed 1) become a fleet, meeting each other at 6. The fleet moves 
at speed 1 until it reaches target. Note that no other cars meet these fleets before the destination, so the answer 
is 3. """


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    carFleets, cars = [], sorted([(x, y) for x, y in zip(position, speed)], reverse=True)
    for pos, spd in cars:
        arrival = (target - pos) / spd
        if not (carFleets and arrival <= carFleets[-1]):
            carFleets.append(arrival)
    return len(carFleets)


class TestSolutions(unittest.TestCase):
    def test_one(self):
        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]
        expected = 3
        actual = carFleet(target, position, speed)
        self.assertEqual(expected, actual)
