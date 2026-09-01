import spacy


nlp = spacy.load("en_core_web_sm")


def extract_entities(text: str):
    """
    Dynamically extracts named entities from text.

    Returns:
        [
            {
                "text": "...",
                "type": "..."
            }
        ]
    """

    doc = nlp(text)

    entities = []

    for entity in doc.ents:

        entities.append({
            "text": entity.text,
            "type": entity.label_,
        })

    return entities