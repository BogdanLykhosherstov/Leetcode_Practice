def lengthOfLongestSubstring(s: str) -> int:
    #   hint: sliding window with lagging start
    start = 0
    visitedChars = {}

    # Alg: For each char,
    # IF unique : place {number:index} into visitedChars,
    # ELSE: visitedChars[number] = newIndex,

    return


if __name__ == "__main__":
    lengthOfLongestSubstring('abcabcbb')
