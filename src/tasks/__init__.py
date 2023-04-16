from . import ace, rams


TASK_ID_TO_TASKS = {
    "ACE05_NER": "src.tasks.ace",
    "ACE05_VER": "src.tasks.ace",
    "ACE05_RE": "src.tasks.ace",
    "ACE05_EE": "src.tasks.ace",
    "RAMS_EAE": "src.tasks.rams",
}

__all__ = ["ace", "rams", "TASK_ID_TO_TASKS"]
