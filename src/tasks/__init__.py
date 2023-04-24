from . import ace, conll03, rams


TASK_ID_TO_TASKS = {
    "ACE05_NER": "src.tasks.ace",
    "ACE05_VER": "src.tasks.ace",
    "ACE05_RE": "src.tasks.ace",
    "ACE05_EE": "src.tasks.ace",
    "RAMS_EAE": "src.tasks.rams",
    "CoNLL03_NER": "src.tasks.conll03",
}

__all__ = ["ace", "rams", "conll03", "TASK_ID_TO_TASKS"]
