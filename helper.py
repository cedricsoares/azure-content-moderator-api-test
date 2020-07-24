import sqlite3
import traceback

DB_PATH = './comments.db'   # Update this path accordingly
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()


def is_table():

    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' 
                AND name='comments' ''')
    
    if c.fetchone()[0]==1 :
        return True
    
    else:
        return False

def create_table():

    try:

       # Keep the initial status as Not Started
        c.execute('''create table comments
                    (comment text, status varchar(20))''')
                    
        # We commit to save the change
        conn.commit()
        print('Created db')

    except Exception as e:
        # print('Error: ', e)
        print(traceback.format_exc())
        return None

def add_to_db(comment, status):

    if not is_table():
        create_table()
    
    try:
        # Keep the initial status as Not Started
        c.execute('''insert into comments values ('{first_value}',
                                               '{second_value}');'''
                                               .format(first_value = comment,
                                               second_value = status))

        # We commit to save the change
        conn.commit()
        return {"comment": comment, "staus": status}
    except Exception as e:
        # print('Error: ', e)
        print(traceback.format_exc())
        return None

def display_content(): 
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    data = []
    c.execute("select * from comments")
    print(c)
    
    for entry in c:
        data.append("Commentaire: {comment}".format(comment=entry["comment"]))
        data.append("Statut: {status} \n".format(status=entry["status"]))
    
    return data

