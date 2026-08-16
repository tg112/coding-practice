class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hash_map = {}
        ans = []

        cols = len(mat)
        rows = len(mat[0])
        
        low = 0
        high = cols * rows - 1

        for col in range(cols):
            counter = 0
            for row in range(rows):
                if mat[col][row] == 0:
                    continue
                counter += 1
            hash_map[col] = counter
        # hash_map.items()でtupleを作る
        # key= は「この値を基準に並べ替えてください」という意味で、xはtupleの値でx[1]がソートキーになる
        # sort順に並べたtupleをforに渡して一つずつiterationする
        for key, _ in sorted(hash_map.items(), key=lambda x: x[1]):
            ans.append(key)
        return ans[:k]
