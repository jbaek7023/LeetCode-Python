import unittest
class Solution(object):
    # Run time error
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pointer = 0
        output = []

        # This takes O(n^2)
        while(len(s) >= pointer+len(p)):
            compare_s = s[pointer:pointer+len(p)]
            # Sorted Takes Too Long time
            hash = {}
            for letter in compare_s:
                if letter in hash:
                    hash[letter] += 1
                else:
                    hash[letter] = 1

            for letter in p:
                if letter in hash:
                    hash[letter] -= 1
                else:
                    hash[letter] = 1

            isAnagram = True
            for key in hash:
                if hash[key] != 0:
                    isAnagram = False
                    break;
            if isAnagram:
                output.append(pointer)
            pointer += 1

        return output

# To Run the Code -> Ctrl + Shift + B
class SolutionUnitTest(unittest.TestCase):
    def testArray(self):
        s = Solution()

        input = "cbaebabacd"
        input2 = "abc"
        output = [0, 6]
        self.assertEqual(s.findAnagrams(input, input2), output)

if __name__ == '__main__':
    unittest.main()

# Note
# xrange and range are the exact same in terms of functionality
# only difference is that xrange returns List
# range returns object
