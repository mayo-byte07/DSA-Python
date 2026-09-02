class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []
        cur_line = []
        num_of_letters = 0
        
        for word in words:
            # Check if the word fits on the current line with at least 1 space between words
            if num_of_letters + len(word) + len(cur_line) > maxWidth:
                # Distribute extra spaces round-robin to all words except the last one
                for i in range(maxWidth - num_of_letters):
                    cur_line[i % (len(cur_line) - 1 or 1)] += ' '
                    
                res.append(''.join(cur_line))
                cur_line = []
                num_of_letters = 0
                
            cur_line.append(word)
            num_of_letters += len(word)
            
        # The last line must be left-justified
        res.append(' '.join(cur_line).ljust(maxWidth))
        
        return res