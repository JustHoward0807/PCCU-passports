import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Field I need to insert
'''
eventsTitle
eventsDetail
location
organizer
points
type
startTime
endTime
typeInt
'''

# Give credentials
cred = credentials.Certificate('firebase_admin.json')
# init
firebase_admin.initialize_app(cred)
db = firestore.client()

# Clear data in document first to make sure data are clean
def deleteDoc():
    i = 0
    sum = 0
    points = ['德', '智', '體', '群', '美']
    for point in points:
        get_all_doc = db.collection(point).stream()
        for doc in get_all_doc:
            if (i < len(doc.id)):
                db.collection(point).document(doc.id).delete()
                print(f'id: ${doc.id} has been deleted')
                sum += 1
    print(f'total deleted: {sum}')


def uploadFirestore(collection, eventsTitle, eventsDetail, location, organizer, points, type, startTime, endTime, typeInt):
    
    # Document with auto generated id
    doc_ref = db.collection(collection).document()

    if (typeInt == '德'):
        typeInt = 0
    elif (typeInt == '智'):
        typeInt = 1
    elif (typeInt == '體'):
        typeInt = 2
    elif (typeInt == '群'):
        typeInt = 3
    elif (typeInt == '美'):
        typeInt = 4
    else:
        typeInt = '無'

    # Give the values
    doc_ref.set({
        'eventsTitle': eventsTitle,
        'eventsDetail': eventsDetail,
        'location': location,
        'organizer': organizer,
        'points': points,
        'type': type,
        'startTime': startTime,
        'endTime': endTime,
        'typeInt': typeInt,
    })
    
