# https://leetcode.com/problems/account-balance-after-rounded-purchase/description/

class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """        
        price = 100 - purchaseAmount

        remainder = price % 10
        
        if remainder == 0:
            return price
        elif remainder <= 5:
            return price - remainder
        else:
            return price + (10 - remainder)
