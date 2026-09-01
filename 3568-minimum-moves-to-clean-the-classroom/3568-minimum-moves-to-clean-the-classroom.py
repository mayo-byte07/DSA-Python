from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])
        litter_map = {}
        start = None
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_map[(r, c)] = len(litter_map)
                    
        num_litters = len(litter_map)
        if num_litters == 0:
            return 0
            
        target_mask = (1 << num_litters) - 1
        
        # best_energy[r][c][mask] stores the maximum remaining energy seen for that state
        best_energy = [[[-1] * (1 << num_litters) for _ in range(n)] for _ in range(m)]
        
        sr, sc = start
        queue = deque([(sr, sc, 0, energy, 0)]) # (r, c, mask, current_energy, moves)
        best_energy[sr][sc][0] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, curr_e, moves = queue.popleft()
            
            if curr_e < best_energy[r][c][mask]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_e = curr_e - 1
                    cell_type = classroom[nr][nc]
                    
                    if cell_type == 'R':
                        next_e = energy
                        
                    next_mask = mask
                    if cell_type == 'L' and (nr, nc) in litter_map:
                        next_mask |= (1 << litter_map[(nr, nc)])
                        
                    if next_mask == target_mask:
                        return moves + 1
                        
                    # Can only continue moving if remaining energy > 0 or cell is 'R'
                    if next_e > 0 and next_e > best_energy[nr][nc][next_mask]:
                        best_energy[nr][nc][next_mask] = next_e
                        queue.append((nr, nc, next_mask, next_e, moves + 1))
                        
        return -1