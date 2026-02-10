from firebase_config import database

# Methods to interact with the database

# Create note with user id and note content
def create_note(note, uid):
    data = {"user_id": uid, "note": note}
    database.child("notes").push(data)

# Get notes for the use with given user id
def get_notes(uid):
    values = database.child("notes").get()

    if not values:
        return []
    
    notes = []
    for key, value in values.items():
        if uid == value["user_id"]:
            notes.append(value["note"])
    return notes


# Delete note with given note id and user id
def delete_note(note_id, uid):
    values = database.child("notes").get()
    if not values:
        return False
    
    for key, value in values.items():
        if value["user_id"] == uid:
            database.child("notes").child(note_id).delete()
            
    return True

# Update the note with given note id and user id
def update_note(note_id, note, uid):
    data = {"user_id": uid, "note": note}
    # values = database.child("notes").child(note_id)
    values = database.child("notes").get()
    # values = values.get()

    # if not values:
    #     return False
    
    # if values["user_id"] != uid:
    #     return False
    
    # database.child("notes").child(note_id).update(data)

    for key, value in values.items():
        if value["user_id"] == uid:
            database.child("notes").child(note_id).update(data)
        return True
    
    