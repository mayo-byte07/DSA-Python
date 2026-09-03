class Solution(object):
    def suggestedProducts(self, products, searchWord):
        products.sort()
        
        res = []
        left, right = 0, len(products) - 1
        
        for i, char in enumerate(searchWord):
            while left <= right and (len(products[left]) <= i or products[left][i] != char):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != char):
                right -= 1
            current_suggestions = []
            for j in range(min(3, right - left + 1)):
                current_suggestions.append(products[left + j])
            res.append(current_suggestions)
            
        return res