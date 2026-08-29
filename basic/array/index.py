from typing import List

# Not solved: 1, 7, 22, 23, 28
# Not efficient: 8, 19, 24

# 1929. Concatenation of Array
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

# 1480. Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(ans[i-1] + nums[i])
        return ans

# 1672. Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        for account in accounts:
            wealth.append(sum(account))
        return max(wealth)


# 1470. Shuffle the Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        ans = []
        for i in range(len(x)):
            ans.append(x[i])
            ans.append(y[i])
        return ans

# 1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        greatest = max(candies)
        for candie in candies:
            if candie + extraCandies >= greatest:
                ans.append(True)
            else:
                ans.append(False)
        return ans

# 1365. How Many Numbers Are Smaller Than the Current Number
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        counter = 0
        for num in nums:
            for i in range(len(nums)):
                if num > nums[i]:
                    counter += 1
            ans.append(counter)
            counter = 0
        return ans

# 1389. Create Target Array in the Given Order
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target

# 1832. Check if the Sentence Is Pangram
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for i in range(26):
            current_char = chr(ord("a") + i)
        
            if sentence.find(current_char) == -1:
                return False 
        return True

# 1773. Count Items Matching a Rule
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        type = {
            "type": 0,
            "color": 1,
            "name": 2
        }

        for item in items:
            if item[type[ruleKey]] == ruleValue:
                ans += 1
        return ans

# 1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]
        
        for i in range(len(gain)):
            altitude.append(altitude[i] + gain[i])
        return max(altitude)

# 867. Transpose Matrix
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        rows = len(matrix)
        cols = len(matrix[0])

        result = [[0 for _ in range(rows)] for _ in range(cols)]

        for row in range(rows):
            for col in range(cols):
                result[col][row] = matrix[row][col]

        return result

# 989. Add to Array-Form of Integer 
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        str_num = ""
        for digit in num:
            str_num = str_num + str(digit)
        total = str(int(str_num) + k)
        ans = []
        for num in total:
            ans.append(int(num))
        return ans

# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Make empty hashmap
        map = {}
        # iterate nums
        for i in range(len(nums)):
            # DIFF = target - num
            diff = target - nums[i]
            # IF there is DIFF in hashmap
            if diff in map:
                # RETURN [index, HASHMAP[DIFF]]
                return [i, map[diff]]
            map[nums[i]] = i

# 566. Reshape the Matrix
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # Define the length of matrix row and column
        mat_row_length = len(mat)
        mat_column_length = len(mat[0])
        # if mat_row * mat_column != r * c, return mat itself
        if mat_row_length * mat_column_length != r * c:
            return mat
        # make the list for answer
        output = [[0 for _ in range(c)] for _ in range(r)]
        
        # iterate until index < r * c
        index = 0
        while index < r * c:
            print(f"row: {index // c} col:{index % c}")
            output[index // c][index % c] = mat[index // mat_column_length][index % mat_column_length]
            index += 1
        return output

# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        target_index = 1
        for i in range(1, n): # [0,0,1,1,1,2,2,3,3,4]
            if nums[i-1] != nums[i]:
                nums[target_index] = nums[i]
                target_index += 1
        return target_index

# 1854. Maximum Population Year (ref: https://leetcode.com/problems/rotate-image/)
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        population = {}

        for birth, death in logs:
            for year in range(birth, death):
                population[year] = population.get(year, 0) + 1

        maximum = 0
        ans = float("inf")

        for year in population:
            if population[year] > maximum:
                maximum = population[year]
                ans = year
            elif population[year] == maximum:
                ans = min(ans, year)

        return ans

# 1886. Determine Whether Matrix Can Be Obtained By Rotation
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        rows = len(mat)
        # Rotate the matrix at most 4 times. (0°, 90°, 180°, and 270°)
        for _ in range(4):
            # Only need to process the top half of the matrix.
            for i in range(rows // 2):
                # (rows + 1) // 2 handles both even and odd-sized matrices.
                for j in range((rows + 1) // 2):
                    # (i, j)                     -> top-left
                    # (rows-1-j, i)              -> bottom-left
                    # (rows-1-i, rows-1-j)       -> bottom-right
                    # (j, rows-1-i)              -> top-right
                    (
                        mat[i][j],
                        mat[rows-1-j][i],
                        mat[rows-1-i][rows-1-j],
                        mat[j][rows-1-i]
                    ) = (
                        mat[rows-1-j][i],
                        mat[rows-1-i][rows-1-j],
                        mat[j][rows-1-i],
                        mat[i][j]
                    )

            if mat == target:
                return True
        return False

# 53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = float("-inf")
        for i in range(len(nums)):
            current = 0
            for j in range(i, len(nums)):
                current += nums[j]
                max_subarray = max(max_subarray, current)
        return max_subarray

# 1217. Minimum Cost to Move Chips to The Same Position
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_nums = 0
        odd_nums = 0

        for num in position:
            if num % 2 == 0:
                even_nums += 1
            else:
                odd_nums += 1
        return min(even_nums, odd_nums)