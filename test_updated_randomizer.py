import os
from quiz_randomizer import QuestionBank, QuizRandomizer

def run_test():
    print("Loading question bank from test_formatted_quiz.docx...")
    question_bank = QuestionBank()
    question_bank.load_from_file("test_formatted_quiz.docx")
    
    print(f"Loaded {question_bank.get_size()} questions")
    
    # Print the questions and formatting
    for i, question in enumerate(question_bank.questions, 1):
        print(f"\nQuestion {i}: {question.text}")
        for j, option in enumerate(question.options):
            print(f"  {option}")
        if question.feedback:
            print(f"  {question.feedback}")
    
    # Create a randomizer and generate quizzes
    randomizer = QuizRandomizer(question_bank)
    
    # Make sure output directory exists
    if not os.path.exists("quizzes"):
        os.makedirs("quizzes")
    
    # Generate a quiz in each format
    print("\nGenerating quizzes in different formats...")
    randomizer.create_quizzes(
        num_quizzes=1,
        questions_per_quiz=2,
        allow_duplicates=False,
        output_format="docx",
        output_dir="quizzes"
    )
    
    randomizer.create_quizzes(
        num_quizzes=1,
        questions_per_quiz=2,
        allow_duplicates=False,
        output_format="pdf",
        output_dir="quizzes"
    )
    
    randomizer.create_quizzes(
        num_quizzes=1,
        questions_per_quiz=2,
        allow_duplicates=False,
        output_format="text",
        output_dir="quizzes"
    )
    
    print("\nDone\! Check the 'quizzes' directory for the output files:")
    print(" - quiz_1.docx (best formatting)")
    print(" - quiz_1.pdf")
    print(" - quiz_1.txt")

if __name__ == "__main__":
    run_test()
