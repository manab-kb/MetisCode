import unittest
import os
from hint_system.hint_generator import AdaptiveHintGenerator
script_directory = os.path.dirname(os.path.abspath(__file__))

class TestHintSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.generator = AdaptiveHintGenerator(f"{script_directory}/hint_system/questions.json")
    
    def test_can_place_flowers(self):
        with open("sample_code/can_place_flowers_buggy.py") as f:
            code = f.read()
            
        hints = self.generator.generate_hints(
            "Can Place Flowers",
            code
        )
        self.assertGreater(len(hints), 0)
        print("\nCan Place Flowers Hints:")
        for h in hints: print(f"- {h['hint']}")

    def test_reverse_vowels(self):
        with open("sample_code/reverse_vowels_buggy.py") as f:
            code = f.read()
            
        hints = self.generator.generate_hints(
            "Reverse Vowels of a String",
            code
        )
        self.assertGreater(len(hints), 0)
        print("\nReverse Vowels Hints:")
        for h in hints: print(f"- {h['hint']}")

if __name__ == "__main__":
    unittest.main()