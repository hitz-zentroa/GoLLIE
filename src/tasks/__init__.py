from . import ace, conll03, rams, tacred


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
    "TACRED": "src.tasks.tacred",
}

__all__ = ["ace", "rams", "conll03", "tacred", "TASK_ID_TO_TASKS"]
