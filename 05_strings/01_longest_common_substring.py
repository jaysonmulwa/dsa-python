"""
Longest Common Substring
========================
The longest common substring problem is a classic problem in computer science where the goal is to find the longest substring that appears in two or more strings.
A substring is a contiguous sequence of characters within a string.

The problem can be solved using dynamic programming, which involves building a table to store the lengths of common substrings between the two strings. 
The solution has a time complexity of O(m * n), where m and n are the lengths of the two strings.

1. Initialize a 2D array to store lengths of common substrings.
2. Iterate through each character of both strings.
3. If characters match, update the length in the table.
4. Keep track of the maximum length and the ending index of the longest common substring.
5. Extract the longest common substring using the maximum length and ending index.
"""

#// complexity: O(m*n)
#// space: O(m*n)
def longest_common_substring(s1, s2):
    m, n = len(s1), len(s2) # 7, 8

    # Create a 2D array to store lengths of common substrings
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    print(dp)  # Debugging: Print the initial DP table

    max_length = 0
    end_index = 0

    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0

    # Extract the longest common substring
    return s1[end_index - max_length:end_index]

# Example usage
s1 = "abcdefg"
s2 = "xyzabcde"
result = longest_common_substring(s1, s2) # Output: "abcde"
print("Longest Common Substring:", result)


"""
With recursion, the problem can be solved with a time complexity of O(2^(m+n)), which is inefficient for larger strings.
Using dynamic programming, the time complexity is reduced to O(m * n), where m and n are the lengths of the two strings.
The space complexity is also O(m * n) due to the 2D array used for storing the lengths of common substrings.
The dynamic programming approach builds a table where each cell dp[i][j] represents the length of the longest common substring ending at the i-th character of s1 and the j-th character of s2.
The final result is found by extracting the substring from s1 using the maximum length and the ending index.
"""

def longest_common_substring_recursive(s1, s2, m, n, count=0):
    """
    Recursive function to find the length of the longest common substring between two strings.
    """
    if m == 0 or n == 0:
        return count
    if s1[m - 1] == s2[n - 1]:
        count = longest_common_substring_recursive(s1, s2, m - 1, n - 1, count + 1)
    else:
        count = max(count, longest_common_substring_recursive(s1, s2, m - 1, n, 0),
                     longest_common_substring_recursive(s1, s2, m, n - 1, 0))
    return count

# Example usage of recursive approach
s1 = "abcdefg"
s2 = "xyzabcde"
m, n = len(s1), len(s2)
result_recursive = longest_common_substring_recursive(s1, s2, m, n)  # Output: 5 ("abcde")
print("Length of Longest Common Substring (Recursive):", result_recursive)