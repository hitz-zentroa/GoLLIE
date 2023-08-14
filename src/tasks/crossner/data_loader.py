from typing import Tuple, Union

from src.tasks.conll03.data_loader import load_conll_tsv
from src.tasks.crossner.guidelines import GUIDELINES
from src.tasks.crossner.guidelines_gold import EXAMPLES
from src.tasks.crossner.prompts_ai import ENTITY_DEFINITIONS_AI
from src.tasks.crossner.prompts_literature import ENTITY_DEFINITIONS_LITERATURE
from src.tasks.crossner.prompts_music import ENTITY_DEFINITIONS_MUSIC
from src.tasks.crossner.prompts_natural_science import ENTITY_DEFINITIONS_NATURAL_SCIENCE
from src.tasks.crossner.prompts_politics import ENTITY_DEFINITIONS_POLITICS

from ..utils_data import DatasetLoader, Sampler


class CrossNERDatasetLoader(DatasetLoader):
    """
    A `DatasetLoader` for the CrossNER dataset.

    Args:
        split (`str`):
            The split to load. Can be one of `train`, `validation` or `test`.
        task (`str`):
            The task to load. Can be one of `politics`, `music`, `literature`, `ai` or `natural_science`.

    Raises:
        `ValueError`:
            raised when a not defined value found.
    """

    ENTITY_TO_CLASS_MAPPING = None

    def __init__(self, path_or_split: str, tasks: str, **kwargs) -> None:
        if len(tasks) > 1:
            raise ValueError(
                "CrossNER only supports one task at a time. Please specify only one task in the config file. You"
                f" specified {tasks}"
            )
        task = tasks[0].lower().replace("crossner_", "")

        if task == "politics":
            from src.tasks.crossner.prompts_politics import (
                Country,
                Election,
                Event,
                Location,
                Miscellaneous,
                Organization,
                Person,
                PoliticalParty,
                Politician,
            )

            self.ENTITY_TO_CLASS_MAPPING = {
                "person": Person,
                "organisation": Organization,
                "location": Location,
                "politician": Politician,
                "politicalparty": PoliticalParty,
                "election": Election,
                "event": Event,
                "country": Country,
                "misc": Miscellaneous,
            }

        elif task == "music":
            from src.tasks.crossner.prompts_music import (
                Album,
                Award,
                Band,
                Country,
                Event,
                Location,
                Miscellaneous,
                MusicalArtist,
                MusicalInstrument,
                MusicGenre,
                Organization,
                Person,
                Song,
            )

            self.ENTITY_TO_CLASS_MAPPING = {
                "musicgenre": MusicGenre,
                "song": Song,
                "band": Band,
                "album": Album,
                "musicalartist": MusicalArtist,
                "musicalinstrument": MusicalInstrument,
                "award": Award,
                "event": Event,
                "country": Country,
                "location": Location,
                "organisation": Organization,
                "person": Person,
                "misc": Miscellaneous,
            }

        elif task == "literature":
            from src.tasks.crossner.prompts_literature import (
                Award,
                Book,
                Country,
                Event,
                LiteraryGenre,
                Location,
                Magazine,
                Miscellaneous,
                Organization,
                Person,
                Poem,
                Writer,
            )

            self.ENTITY_TO_CLASS_MAPPING = {
                "book": Book,
                "writer": Writer,
                "award": Award,
                "poem": Poem,
                "event": Event,
                "magazine": Magazine,
                "literarygenre": LiteraryGenre,
                "person": Person,
                "location": Location,
                "organisation": Organization,
                "country": Country,
                "misc": Miscellaneous,
            }

        elif task == "ai":
            from src.tasks.crossner.prompts_ai import (
                Algorithm,
                Conference,
                Country,
                Field,
                Location,
                Metric,
                Miscellaneous,
                Organization,
                Person,
                Product,
                ProgrammingLanguage,
                Researcher,
                Task,
                University,
            )

            self.ENTITY_TO_CLASS_MAPPING = {
                "field": Field,
                "task": Task,
                "product": Product,
                "algorithm": Algorithm,
                "researcher": Researcher,
                "metrics": Metric,
                "university": University,
                "country": Country,
                "person": Person,
                "organisation": Organization,
                "location": Location,
                "programlang": ProgrammingLanguage,
                "conference": Conference,
                "misc": Miscellaneous,
            }
        elif task == "natural_science":
            from src.tasks.crossner.prompts_natural_science import (
                AcademicJournal,
                AstronomicalObject,
                Award,
                ChemicalCompound,
                ChemicalElement,
                Country,
                Discipline,
                Enzyme,
                Event,
                Location,
                Miscellaneous,
                Organization,
                Person,
                Protein,
                Scientist,
                Theory,
                University,
            )

            self.ENTITY_TO_CLASS_MAPPING = {
                "scientist": Scientist,
                "person": Person,
                "university": University,
                "organisation": Organization,
                "country": Country,
                "location": Location,
                "discipline": Discipline,
                "enzyme": Enzyme,
                "protein": Protein,
                "chemicalelement": ChemicalElement,
                "chemicalcompound": ChemicalCompound,
                "astronomicalobject": AstronomicalObject,
                "academicjournal": AcademicJournal,
                "event": Event,
                "theory": Theory,
                "award": Award,
                "misc": Miscellaneous,
            }
        else:
            raise ValueError(
                f"Task {task} not defined. Please choose one of the following: politics, music, literature, ai or"
                " natural_science"
            )
        self.elements = {}

        dataset_words, dataset_entities = load_conll_tsv(
            path=path_or_split,
            include_misc=True,
            ENTITY_TO_CLASS_MAPPING=self.ENTITY_TO_CLASS_MAPPING,
        )

        for id, (words, entities) in enumerate(zip(dataset_words, dataset_entities)):
            self.elements[id] = {
                "id": id,
                "doc_id": id,
                "text": " ".join(words),
                "entities": entities,
                "gold": entities,
            }


