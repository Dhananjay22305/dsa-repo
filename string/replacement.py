def character_Replacement(s: str, k: int) -> int:
    count = {}  # Hash map to store frequency of characters in current window
    res = 0     # Result: max length found
    l = 0       # Left pointer
    maxf = 0    # The count of the most frequent character in the CURRENT window

    # Iterate with Right pointer (r) over the string
    for r in range(len(s)):
        # 1. Add current character to count map
        count[s[r]] = 1 + count.get(s[r], 0)
        
        # 2. Update the max frequency found so far in this window
        maxf = max(maxf, count[s[r]])

        # 3. Check if window is valid
        # Window Length = (r - l + 1)
        # If (Window Length - Max Frequency) > k, we need too many replacements.
        if (r - l + 1) - maxf > k:
            # Shrink the window from the left
            count[s[l]] -= 1
            l += 1
            # Note: We don't need to update maxf here strictly because
            # we are only interested in finding a BIGGER window than we have seen.
        
        # 4. Update the result with the current window size
        res = max(res, r - l + 1)

    print(res) 

# Example usage:
character_Replacement("AABBABA", 2)
    
