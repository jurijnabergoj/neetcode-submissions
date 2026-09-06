class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st = sorted(stones, reverse=True)

        while len(st) > 1:
            stone1 = st[0]
            stone2 = st[1]

            if stone1 == stone2:
                st = st[2:]
            elif stone1 > stone2:
                st.pop(1)
                st[0] = stone1 - stone2
                st = sorted(st, reverse=True)
            else:
                st.pop(0)
                st[0] = stone2 - stone1
                st = sorted(st, reverse=True)
        return st[0] if st else 0