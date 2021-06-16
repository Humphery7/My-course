def loop(x,y):
    for i in x:
        for j in range(y):
            if i == x[0]:
                k = input("please enter your courses : ").lower()
            else:
                k = int(input("please enter results of courses : "))
            i.append(k)


courses_avaliable = ['Electronics and Electrical Engineering','Computer Science',
                     'Civil Engineering','Mechanical Engineering','Chemical Engineering',
                     'Medicine and Surgery','Dentistry','Nursing','Physics','Chemistry',
                     'Mathematics','Architecture','Law','English','Fine Arts','Music',
                     'Economics','Accounting','International Relations']


