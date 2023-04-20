from typing import List


def to_iob_encoding(tags: List[str]) -> List[str]:
    # From IOB2 or BILOU
    prev_tag_b: str = "O"
    prev_tag_t: str = ""

    for i in range(len(tags)):
        tag = tags[i]
        if tag == "O":
            prev_tag_b = "O"
            prev_tag_t = ""
        else:
            try:
                b, t = tag.split("-")
            except ValueError:
                raise ValueError(f"Error tag {tag}, unable to split the tag in 2 fields.")
            if (b == "B" or b == "U") and prev_tag_b != "O" and prev_tag_t == t:
                tags[i] = f"B-{t}"
            else:
                tags[i] = f"I-{t}"

            prev_tag_b = b
            prev_tag_t = t

    return tags


def to_iob2_encoding(tags: List[str]) -> List[str]:
    # From IOB or BILOU
    prev_tag_b: str = "O"
    prev_tag_t: str = ""
    for i in range(len(tags)):
        tag = tags[i]
        if tag == "O":
            prev_tag_b = "O"
            prev_tag_t = ""
        else:
            try:
                b, t = tag.split("-")
            except ValueError:
                raise ValueError(f"Error tag {tag}, unable to split the tag in 2 fields.")

            if (b == "B" or b == "U") or ((prev_tag_b == "O") or (prev_tag_t != "" and prev_tag_t != t)):
                tags[i] = f"B-{t}"
            else:
                tags[i] = f"I-{t}"

            prev_tag_b = b
            prev_tag_t = t

    return tags


def to_bilou_encoding(tags: List[str]) -> List[str]:
    # From IOB or IOB2

    prev_word_tag_tmp: str = ""
    for i in range(len(tags)):
        tag = tags[i]
        if tag == "O":
            if prev_word_tag_tmp != "":
                try:
                    prev_b, prev_t = prev_word_tag_tmp.split("-")
                except ValueError:
                    raise ValueError(f"Error in tag {prev_word_tag_tmp}, unable to split the tag in 2 fields.")

                if prev_b == "B":
                    tags[i - 1] = f"U-{prev_t}"
                else:
                    tags[i - 1] = f"L-{prev_t}"

            prev_word_tag_tmp: str = ""

        else:
            try:
                b, t = tag.split("-")
            except ValueError:
                raise ValueError(f"Error in tag {prev_word_tag_tmp}, unable to split the tag in 2 fields.")

            if prev_word_tag_tmp == "":
                if b == "U":
                    prev_word_tag_tmp = ""
                else:
                    prev_word_tag_tmp = f"B-{t}"

            else:
                try:
                    prev_b, prev_t = prev_word_tag_tmp.split("-")
                except ValueError:
                    raise ValueError(f"Error in tag {prev_word_tag_tmp}, unable to split the tag in 2 fields.")

                if b == "U":
                    if prev_b == "B":
                        tags[i - 1] = f"U-{prev_t}"
                    else:
                        tags[i - 1] = f"L-{prev_t}"

                    prev_word_tag_tmp = ""

                elif b == "B":
                    if prev_b == "B":
                        tags[i - 1] = f"U-{prev_t}"
                    else:
                        tags[i - 1] = f"L-{prev_t}"

                    prev_word_tag_tmp = f"B-{t}"

                else:
                    if prev_t != t:
                        if prev_b == "B":
                            tags[i - 1] = f"U-{prev_t}"
                        else:
                            tags[i - 1] = f"L-{prev_t}"

                        prev_word_tag_tmp = f"B-{t}"
                    else:
                        if prev_b == "B":
                            tags[i - 1] = f"B-{prev_t}"
                        else:
                            tags[i - 1] = f"I-{prev_t}"

                        prev_word_tag_tmp = f"I-{t}"

    if prev_word_tag_tmp != "":
        try:
            prev_b, prev_t = prev_word_tag_tmp.split("-")
        except ValueError:
            raise ValueError(f"Error in tag {prev_word_tag_tmp}, unable to split the tag in 2 fields.")

        if prev_b == "B":
            tags[-1] = f"U-{prev_t}"
        else:
            tags[-1] = f"L-{prev_t}"

    return tags


def rewrite_labels(labels, encoding: str = "iob2") -> List[str]:
    if encoding.lower() == "iob":
        return to_iob_encoding(labels)
    elif encoding.lower() == "iob2":
        return to_iob2_encoding(labels)
    elif encoding.lower() == "bilou":
        return to_bilou_encoding(labels)
    else:
        raise NotImplementedError(f"Encoding {encoding} not supported. Supported encodings [IOB,IOB2,BILOU]")
