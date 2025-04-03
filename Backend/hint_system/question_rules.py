QUESTION_HINT_RULES = {
    "Can Place Flowers": [
        {
            "trigger": "edge_cases",
            "patterns": [
                r"range\(1,\s*len",
                r"flowerbed\[i-1\]"
            ],
            "hints": [
                "Handle first and last elements separately before the main loop",
                "Check if i-1 or i+1 are valid indices before accessing"
            ]
        },
        {  # THIS RULE WAS MISSING PATTERNS
            "trigger": "adjacent_check",
            "patterns": [  # ADD THIS
                r"flowerbed\[i-1\] == 0",
                r"flowerbed\[i\+1\] == 0"
            ],
            "hints": [
                "Remember flowers can't be adjacent. Check both sides before placing"
            ]
        }
    ],
   
    "Reverse Vowels of a String": [
        {
            "trigger": "vowel_case_missing",
            "patterns": [
                r"vowels\s*?=\s*?['\"]aeiou['\"]",  # More flexible whitespace
                r"vowels\s*?=\s*?['\"]AEIOU['\"]"
            ],
            "hints": [
                "Include both lowercase and uppercase vowels (A, E, I, O, U)",
                "Use: vowels = 'aeiouAEIOU' for complete vowel checking"
            ]
        },
        {
            "trigger": "incorrect_reversal",
            "patterns": [
                r"\[::-1\]",  # Direct match for reversal pattern
                r"\[\s*?c\s*?for.*?\]\s*?\[\s*?::-1\s*?\]"  # Match filtered list reversal
            ],
            "hints": [
                "Reversing a filtered list breaks original vowel positions",
                "Use two pointers (start and end) to swap vowels in-place"
            ]
        }
    ]
}