requirements = {
    "robotType": "Flex",
    "apiLevel": "2.15",
}

# This is an example of how to construct a variable length list of integers
# in this case we have 2 lists we want
# these are the defaults we want constructed from the protocol parameters
# 1) a list of volumes for inserts
#    vol_inserts = [1, 1, 1, 1, 2, 2, 2, 2]
# 2) a list of volumes for vectors
#    vol_vectors = [1, 1, 1, 1, 2, 2, 2, 2]


def run(protocol):
    # Instantiate and set the defaults for your variables
    # that are mapped to the protocol parameters
    # These should match the defaults defined in your parameters json
    insert_1 = 1
    vector_1 = 1
    insert_2 = 1
    vector_2 = 1
    insert_3 = 1
    vector_3 = 1
    insert_4 = 1
    vector_4 = 1
    insert_5 = 2
    vector_5 = 2
    insert_6 = 2
    vector_6 = 2
    insert_7 = 2
    vector_7 = 2
    insert_8 = 2
    vector_8 = 2

    # if the get_values function is defined,
    # as it would be when this protocol is downloaded from the protocol library,
    # read the values from the json string there
    # overwriting the defaults defined above
    try:
        [
            insert_1,
            vector_1,
            insert_2,
            vector_2,
            insert_3,
            vector_3,
            insert_4,
            vector_4,
            insert_5,
            vector_5,
            insert_6,
            vector_6,
            insert_7,
            vector_7,
            insert_8,
            vector_8,
        ] = get_values(
            "insert_1",
            "vector_1",
            "insert_2",
            "vector_2",
            "insert_3",
            "vector_3",
            "insert_4",
            "vector_4",
            "insert_5",
            "vector_5",
            "insert_6",
            "vector_6",
            "insert_7",
            "vector_7",
            "insert_8",
            "vector_8",
        )
    except NameError:
        # get_values is not defined, so proceed with defaults
        pass
    vol_inserts = []
    for i in range(1, 9):
        if locals()["insert_" + str(i)] != 0:
            vol_inserts.append(int(locals()["insert_" + str(i)]))
    vol_vectors = []
    for i in range(1, 9):
        if locals()["vector_" + str(i)] != 0:
            vol_vectors.append(int(locals()["vector_" + str(i)]))
    # inserts and vectors must match
    if len(vol_inserts) != len(vol_vectors):
        raise Exception("Number of inserts and vectors must match")
    # at least one insert and vector must be set
    if len(vol_inserts) == 0:
        raise Exception("No inserts or vectors set")

    protocol.comment(f"vol_inserts: {vol_inserts}")
    protocol.comment(f"vol_vectors: {vol_vectors}")
