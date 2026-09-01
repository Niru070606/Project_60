import spacy


nlp = spacy.load("en_core_web_sm")


def extract_entity_candidates(text: str):
    """
    Extracts possible entity phrases from text.

    This does NOT decide what an entity is.
    It only generates candidates for the
    interpretation layer.
    """

    doc = nlp(text)

    candidates = []

    # 1. spaCy named entities
    for entity in doc.ents:

        candidates.append({
            "text": entity.text.strip(),
            "source": "ner",
            "source_type": entity.label_,
        })

    # 2. Proper nouns that spaCy may have missed
    for token in doc:

        if token.pos_ == "PROPN":

            candidate = token.text.strip()

            if not candidate:
                continue

            # Avoid duplicates
            already_exists = any(
                item["text"].lower() == candidate.lower()
                for item in candidates
            )

            if not already_exists:

                candidates.append({
                    "text": candidate,
                    "source": "proper_noun",
                    "source_type": None,
                })

    return candidates