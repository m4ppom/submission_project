from django.shortcuts import render

db = {
    'teacher': {
        'name': '유태영'
    },
    'students': [
        {
            'name': '홍길동'
            'age': 26
        },
        {
            'name': '김길동'
            'age': 25
        },
        {
            'name': '박길동'
            'age': 28
        },
    ],
}


def info(request):
    teacher = db.get('teacher')  # dict
    students = db.get('students')  # list of dict)
    return render(request, 'info.html', {
        'teacher' : teacher,
        'students' : students,
    })


def student(request, name):
    for student in db.get('students'):
        if student.get('name') == name:
            age = student.get('age')
            break

    return render(request, 'student.html', {
        'name' : name,
        'age' : age,
    })
# Create your views here.
