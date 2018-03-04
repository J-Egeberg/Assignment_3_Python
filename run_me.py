from file_handler import download_csv_sheet
import question1, question3, question4, question5


def print_question_separator(question_number):
    print("\nQuestion " + question_number, end="\n" + 100 * "-" + "\n")


csv_sheet_name = download_csv_sheet()
with open(csv_sheet_name) as f:
    print_question_separator("1")
    question1.run(f)

    print_question_separator("3")
    question3.run(f)

    print_question_separator("4")
    question4.run(f)

    print_question_separator("5")
    question5.run(f)

    # put everything that is needed to run a question into it's own run function and call it here with the question separator
    # viz question num 3
