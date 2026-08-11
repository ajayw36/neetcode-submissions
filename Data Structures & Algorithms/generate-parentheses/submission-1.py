class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        self.search(answer, '', 0, 0, n)
        return answer

    def search(self, answer, curString, leftCount, rightCount, n):
        if leftCount == rightCount == n:
            answer.append(curString)
        if rightCount > leftCount or leftCount > n:
            return

        curString += '('
        self.search(answer, curString, leftCount + 1, rightCount, n)
        curString = curString[:-1]

        curString += ')'
        self.search(answer, curString, leftCount, rightCount + 1, n)
        curString = curString[:-1]
        