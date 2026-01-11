
class Solution:
   # write python program to reverse a string without loop
   def reverse_string(self, s: str):
      return s[::-1]

   # write python program to reverse a string with loop
   def reverse_string_loop(self, s: str):
      new_string = ""
      for i in range(len(s)-1, -1, -1):
         new_string += s[i]
      return new_string

   # write python program to reverse words in a string
   def reverse_string_in_words(self, s: str):
      return " ".join(s.split()[::-1])

if __name__ == "__main__":
   data: str = "I am anand sogalad"
   result = Solution().reverse_string(data) # dalagos dnana ma I
   result1 = Solution().reverse_string_loop(data) # dalagos dnana ma I

   print(result, result1, sep="\n")

   result2 = Solution().reverse_string_in_words(data) # sogalad anand am I
   print(result2)

# what is the difference between method overriding and method overloading?
# what are the oops principles?
# how do you handle flaky test cases
# what are the different locator starategies in selenium
# asked to find an element using xpath
# what are xpath methods
# asked to find element usinf ancestor element strategy
# what is the difference between selenium and playwright
# why are you looking for change etc..
