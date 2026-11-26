def merge_entity_candidates(
    candidates: list[dict],
):
    """
    Merges duplicate and overlapping candidates.

    NER candidates provide context, while proper-noun
    candidates can provide more precise entity names.
    """

    if not candidates:
        return []

    cleaned = []

    for candidate in candidates:

        entity_text = candidate["text"].strip()

        if not entity_text:
            continue

        cleaned.append({
            **candidate,
            "text": entity_text,
        })

    # --------------------------------
    # Remove exact duplicates
    # --------------------------------

    unique = []

    seen = set()

    for candidate in cleaned:

        key = (
            candidate["text"].lower(),
            candidate.get("source"),
        )

        if key in seen:
            continue

        seen.add(key)

        unique.append(candidate)

    # --------------------------------
    # Remove proper-noun fragments
    # that are merely parts of a
    # longer candidate (NER or proper_noun).
    # --------------------------------

    merged = []

    for candidate in unique:

        candidate_text = candidate["text"].lower()

        if candidate.get("source") != "proper_noun":
            merged.append(candidate)
            continue

        # Check whether this proper noun is part
        # of any other candidate (NER or proper_noun).
        is_fragment = False

        for other in unique:

            if candidate is other:
                continue

            other_text = other["text"].lower()

            if (
                candidate_text != other_text
                and candidate_text in other_text
            ):
                is_fragment = True
                break

        if not is_fragment:
            merged.append(candidate)

    return merged