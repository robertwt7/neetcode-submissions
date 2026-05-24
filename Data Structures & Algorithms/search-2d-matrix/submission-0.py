import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        combined_list = []

        for m in matrix:
            combined_list.extend(m)

        index = bisect.bisect_left(combined_list, target)

        # out of range
        if index >= len(combined_list):
            return False

        return combined_list[index] == target 