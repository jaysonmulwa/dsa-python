def longest_palindromic_subsequence(s):
    """
    Function to find the length of the longest palindromic subsequence in a string.
    Uses dynamic programming to build a 2D table to store lengths of palindromic subsequences.
    """
    n = len(s)
    
    # Create a 2D array to store lengths of longest palindromic subsequence
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Build the dp array
    for length in range(2, n + 1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n - 1]

# Example usage
s = "BBABCBCAB"
result = longest_palindromic_subsequence(s)  # Output: 7 ("BABCBAB" or "BCBCB")
print("Length of Longest Palindromic Subsequence:", result)


"""
LPS - expand around center
With recursion, the problem can be solved with a time complexity of O(2^n),
which is inefficient for larger strings.
Using dynamic programming, the time complexity is reduced to O(n^2), where n is the length of the string.
The space complexity is also O(n^2) due to the 2D array used for storing the lengths of palindromic subsequences.
The dynamic programming approach builds a table where each cell dp[i][j] represents the length of the longest palindromic subsequence in the substring s[i:j+1].
The final result is found in dp[0][n-1], which gives the length of the longest palindromic subsequence in the entire string.
"""

def longest_palindromic_subsequence_recursive(s, i, j):
    """
    Recursive function to find the length of the longest palindromic subsequence in a string.
    """
    if i > j:
        return 0
    if i == j:
        return 1
    if s[i] == s[j]:
        return 2 + longest_palindromic_subsequence_recursive(s, i + 1, j - 1)
    else:
        return max(longest_palindromic_subsequence_recursive(s, i + 1, j), 
                   longest_palindromic_subsequence_recursive(s, i, j - 1))