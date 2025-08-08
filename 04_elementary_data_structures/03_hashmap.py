"""
Hashmap Implementation in Python
This code implements a simple hashmap (also known as a hash table) in Python.
A hashmap is a data structure that stores key-value pairs and allows for efficient retrieval of values based on their keys.
It uses a list to store the data and a hash function to compute the index for each key
in the list.
The hashmap supports basic operations such as insertion, deletion, and retrieval of values.


 * Hashing uses a data structure called a hash table.
 * - hash tables provide fast insertion, deletion, and retrieval,
 * - hash tables perform poorly for operations that involve searching, (like finding max and min value ina a data set)
 * - For these operations, other data structures such as the binary search tree are more appropriate
 * 
 * A better hashing algorithm (more superior for strings ad integers) involves:
 * - - properly sizing array - use a size that is a prime number
 * - - a better hashing algorithm e.g Horners algorithm (it adds a step by multiplying the resulting total by a prime constant e.g 31, 37) 
 * 
 * Hash Functions
 * 1. Universal hashing
 * Maximizes best average case performance by randomizing the set of hash functions chosen.
 * We begin by choosing a prime number p large enough so that every possible key k is in the range 0 to p - 1, inclusive
 *
 *
 * 2. Perfect hashing
 * - Hashing is often a good choice for its excellent average-case performance, hashing can also provide excellent worst-case performance when the set of keys is static
 * - We call a hashing technique perfect hashing if O.1/ memory accesses are required to perform a search in the worst case
 * - To create a perfect hashing scheme, we use two levels of hashing, with universal hashing at each level.
 * - - The first level is essentially the same as for hashing with chaining. universal hash functions.
 * - - Instead of making a linked list of the keys hashing to slot j , however, we use a small secondary hash table Sj with an associated hash function hj
 *
 * 3. Other (Multiplication and division hashing)
 * - Division
 * -- h(k) = k mod m : where m is the size of array
 * - Multiplication we first multiply key k by some integer value A. 
 * -- h(k) = m(kA mod 1)
 *
 * Handling collisions:
 * 1. Chaining
 * a. Separate chaining
 * -- - a hash table that uses a linked list or array to handle collisionss (each array element of the hash table holds another array).
 * -- - this is a good data structure for small data sets
 * -- - after we create the array to store the hashed keys, we call a function that assigns an empty array to each array element of the hash table
 *
 * 2.Open addressing
 * - All elements occupy the hashtable itself. (no chaining)
 * a. Linear probing
 * -- - is an example of a more general hashing technique called open-addressing hashing.
 * -- - should be chosen over separate chaining when your array for storing data can be fairly large.
 * -- - when there is a collision, the program simply looks to see if the next element of the hash table is empty. 
 * -- - - If so, the key is placed in that element. If the element is not empty, the program continues to search for an empty hash-table element until one is found.
 * -- - This technique makes use of the fact that any hash table is going to have many empty elements and it makes sense to use the space to store keys.
 *
 * b. Quadratic probing
 * - This method works much better than linear probing, but to make full use of the hash table, the values of c1, c2, and m are constrained
 * - If two keys have the same initial probe position, then their probe sequences are the same. This property leads to a milder form of clustering, called secondary clustering
 *
 * c. Double hashing
 * - offers one of the best methods available for open addressing because the permutations produced have many of the characteristics of randomly chosen permutations
 * - The initial probe goes to position T[h1(k)]
 * - successive probe positions are offset from previous positions by the amount h2(k) . modulo m
 */

"""

class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.map = [[] for _ in range(size)]  # Create a list of empty lists

    def _hash(self, key):
        return hash(key) % self.size  # Compute the hash index

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:  # Update existing key
                self.map[index][i] = (key, value)
                return
        self.map[index].append((key, value))  # Insert new key-value pair

    def get(self, key):
        index = self._hash(key)
        for k, v in self.map[index]:
            if k == key:
                return v  # Return the value if key is found
        return None  # Return None if key is not found

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                del self.map[index][i]  # Delete the key-value pair
                return True
        return False  # Return False if key was not found
    def contains(self, key):
        index = self._hash(key)
        for k, v in self.map[index]:
            if k == key:
                return True
        return False
    def __str__(self):
        return str({k: v for sublist in self.map for k, v in sublist})
# Example usage
if __name__ == "__main__":
    hashmap = HashMap()
    hashmap.insert("name", "Alice")
    hashmap.insert("age", 30)
    hashmap.insert("city", "New York")

    print("HashMap:", hashmap)

    print("Get 'name':", hashmap.get("name"))
    print("Get 'age':", hashmap.get("age"))
    print("Get 'country':", hashmap.get("country"))  # Should return None

    hashmap.delete("age")
    print("After deleting 'age':", hashmap)

    print("Contains 'city':", hashmap.contains("city"))
    print("Contains 'age':", hashmap.contains("age"))  # Should return False