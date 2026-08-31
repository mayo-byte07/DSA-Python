class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        if not head or not head.next or not head.next.next:
            return [-1, -1]
            
        first_crit = -1
        last_crit = -1
        min_dist = float('inf')
        
        prev = head
        curr = head.next
        idx = 1
        
        while curr.next:
            # Check for local maxima or local minima
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                
                if first_crit == -1:
                    first_crit = idx
                else:
                    min_dist = min(min_dist, idx - last_crit)
                    
                last_crit = idx
                
            prev = curr
            curr = curr.next
            idx += 1
            
        # If there are fewer than two critical points
        if first_crit == -1 or first_crit == last_crit:
            return [-1, -1]
            
        return [min_dist, last_crit - first_crit]