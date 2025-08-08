"""
    https://www.youtube.com/watch?v=sSno9rV8Rhg
"""



def longest_common_subsequence(s1, s2):
  
    """
    Function to find the length of the longest common subsequence (LCS) between two strings.
    Uses dynamic programming to build a 2D table to store lengths of LCS for substrings.
    """
    m, n = len(s1), len(s2)
    
    # Create a 2D array to store lengths of longest common subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

# Example usage
s1 = "AGGTAB"
s2 = "GXTXAYB"
result = longest_common_subsequence(s1, s2)  # Output: 4 ("GTAB")
print("Length of Longest Common Subsequence:", result)


"""
With recursion, the problem can be solved with a time complexity of O(2^(m+n)), which is inefficient for larger strings.
Using dynamic programming, the time complexity is reduced to O(m * n), where m and n are the lengths of the two strings.
The space complexity is also O(m * n) due to the 2D array used for storing the lengths of LCS.
The dynamic programming approach builds a table where each cell dp[i][j] represents the length of the longest common subsequence of the first i characters of s1 and the first j characters of s2.
The final result is found in dp[m][n], which gives the length of the longest common subsequence between the two strings.
"""

def longest_common_subsequence_recursive(s1, s2, m, n):
    """
    Recursive function to find the length of the longest common subsequence (LCS) between two strings.
    """
    if m == 0 or n == 0:
        return 0
    if s1[m - 1] == s2[n - 1]:
        return 1 + longest_common_subsequence_recursive(s1, s2, m - 1, n - 1)
    else:
        return max(longest_common_subsequence_recursive(s1, s2, m - 1, n), 
                   longest_common_subsequence_recursive(s1, s2, m, n - 1))
    
# Example usage of recursive approach
s1 = "AGGTAB"
s2 = "GXTXAYB"
m, n = len(s1), len(s2)
result_recursive = longest_common_subsequence_recursive(s1, s2, m, n)  # Output: 4 ("GTAB")
print("Length of Longest Common Subsequence (Recursive):", result_recursive)