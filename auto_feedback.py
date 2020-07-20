import re


def auto_feedback():
    student_name = input('Student name: ')
    template = str(input('Feedback template: '))
    feedback = template.replace('we', f'{student_name} and I', 1)
    print(f'{feedback} Great job today {student_name}!' + ' Keep practicing your English and working hard!' +
          f" If you enjoyed today's lesson {student_name} please remember to leave a 5 apple feedback," +
          f' I would really appreciate it :) See you next time {student_name}!')


auto_feedback()



