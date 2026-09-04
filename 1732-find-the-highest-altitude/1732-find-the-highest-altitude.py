class Solution(object):
    def largestAltitude(self, gain):
        current_altitude = 0
        max_altitude = 0
        
        for g in gain:
            current_altitude += g
            if current_altitude > max_altitude:
                max_altitude = current_altitude
                
        return max_altitude