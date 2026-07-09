class Solution:
    def isValid(self, s: str) -> bool:
        start_par = ["{", "[", "("]
        end_par = ["}", "]", ")"]
        parenths = [l for l in s if l in start_par or l in end_par]

        for i in range(len(start_par)):
            sp = start_par[i]
            ep = end_par[i]

            if parenths.count(sp) != parenths.count(ep):
                return False

        return True