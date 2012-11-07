import pymongo

def remove_lowest_score():
    connection = pymongo.Connection("mongodb://localhost", 
                                    safe=True)    
    db = connection.students
    grades = db.grades

    query = {'type': 'homework'}
    #projection = {'student_id': 1, 'score': 1, '_id': 0}
    sort_exp = [('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)]

    try:
        cursor = grades.find(query).sort(sort_exp)

        prev_student_id = -1

        for doc in cursor:
            if (prev_student_id != doc['student_id']):
                prev_student_id = doc['student_id']
                grades.remove(doc)

        print grades.count()

    except:
        print "Unexpected error:", sys.exc_info()[0]

remove_lowest_score()