def reverseVowels(s):
    # Buggy implementation with two key issues:
    # 1. Only checks lowercase vowels
    # 2. Reverses entire list instead of swapping positions
    vowels = 'aeiou'
    vowel_list = [c for c in s if c in vowels]
    reversed_vowels = vowel_list[::-1]
    
    result = []
    vowel_idx = 0
    for char in s:
        if char in vowels:
            result.append(reversed_vowels[vowel_idx])
            vowel_idx += 1
        else:
            result.append(char)
    return ''.join(result)