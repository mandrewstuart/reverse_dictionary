import dict_parser
import numpy as np
import sqlite3
import text_to_vector
from urllib import parse


def convert_vector_to_text(vector):
    data = []
    for idx in range(512):
        data.append(float(vector[idx]))
    return ','.join([str(elem) for elem in data])


def convert_text_to_vector(text):
    return [np.float32(x) for x in text.split(',')]


def prepare():
    print('loading definitions')
    definitions = dict_parser.get_dictionary_into_list()
    print('loading vector model')
    nlp_model = text_to_vector.load_model()
    vectors = []
    c = 0
    print('turning definitions into vectors')
    for definition in definitions:
        print(c)
        # if c == 10:
        #     break
        c += 1
        vector = nlp_model(' '.join(definition))[0]
        vectors.append(vector)

    connection = sqlite3.connect('file.db')
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS data (vector text, label text, defitinion text);")
    for idx in range(c):
        cursor.execute("""INSERT INTO data (vector, label, defitinion) VALUES (
            '{0}', '{1}', '{2}'
        );""".format(
            convert_vector_to_text(vectors[idx]),
            parse.quote(definitions[idx][0]),
            parse.quote(definitions[idx][1])
        ))
    connection.commit()


def retrieve_from_database():
    connection = sqlite3.connect('file.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM data;")
    data = cursor.fetchall()
    vectors = [convert_text_to_vector(row[0]) for row in data]
    dictionary = [[parse.unquote(row[1]), parse.unquote(row[2])] for row in data]
    return vectors, dictionary
