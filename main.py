import cache
import database_version
# import dict_parser
import numpy as np
import text_to_vector


# def uncached_main_old():
#     print('loading definitions')
#     definitions = dict_parser.get_dictionary_into_list()
#     print('loading vector model')
#     nlp_model = text_to_vector.load_model()
#     vectors = []
#     c = 0
#     print('turning definitions into vectors')
#     for definition in definitions:
#         print(c)
#         # if c == 0:
#         #     break
#         c += 1
#         vector = nlp_model(' '.join(definition))[0]
#         vectors.append(vector)

#     vectors = np.asarray(vectors)
#     cache.load_index()
#     database = cache.add_vectors(vectors)
#     while True:
#         find_similar_definition(nlp_model, database, definitions)


def find_similar_definition(model, database, definitions):
    text = input("Describe the word you're thinking of and press enter:\n")
    vector = model(text)[0]
    _, indexes = database.search(np.asarray([vector]), 15)
    for index in indexes[0]:
        print(definitions[index])


def main():
    vectors, dictionary = database_version.retrieve_from_database()
    vectors = np.asarray([np.asarray(vector) for vector in vectors])
    cache.load_index()
    database = cache.add_vectors(vectors)
    print('loading vector model')
    nlp_model = text_to_vector.load_model()
    while True:
        find_similar_definition(nlp_model, database, dictionary)


main()