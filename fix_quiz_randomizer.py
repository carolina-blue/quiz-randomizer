#\!/usr/bin/env python3
"""
This script will fix the quiz_randomizer.py file to properly handle
numbered options (1., 2., etc.) in addition to letter options (a), b), etc.)
"""
import os
import re
import sys

def main():
    """Fix the quiz_randomizer.py file"""
    # Check if quiz_randomizer.py exists
    if not os.path.exists('quiz_randomizer.py'):
        print("quiz_randomizer.py not found\!")
        sys.exit(1)
    
    # Read the file
    with open('quiz_randomizer.py', 'r') as f:
        content = f.read()
    
    # Make a backup
    with open('quiz_randomizer.py.bak', 'w') as f:
        f.write(content)
    
    # Fix the _load_from_docx method
    fixed_docx_loader = """    def _load_from_docx(self, filename: str) -> None:
        \"\"\"Load questions from a DOCX file, preserving formatting for both letter and numbered options.\"\"\"
        doc = docx.Document(filename)
        
        # We'll process paragraphs sequentially
        current_question = None
        current_options = []
        current_feedback = None
        
        for para in doc.paragraphs:
            text = para.text.strip()
            if not text:
                # Empty paragraph means end of current question
                if current_question:
                    question_type = "free-response"
                    if current_options:
                        question_type = "multiple-choice"
                    elif current_question.lower().find("true/false") > -1:
                        question_type = "true-false"
                        current_options = ["True", "False"]
                    
                    self.add_question(Question(current_question, question_type, current_options, current_feedback))
                    current_question = None
                    current_options = []
                    current_feedback = None
            elif text.startswith("Answer Feedback:"):
                # This is feedback for the current question
                current_feedback = text
            # Check for letter-style options (a), b), etc.)
            elif any(text.startswith(f"{chr(97 + i)})") for i in range(26)):
                # This is a letter option - check for bold parts
                option_text = text
                
                # Explicitly check each run for bold property
                has_bold = False
                
                for run in para.runs:
                    if run.bold is True:  # Must explicitly check against True
                        has_bold = True
                        bold_text = run.text
                        # Mark the bold part with markdown
                        option_text = option_text.replace(bold_text, f"**{bold_text}**")
                        break
                
                current_options.append(option_text)
            # Check for number-style options (1., 2., etc.)
            elif re.match(r'^\\d+\\.\\s+.+', text):
                # This is a numbered option
                number_match = re.match(r'^(\\d+)\\.\\s+(.+)$', text)
                if number_match:
                    number = int(number_match.group(1))
                    content = number_match.group(2)
                    
                    # Convert to letter format (1 -> a, 2 -> b, etc.)
                    letter = chr(96 + number) if 1 <= number <= 26 else chr(96 + (number % 26))
                    letter_prefix = f"{letter}) "
                    
                    # Check for bold formatting
                    has_bold = False
                    for run in para.runs:
                        if run.bold is True:
                            has_bold = True
                            # Find which part of the text is the bold part
                            bold_text = run.text
                            if bold_text in content:
                                # Mark content as bold
                                modified_content = content.replace(bold_text, f"**{bold_text}**")
                                option_text = f"{letter_prefix}{modified_content}"
                                break
                    
                    # If no bold parts found, use plain formatting
                    if not has_bold:
                        option_text = f"{letter_prefix}{content}"
                    
                    current_options.append(option_text)
            elif not current_question:
                # This must be a new question text
                current_question = text
        
        # Add the last question if there is one
        if current_question:
            question_type = "free-response"
            if current_options:
                question_type = "multiple-choice"
            elif current_question.lower().find("true/false") > -1:
                question_type = "true-false"
                current_options = ["True", "False"]
            
            self.add_question(Question(current_question, question_type, current_options, current_feedback))"""
    
    # Define the updated text file loader code
    fixed_txt_loader = """        # Process text-based content (TXT or RTF)
        # Split content into individual questions
        question_blocks = re.split(r'\\n\\s*\\n', content)
        
        for block in question_blocks:
            if not block.strip():
                continue
            
            lines = block.strip().split('\\n')
            if not lines:  # Skip empty blocks
                continue
                
            question_text = lines[0]
            
            # Try to determine question type
            question_type = "free-response"  # Default
            options = []
            feedback = None
            
            # Check for answer feedback
            feedback_pattern = re.compile(r'^Answer\\s+Feedback:\\s+.+')
            feedback_lines = [line for line in lines if feedback_pattern.match(line)]
            if feedback_lines:
                feedback = feedback_lines[0]
                # Remove feedback line from lines to process
                lines = [line for line in lines if not feedback_pattern.match(line)]
            
            # Check for multiple choice format - support both letter (a), b)) and numbered formats (1., 2.)
            letter_option_pattern = re.compile(r'^[a-z]\\)\\s+.+')
            number_option_pattern = re.compile(r'^\\d+\\.\\s+.+')
            
            has_letter_options = any(letter_option_pattern.match(line) for line in lines[1:])
            has_number_options = any(number_option_pattern.match(line) for line in lines[1:])
            has_options = has_letter_options or has_number_options
            
            if has_options:
                question_type = "multiple-choice"
                options = []
                for line in lines[1:]:
                    # Check for letter-style options (a), b), etc.)
                    if letter_option_pattern.match(line):
                        options.append(line)
                    # Check for number-style options (1., 2., etc.)
                    elif number_option_pattern.match(line):
                        # Convert numbered format to letter format for consistency
                        number_match = re.match(r'^(\\d+)\\.\\s+(.+)$', line)
                        if number_match:
                            number = int(number_match.group(1))
                            option_text = number_match.group(2)
                            # Convert to letter format (1 -> a, 2 -> b, etc.)
                            letter = chr(96 + number) if 1 <= number <= 26 else chr(96 + (number % 26))
                            converted_option = f"{letter}) {option_text}"
                            options.append(converted_option)"""
    
    # Replace the load_from_docx method - simple search and replace won't work because of the file state
    # So we'll search for def _load_from_docx, and replace the whole function
    docx_loader_pattern = re.compile(r'def\s+_load_from_docx.*?self\.add_question\(Question\(current_question,\s*question_type,\s*current_options,\s*current_feedback\)\)', re.DOTALL)
    if docx_loader_pattern.search(content):
        content = docx_loader_pattern.sub(fixed_docx_loader, content)
        print("Fixed _load_from_docx method")
    else:
        print("Warning: Could not find _load_from_docx method to replace")
    
    # Now update the text file loader - we need to find the processing section
    # Look for "# Process text-based content" and replace the following section
    txt_loader_pattern = re.compile(r'# Process text-based content.*?self\.add_question\(Question\(question_text,\s*question_type,\s*options,\s*feedback\)\)', re.DOTALL)
    if txt_loader_pattern.search(content):
        content = txt_loader_pattern.sub(fixed_txt_loader + '\n            \n            # Check for true/false\n            elif any(re.search(r\'true\\\\s*\\/\\\\s*false\', line.lower()) for line in lines):\n                question_type = "true-false"\n                options = ["True", "False"]\n            \n            self.add_question(Question(question_text, question_type, options, feedback))', content)
        print("Fixed text file loader")
    else:
        print("Warning: Could not find text processing section to replace")
    
    # Write the fixed file
    with open('quiz_randomizer.py', 'w') as f:
        f.write(content)
    
    print("\nDone\! The quiz_randomizer.py file has been updated to handle numbered options.")
    print("A backup of the original file was saved as quiz_randomizer.py.bak")

if __name__ == "__main__":
    main()
