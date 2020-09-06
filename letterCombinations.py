# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

# Note:

# Although the above answer is in lexicographical order, your answer could be in any order you want.

def letterCombinations(self, digits: str) -> List[str]:
    letters = [[],[],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"], ["p","q","r","s"], ["t","u","v"], ["w","x","y","z"]]
    if(len(digits) == 0):
        return ""
    combinations = letters[int(digits[0])]
    if(len(combinations) == 1):
        return combinations 
    i = 1
    combinations = letters[int(digits[0])]
    while(i <= len(digits) - 1):
        b = letters[int(digits[i])]
        lengthC = len(combinations)
        for j in range(lengthC):
            for k in range(len(b)):
                combinations.append(combinations[j]+letters[int(digits[i])][k])
        i= i + 1
        combinations = combinations[lengthC:]
    combinations = [i for i in combinations if len(i) == len(digits)]
    return combinations