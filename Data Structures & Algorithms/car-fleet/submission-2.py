import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # if a car catch up to the previous car < steps taken to destination then it is considered on the same fleet
        hm = {}
        for i in range(len(position)):
            hm[position[i]] = speed[i]

        sorted_pos = sorted(position)
        fleet = 0
        # max from the max target
        last_steps_to_target = 0
        while sorted_pos:
            last_pos = sorted_pos.pop()
            # remaining distance divided by speed, because it needs to be caught before destination so this is fine to be rounded to floor
            steps_to_target = (target - last_pos) / hm[last_pos]
            if steps_to_target > last_steps_to_target:
                fleet += 1
                # only update when this becomes the next fleet, otherwise keep it the original fleet 
                last_steps_to_target = steps_to_target

        return fleet