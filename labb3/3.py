with open('subjects.rtf', 'r') as f:
    subjects_dict = {}
    for line in f:
        subject, lessons = line.split(':')
        total_lessons = 0
        for lesson in lessons.split():
            num_lessons = int(lesson.split('(')[0])
            total_lessons += num_lessons
        subjects_dict[subject] = total_lessons

    print(subjects_dict)