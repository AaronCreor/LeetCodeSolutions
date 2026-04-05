class Solution:
    def calPoints(self, operations: List[str]) -> int:
        retList = []
        operations.reverse()
        while len(operations) > 0:
            matchStatement = operations.pop()
            match matchStatement:
                case '+':
                    retList.append(retList[-1] + retList[-2])
                case 'D':
                    retList.append(retList[-1]*2)
                case 'C':
                    retList.pop()
                case _:
                    retList.append(int(matchStatement))
        return sum(retList)