import re


def auto_feedback():
    student_name = input('Student name: ')
    new_student = input('New Student?: ')
    template = str(input('Feedback template: '))
    feedback = template.replace('we', f'{student_name} and I', 1)
    if new_student in ['no', 'No', 'n']:
        print(f'{feedback} Fantastic job today {student_name}! Keep practicing your English and working hard, you are improving every class! See you next time {student_name}.' +
            ' 亲爱的父母，如果您喜欢今天的课程，请考虑给我一个5分的苹果评估。 这项评估对我的工作非常重要。 非常感谢!' +
            ' From, Teacher Carlos ZDG.')
    else:
        print(f'{feedback} Fantastic job today {student_name}! It was great meeting you. Keep up the great work, and I hope to see you in my class again soon.' +
            ' 亲爱的父母，如果您喜欢今天的课程，请考虑给我一个5分的苹果评估。 这项评估对我的工作非常重要。 非常感谢!' +
            ' From, Teacher Carlos ZDG.')


auto_feedback()



