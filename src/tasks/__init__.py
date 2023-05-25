from typing import Dict, List

from . import ace, conll03, rams, tacred, ontonotes, ncbidisease, bc5cdr, diann, wnut


TASK_ID_TO_TASKS = {
    "ACE05_NER": "src.tasks.ace",
    "ACE05_VER": "src.tasks.ace",
    "ACE05_RE": "src.tasks.ace",
    "ACE05_RC": "src.tasks.ace",
    "ACE05_EE": "src.tasks.ace",
    "ACE05_EAE": "src.tasks.ace",
    "RAMS_EAE": "src.tasks.rams",
    "CoNLL03_NER": "src.tasks.conll03",
    "Europarl_NER": "src.tasks.conll03",
    "TACRED_SF": "src.tasks.tacred",
    "OntoNotes5_NER": "src.tasks.ontonotes",
    "NcbiDisease_NER": "src.tasks.ncbidisease",
    "DIANN": "src.tasks.diann",
    "WNUT17": "src.tasks.wnut",
}

__all__ = [
    "ace",
    "rams",
    "conll03",
    "tacred",
    "ontonotes",
    "ncbidisease",
    "bc5cdr",
    "diann",
    "wnut",
    "TASK_ID_TO_TASKS",
    "task_id_to_guidelines",
]


def task_id_to_guidelines(task_id: str) -> Dict[str, Dict[str, List[str]]]:
    """
    Return the guidelines for a given task.

    Args:
        task_id (str): The task id.

    Returns:
        The guidelines for the task.
    """
    if task_id.lower() == "ace05":
        from src.tasks.ace.guidelines_gold import GUIDELINES

        return GUIDELINES
    elif task_id.lower() == "rams":
        from src.tasks.rams.guidelines_gold import GUIDELINES

        return GUIDELINES
    elif task_id.lower() == "conll03":
        from src.tasks.conll03.guidelines_gold import GUIDELINES

        return GUIDELINES
    elif task_id.lower() == "tacred":
        from src.tasks.tacred.guidelines_gold import GUIDELINES

        return GUIDELINES
    elif task_id.lower() == "ontonotes5":
        from src.tasks.ontonotes.guidelines_gold import GUIDELINES

        return GUIDELINES
    elif task_id.lower() == "ncbidisease":
        from src.tasks.ncbidisease.guidelines_gold import GUIDELINES

        return GUIDELINES
    elif task_id.lower() == "bc5cdr":
        from src.tasks.bc5cdr.guidelines_gold import GUIDELINES

        return GUIDELINES
    elif task_id.lower() == "diann":
        from src.tasks.diann.guidelines_gold import GUIDELINES

        return GUIDELINES
    elif task_id.lower() == "wnut17":
        from src.tasks.wnut.guidelines_gold import GUIDELINES

        return GUIDELINES
    else:
        raise ValueError(f"Task {task_id} not supported.")
