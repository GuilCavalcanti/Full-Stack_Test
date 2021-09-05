def reassign_labels(peptides):

    peptides_length = len(peptides)

    # origin peptide's ids list with non-numeric text removed and the rest converted to ints
    original_ids = [pep.replace("pep_", "") for pep in peptides]
    original_ids = list(map(int, original_ids))

    # sorted peptide's ids list
    sorted_ids = sorted(original_ids)

    # peptide's ids with gaps removed
    ids_gaps_removed = list(range(1, peptides_length + 1))

    # result labels empty list
    result = [None] * peptides_length

    for i in range(peptides_length):
        # original id
        origin_id = original_ids[i]
        # find original id index in sorted list
        sorted_id_index = sorted_ids.index(origin_id)
        # get new id from sorted list by index
        new_id = ids_gaps_removed[sorted_id_index]
        # set new id with text added to result list
        result[i] = f'pep_{new_id}'

    return result
