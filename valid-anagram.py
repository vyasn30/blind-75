class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            # print("False")
            return False

        s_count_dict = self.getCountDict(s)
        t_count_dict = self.getCountDict(t)

        # print(s_count_dict)
        # print(t_count_dict)
        return s_count_dict == t_count_dict

    def getCountDict(self, input_string):
        input_string = list(input_string)
        ret = dict()

        for val in input_string:
            if val not in ret:
                ret[val] = 1
            if val in ret:
                ret[val] += 1

        return ret

if __name__ == "__main__":
    a = "aacc"
    b = "ccac"
    print(Solution().isAnagram(a,b))