

from collections import defaultdict, deque
from typing import List

def alien_order(words: List[str]) -> str:
    """
    Determines the character order in an alien language using topological sort.

    Parameters:
        words (List[str]): Sorted list of words in alien language.

    Returns:
        str: A valid character order string or an empty string if invalid.
    """
    # Step 1: Initialize graph and in-degree dictionary
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}

    # Step 2: Build graph by comparing adjacent words
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        
        # Invalid if first word is longer and is a prefix of the second
        if len(w1) > len(w2) and w1.startswith(w2):
            return ""

        # Find first differing character
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    in_degree[c2] += 1
                break

    # Step 3: Topological sort using Kahn's Algorithm
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check for cycle
    if len(result) != len(in_degree):
        return ""

    return ''.join(result)


def run_tests():
    """Runs predefined test cases with expected outputs."""
    print("=== TEST CASES ===")

    # Test 1: Normal input
    words1 = ["wrt", "wrf", "er", "ett", "rftt"]
    print("Test 1:")
    print("Input:", words1)
    print("Expected Output: wertf")
    print("Actual Output  :", alien_order(words1))
    print()

    # Test 2: Cycle in graph
    words2 = ["z", "x", "z"]
    print("Test 2:")
    print("Input:", words2)
    print("Expected Output: (empty string)")
    print("Actual Output  :", alien_order(words2))
    print()

    # Test 3: Single word input
    words3 = ["abc"]
    print("Test 3:")
    print("Input:", words3)
    print("Expected Output: abc")
    print("Actual Output  :", alien_order(words3))
    print()

    # Test 4: Invalid prefix case
    words4 = ["abc", "ab"]
    print("Test 4:")
    print("Input:", words4)
    print("Expected Output: (empty string)")
    print("Actual Output  :", alien_order(words4))
    print()

    # Test 5: Two letters only
    words5 = ["a", "b"]
    print("Test 5:")
    print("Input:", words5)
    print("Expected Output: ab")
    print("Actual Output  :", alien_order(words5))
    print()


if __name__ == "__main__":
    run_tests()
