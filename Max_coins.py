class Solution:
    def maxCoins(self, piles: List[int]) -> int:
    # def max_coin(arr):
        piles.sort()
        pile_len = len(piles)
        m = pile_len // 3
        sum = 0
        for i in range(m,pile_len,2):
            sum += piles[i]

        return sum
