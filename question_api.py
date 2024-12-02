import sqlite3
from random import choice, randint

conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

def get_random_gender_with_answer():
    select_q = "SELECT * FROM genders"
    cursor.execute(select_q)
    result = cursor.fetchall()

    word = choice(result)

    return word[0], word[1]


def get_random_verb_with_answer():
    select_q = "SELECT * FROM verbs"
    cursor.execute(select_q)
    result = cursor.fetchall()

    word = choice(result)

    form = randint(1, 6)

    if form == 1:
        return word[0], word[1], "ich"
    elif form == 2:
        return word[0], word[2], "du"
    elif form == 3:
        return word[0], word[3], "er"
    elif form == 4:
        return word[0], word[4], "wir"
    elif form == 5:
        return word[0], word[5], "ihr"
    elif form == 6:
        return word[0], word[6], "Sie"


def get_random_noun_with_answer():
    select_q = "SELECT * FROM nouns"
    cursor.execute(select_q)
    result = cursor.fetchall()

    word = choice(result)

    return word[0], word[1]


class Editor:
    @staticmethod
    def add_gender(added_info):
        command = """
        INSERT OR IGNORE INTO genders (word, gender) VALUES (?, ?)
        """
        cursor.executemany(command, [added_info])
        conn.commit()

    @staticmethod
    def add_noun(added_info):
        command = """
            INSERT OR IGNORE INTO nouns (singular, plural) VALUES (?, ?)
            """
        cursor.executemany(command, [added_info])
        conn.commit()

    @staticmethod
    def add_verb(added_info):
        command = """
            INSERT OR IGNORE INTO verbs (infinitive, ich, du, er, wir, ihr, Sie) VALUES (?, ?, ?, ?, ?, ?, ?)
            """
        print(added_info)
        cursor.executemany(command, [added_info])
        conn.commit()