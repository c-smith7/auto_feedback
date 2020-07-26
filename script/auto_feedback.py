import re


def auto_feedback():
    student_name = input('Student name: ')
    template = str(input('Feedback template: '))
    if template == 'unit':
        score = input('Score: ')
        gender = input('He or She?: ')
        print(f"{student_name} did a fantastic job with today's Unit Assessment. {gender} scored a perfect" +
                f" score of {score}/{score}, great job! {gender} is well prepared to continue onto the next unit" +
                f" to learn new material. Keep up the great work and I will see you next time {student_name}!")
    else:
        feedback = template.replace('we', f'{student_name} and I', 1)
        print(f'{feedback} Great job today {student_name}!' + ' Keep practicing your English and working hard!' +
                f" If you enjoyed today's lesson {student_name} please remember to leave a 5 apple feedback," +
                f' I would really appreciate it :) See you next time {student_name}!')


auto_feedback()



