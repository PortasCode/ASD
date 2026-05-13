class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        suma = sum(nums)
        if suma % 2 == 1:
            return False
        szukana = suma // 2
        T = [[0 for _ in range(szukana + 1)]]

        return True