class CrossNERSampler(Sampler):
    """
    A data `Sampler` for the CrossNER dataset.

    Args:
        dataset_loader (`CrossNERDatasetLoader`):
            The dataset loader that contains the data information.
        task (`str`, optional):
            The task to sample. It must be one of the following: NER, VER, RE, EE.
            Defaults to `None`.
        split (`str`, optional):
            The path_or_split to sample. It must be one of the following: "train", "dev" or
            "test". Depending on the path_or_split the sampling strategy differs. Defaults to
            `"train"`.
        parallel_instances (`Union[int, Tuple[int, int]]`, optional):
            The number of sentences sampled in parallel. Options:

                * **`int`**: The amount of elements that will be sampled in parallel.
                * **`tuple`**: The range of elements that will be sampled in parallel.

            Defaults to 1.
        max_guidelines (`int`, optional):
            The number of guidelines to append to the example at the same time. If `-1`
            is given then all the guidelines are appended. Defaults to `-1`.
        guideline_dropout (`float`, optional):
            The probability to dropout a guideline definition for the given example. This
            is only applied on training. Defaults to `0.0`.
        seed (`float`, optional):
            The seed to sample the examples. Defaults to `0`.
        prompt_template (`str`, optional):
            The path to the prompt template. Defaults to `"templates/prompt.txt"`.
        ensure_positives_on_train (bool, optional):
            Whether to ensure that the guidelines of annotated examples are not removed.
            Defaults to `False`.
        dataset_name (str, optional):
            The name of the dataset. Defaults to `None`.
        scorer (`str`, optional):
           The scorer class import string. Defaults to `None`.
        sample_only_gold_guidelines (`bool`, optional):
            Whether to sample only guidelines of present annotations. Defaults to `False`.
    """

    def __init__(
        self,
        dataset_loader: CrossNERDatasetLoader,
        task: str = None,
        split: str = "train",
        parallel_instances: Union[int, Tuple[int, int]] = 1,
        max_guidelines: int = -1,
        guideline_dropout: float = 0.0,
        seed: float = 0,
        prompt_template: str = "templates/prompt.txt",
        ensure_positives_on_train: bool = False,
        dataset_name: str = None,
        scorer: str = None,
        sample_only_gold_guidelines: bool = False,
        **kwargs,
    ) -> None:
        assert task in [
            "CrossNER_POLITICS",
            "CrossNER_AI",
            "CrossNER_NATURAL_SCIENCE",
            "CrossNER_LITERATURE",
            "CrossNER_MUSIC",
        ], (
            "CrossNER only supports NER_POLITICS, NER_AI, NER_NATURAL_SCIENCE, NER_LITERATURE, NER_MUSIC. Task"
            f" {task} is not supported."
        )

        task_definitions, task_target = {
            "CrossNER_POLITICS": (ENTITY_DEFINITIONS_POLITICS, "entities"),
            "CrossNER_AI": (ENTITY_DEFINITIONS_AI, "entities"),
            "CrossNER_NATURAL_SCIENCE": (ENTITY_DEFINITIONS_NATURAL_SCIENCE, "entities"),
            "CrossNER_LITERATURE": (ENTITY_DEFINITIONS_LITERATURE, "entities"),
            "CrossNER_MUSIC": (ENTITY_DEFINITIONS_MUSIC, "entities"),
        }[task]

        super().__init__(
            dataset_loader=dataset_loader,
            task=task,
            split=split,
            parallel_instances=parallel_instances,
            max_guidelines=max_guidelines,
            guideline_dropout=guideline_dropout,
            seed=seed,
            prompt_template=prompt_template,
            ensure_positives_on_train=ensure_positives_on_train,
            sample_only_gold_guidelines=sample_only_gold_guidelines,
            dataset_name=dataset_name,
            scorer=scorer,
            task_definitions=task_definitions,
            task_target=task_target,
            definitions=GUIDELINES,
            examples=EXAMPLES,
            **kwargs,
        )
