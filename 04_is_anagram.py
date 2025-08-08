"""
Is Anagram
========================
"""

def is_anagram(s1: str, s2: str) -> bool:
    """
    Function to check if two strings are anagrams of each other.
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
    """
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # Sort the characters and compare
    return sorted(s1) == sorted(s2)

# Example usage
s1 = "listen"
s2 = "silent"
result = is_anagram(s1, s2)  # Output: True