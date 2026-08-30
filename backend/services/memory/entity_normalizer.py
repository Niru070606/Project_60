def normalize_entities(
    text: str,
    entities: list[dict],
):
    """
    Converts spaCy entity results into
    Project Lecyrus entity types.

    Does not hard-code specific people,
    places, or organizations.
    """

    normalized = []

    for entity in entities:

        entity_text = entity["text"].strip()
        entity_type = entity["type"]

        # Start with spaCy's classification.
        normalized_type = "UNKNOWN"

        if entity_type == "PERSON":
            normalized_type = "PERSON"

        elif entity_type == "ORG":
            normalized_type = "ORGANIZATION"

        elif entity_type == "GPE":
            normalized_type = "PLACE"

        elif entity_type in {
            "LOC",
            "FAC",
        }:
            normalized_type = "PLACE"

        elif entity_type in {
            "PRODUCT",
            "WORK_OF_ART",
        }:
            normalized_type = "CONCEPT"

        normalized.append({
            "text": entity_text,
            "type": normalized_type,
            "source_type": entity_type,
        })

    return normalized