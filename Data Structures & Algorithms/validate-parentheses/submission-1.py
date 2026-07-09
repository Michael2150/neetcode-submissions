class Solution:
    def isValid(self, s: str) -> bool:
        start_par = ["{", "[", "("]
        end_par = ["}", "]", ")"]
        parenths = [l for l in s if l in start_par or l in end_par]

        counts = {}

        for x in parenths:  # Check the string
            if x in start_par:  # Check if the char is a start_par
                if x in counts:
                    counts[x] += 1
                else:
                    counts[x] = 1

            else:  # the char is an end_par
                i = end_par.index(x)
                strt_eq = start_par[i]

                # See if we have an equivalent start_par available
                if not (strt_eq in counts):
                    return False

                counts[strt_eq] -= 1
                if counts[strt_eq] == 0:
                    counts.pop(strt_eq)

        print(counts)

        return len(counts) == 0
