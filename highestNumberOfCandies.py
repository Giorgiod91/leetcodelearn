from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Maximaler Wert 
        max_candies = max(candies)
        
      
        result = []
        for candy in candies:
           
            result.append((candy + extraCandies) >= max_candies)
        
      
        return result

# Instanz der Klasse erstellen
solution = Solution()

# Testen der Funktion
result = solution.kidsWithCandies([2, 3, 5, 1, 3], 3)
print(result)  # Ausgabe: [True, True, True, False, True]




result = solution.kidsWithCandies([2, 3, 5, 1, 3], 3)
print(result)
