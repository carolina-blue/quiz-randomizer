import os
import docx
from docx.shared import Pt
import re

def create_numbered_test_txt():
    """Create a test file with numbered options"""
    txt_content = """What is the capital of Italy?
1. Madrid
2. Berlin
3. Rome
4. Athens
Answer Feedback: Rome is the capital of Italy

Which planet is the largest in our solar system?
1. Mars
2. Jupiter
3. Earth
4. Saturn
Answer Feedback: Jupiter is the largest planet
"""
    with open('numbered_test.txt', 'w') as f:
        f.write(txt_content)
    print("Created numbered_test.txt with numbered options")
    
    return 'numbered_test.txt'

def test_text_parser(filename):
    """Test parsing a text file with numbered options"""
    print(f"\nTesting parser with {filename}")
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Split into question blocks
    question_blocks = re.split(r'\n\s*\n', content)
    
    for i, block in enumerate(question_blocks, 1):
        if not block.strip():
            continue
            
        print(f"\nProcessing question block {i}:")
        lines = block.strip().split('\n')
        question_text = lines[0]
        print(f"Question: {question_text}")
        
        # Check for answer feedback
        feedback_pattern = re.compile(r'^Answer\s+Feedback:\s+.+')
        feedback_lines = [line for line in lines if feedback_pattern.match(line)]
        feedback = feedback_lines[0] if feedback_lines else None
        
        # Remove feedback line from lines
        if feedback:
            lines = [line for line in lines if not feedback_pattern.match(line)]
            print(f"Feedback: {feedback}")
        
        # Check for different option formats
        letter_option_pattern = re.compile(r'^[a-z]\)\s+.+')
        number_option_pattern = re.compile(r'^\d+\.\s+.+')
        
        has_letter_options = any(letter_option_pattern.match(line) for line in lines[1:])
        has_number_options = any(number_option_pattern.match(line) for line in lines[1:])
        
        print(f"Has letter options: {has_letter_options}")
        print(f"Has number options: {has_number_options}")
        
        # Process options
        options = []
        for line in lines[1:]:
            # Check for letter options
            if letter_option_pattern.match(line):
                options.append(line)
            # Check for number options
            elif number_option_pattern.match(line):
                number_match = re.match(r'^(\d+)\.\s+(.+)$', line)
                if number_match:
                    number = int(number_match.group(1))
                    option_text = number_match.group(2)
                    # Convert to letter format (1 -> a, 2 -> b, etc.)
                    letter = chr(96 + number) if 1 <= number <= 26 else chr(96 + (number % 26))
                    converted_option = f"{letter}) {option_text}"
                    options.append(converted_option)
        
        print("Processed options:")
        for opt in options:
            print(f"  {opt}")

def main():
    # Create test file
    test_file = create_numbered_test_txt()
    
    # Test parser
    test_text_parser(test_file)
    
    print("\nTest complete. Copy the relevant code into quiz_randomizer.py")

if __name__ == "__main__":
    main()
