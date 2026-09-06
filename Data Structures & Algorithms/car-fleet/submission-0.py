from collections import Counter

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrivalTime = []
        cars = []
        for i in range(len(position)):
            cars.append((position[i],speed[i]))

        cars.sort() #will sort the function based on the first tuple. 
        arrivalTime.append((target - cars[-1][0]) / cars[-1][1] )
        for i in range(len(cars)-2, -1, -1):    #the second argument is end before -1 and the mlast argument is by step of -1
            time = (target - cars[i][0]) / cars[i][1]
            if arrivalTime and time <= arrivalTime[-1]:
                continue
            else:
                arrivalTime.append(time)

        return len(arrivalTime)

