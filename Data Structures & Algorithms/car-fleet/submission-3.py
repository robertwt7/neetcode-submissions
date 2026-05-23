import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # if a car catch up to the previous car <= steps taken to destination then it is considered on the same fleet
        hm = {}
        for i in range(len(position)):
            hm[position[i]] = speed[i]

        sorted_pos = sorted(position)
        fleet = 0
        # max from the max target
        last_steps_to_target = 0
        while sorted_pos:
            last_pos = sorted_pos.pop()
            # distance need to be precise, only if the previous one can pass the next one then we make it 
            steps_to_target = (target - last_pos) / hm[last_pos]
            if steps_to_target > last_steps_to_target:
                fleet += 1
                # only update when this becomes the next fleet, otherwise keep it the original steps of the slowest one at the front
                last_steps_to_target = steps_to_target

        return fleet