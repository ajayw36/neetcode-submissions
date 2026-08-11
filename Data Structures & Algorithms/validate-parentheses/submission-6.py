class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {'}': '{', ')': '(', ']': '[',}

        for ch in s:
            if ch in close_to_open:
                if not stack or stack.pop() != close_to_open[ch]:
                    return False      
            else:
                stack.append(ch)         
        
        return stack == []
