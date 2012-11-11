import pymongo
import sys

def remove_lowest_homework():
    connection = pymongo.Connection("mongodb://localhost", safe=True)    
    
    db = connection.school
    students = db.students

    try:
        cursor = students.find()

        for doc in cursor:
            tempscores = doc['scores']            
            lowestscore = 100
            highestscore = 0            
            
            for tempscore in tempscores:
                if tempscore['type'] == 'homework':
                    if tempscore['score'] > highestscore:
                        highestscore = tempscore['score']
                    if tempscore['score'] < lowestscore:
                        lowestscore = tempscore['score']

            tempscores.remove({'type': 'homework', 'score': lowestscore})
            db.students.update({'_id': doc['_id']}, {'$set': {'scores': tempscores}})

    except:
        print "Unexpected error:", sys.exc_info()[0]

remove_lowest_homework()