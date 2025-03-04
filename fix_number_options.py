# Add this code to the load_from_file method in QuestionBank class

            # Check for multiple choice format - support both letter (a), b)) and numbered formats (1., 2.)
            letter_option_pattern = re.compile(r'^[a-z]\)\s+.+')
            number_option_pattern = re.compile(r'^\d+\.\s+.+')
            
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
                        number_match = re.match(r'^(\d+)\.\s+(.+)$', line)
                        if number_match:
                            number = int(number_match.group(1))
                            option_text = number_match.group(2)
                            # Convert to letter format (1 -> a, 2 -> b, etc.)
                            letter = chr(96 + number) if 1 <= number <= 26 else chr(96 + (number % 26))
                            converted_option = f"{letter}) {option_text}"
                            options.append(converted_option)
