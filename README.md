<h1 align="center">CoLLIE</h1>
<p align="center">
    <br>
    <img src="assets/CoLLIE_project_icon_rounded.png" style="height: 150px;">
    <br>
    <h2 align="center"><b>C</b>ode based <b>L</b>arge <b>L</b>anguage-model for <b>I</b>nformation-<b>E</b>xtraction</h2>
    <br>
</p>
<p align="center">
    <a href="https://twitter.com/intent/tweet?text=Wow+this+new+model+is+amazing:&url=https%3A%2F%2Fgithub.com%2Fosainz59%2FCoLLIE"><img alt="Twitter" src="https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fosainz59%2FCoLLIE"></a>
    <a href="https://github.com/osainz59/CoLLIE/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/osainz59/CoLLIE"></a>
    <a href="https://github.com/osainz59/CoLLIE/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/osainz59/CoLLIE?color=yellow"></a>
    <a href="https://github.com/osainz59/CoLLIE/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/osainz59/CoLLIE"></a>
    <a href="https://huggingface.co/models"><img alt="Pretrained Models" src="https://img.shields.io/badge/Pretrained Models-Available-green"></a>
    <br>
    <a href="http://www.hitz.eus/"><img src="https://img.shields.io/badge/HiTZ-Basque%20Center%20for%20Language%20Technology-blueviolet"></a>
    <a href="http://www.ixa.eus/?language=en"><img src="https://img.shields.io/badge/IXA-%20NLP%20Group-ff3333"></a>
    <br>
     <br>
</p>

<p align="center">
<br>
:warning: Work in Progress :warning:
</p>

## Introduction

CoLLIE is a LLM specialized to perform personalized Information-Extraction (IE) on demand, based on simple specifications given in the input. Developing a model of such characteristics could be a breakthrough that changes the complete paradigm of actual IE. Unfortunately, models capable of achieving such capabilities have restricted access like Codex, InstructGPT or GPT-4. CoLLIE is an open-source attempt to achieve personalized IE. Personalized IE allows to extract information for a given schema (dynamically) without annotating further examples, i.e. zero-shot, this could be very convenient for annotation assistants for example.

### Example (using Code format)
Paper: [Code4Struct: Code Generation for Few-Shot Structured Prediction from Natural Language](https://arxiv.org/abs/2210.12810)

Prompt
```python
@dataclass
class EnergyAndInfrastructureEvent:
    """This class is used to instantiate events that involve Chinese energy and infrastructure projects."""
    meeting_attendees: Union[List[str], None] # Persons or organizations that attended the meeting.
    meeting_location: Union[List[str], None] # Location where the meeting happened.
    meeting_topic: Union[List[str], None] # Topic discussed on the meeting
    project_location: Union[List[str], None] # Location of the project
    project_name: Union[List[str], None] # Name of the project
    
# This is the sentence to analyze
sentence = "The Chinese and Rongovian delegations met at the sidelines of the Berlin Development Futures conference to discuss Rongovia's proposed Pangean Reunification Facility."
```
Output (LLaMA 65B zero-shot)
```python
# The following list contains the events instances that happens in the sentence defined above
—————————
events = [
    EnergyAndInfrastructureEvent(
        meeting_attendees=["Chinese", "Rongovian"],
        meeting_location=["Berlin"],
        meeting_topic=["Pangean Reunification Facility"],
        project_location=["Rongovia"],
        project_name=["Pangean Reunification Facility"]
    ),
]
```
