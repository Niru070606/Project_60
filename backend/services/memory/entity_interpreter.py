def interpret_entities(
    text: str,
    candidates: list[dict],
):
    """
    Interprets entity candidates using their
    extracted source information and context.

    This layer decides what each candidate
    represents. It does not resolve the entity
    to a database record yet.
    """

    interpreted = []

    for candidate in candidates:

        entity_text = candidate["text"].strip()
        source_type = candidate.get("source_type")

        normalized_type = "UNKNOWN"

        # Strong evidence from spaCy
        if source_type == "PERSON":
            normalized_type = "PERSON"

        elif source_type == "ORG":
            normalized_type = "ORGANIZATION"

        elif source_type in {
            "LOC",
            "GPE",
            "FAC",
        }:
            normalized_type = "PLACE"

        # Contextual interpretation
        words = text.lower()

        if entity_text.lower() == "ai":
            normalized_type = "CONCEPT"

        elif (
            "project " in words
            and entity_text.lower().startswith("project ")
        ):
            normalized_type = "PROJECT"

        interpreted.append({
            "text": entity_text,
            "type": normalized_type,
            "source": candidate.get("source"),
            "source_type": source_type,
        })

    return interpreted