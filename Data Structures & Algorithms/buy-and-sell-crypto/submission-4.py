class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                # print(f"prices at L: {prices[l]}", f"prices at R: {prices[r]}")
                l = r
            else:
                profit = prices[r] - prices[l]
                # print(f"prices at L: {prices[l]}", f"prices at R: {prices[r]}", f"profit: {profit}")
                res = max(res, profit)

        return res