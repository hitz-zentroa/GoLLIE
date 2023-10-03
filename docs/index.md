<h1><img src="../assets/GoLLIE.png" width="25"> GoLLIE: Guideline-following Large Language Model for Information Extraction</h1>

**Authors:** [Oscar Sainz](https://osainz59.github.io/), [Iker García-Ferrero](https://ikergarcia1996.github.io/Iker-Garcia-Ferrero/), [Rodrigo Agerri](https://ragerri.github.io/), [Oier Lopez de Lacalle](https://oierldl.github.io/), [German Rigau](https://adimen.si.ehu.es/~rigau/) and [Eneko Agirre](https://eagirre.github.io/)

<p align="justify">
<b>TL;DR</b> We present GoLLIE, a Large Language Model trained to follow annotation guidelines. GoLLIE outperforms previous approaches on zero-shot Information Extraction and allows the user to perform inferences with annotation schemas defined on the fly. Different from previous approaches, GoLLIE is able to follow detailed definitions and does not only rely on the knowledge already encoded in the LLM. Code and models are publicly available.
</p>

<p align="justify">
Information Extraction (IE) is a challenging task, often requiring to follow strict and highly detailed guidelines in order to perform the task correctly. Traditionally, large amounts of annotations were used to train models to mimic expert annotators. This approach, however, is very expensive and rarely applicable in low-resource domains. Since several years ago, data-augmentation techniques like Distant Supervision [<a href="#references">1</a>] were developed to tackle data-scarcity. More recently, with the recent advances in NLP, zero and few-shot methods (cite something) were created exploiting the internal knowledge of LLMs.
</p>

<p align="justify">
Despite the recent advances, the models still struggle with guidelines details. The main reason why that occurs is because models have a strong representation of what the labels mean, and, when more details are needed, the models just ignore them. For instance, this is an example of ChatGPT annotating person entities:
</p>


<table border="0">
 <tr>
   <td><img src="https://www.svgrepo.com/show/532363/user-alt-1.svg" width="80em"></td>
   <td>Can you annotate person entities if I give you a sentence? The "person" entity is defined as follows: "Each distinct person, or set of people, mentioned in a document refers to an entity of type Person. For example, people may be specified by name ("John Smith"), occupation ("the butcher"), family relation ("mum"), pronoun ("they"), etc., or by some combination of these."</td>
 </tr>
</table>

<table border="0">
 <tr>
   <td>Certainly, I can help you annotate person entities in a sentence based on the definition you provided. Please provide the sentence you'd like me to annotate for person entities, and I'll do my best to identify and annotate them for you.</td>
   <td><img src="https://www.svgrepo.com/show/306500/openai.svg" width="50px"></td>
 </tr>
</table>

<table border="0">
 <tr>
   <td><img src="https://www.svgrepo.com/show/532363/user-alt-1.svg" width="25em"></td>
   <td>Sentence: "I go from Lasarte to Donosti to work at the University of the Basque Country every day."</td>
 </tr>
</table>

<table border="0">
 <tr>
   <td>In the sentence you provided, there are <b>no explicit mentions of distinct persons or people</b> by name, occupation, family relation, <b>pronoun</b>, or any combination of these. Therefore, there are no person entities to annotate in this sentence. If you have any other sentences or text where you'd like person entities annotated, please feel free to provide them, and I'll assist you accordingly.</td>
   <td><img src="https://www.svgrepo.com/show/306500/openai.svg" width="90px"></td>
 </tr>
</table>
<p align="center">You can find the original chat <a href="https://chat.openai.com/share/e44e9b0e-3f6b-49a0-b84d-48386e0b5118">here</a></p>

Although the given sentence is quite easy to annotate, the example above shows that even when prompted with the instructions to annotate <b>pronouns</b> as person entities, ChatGPT ignores the instruction and forgets to annotate "I" as person. This imposes a problem when detailed instructions are needed to perform the task, something common on the field of IE where the task guidelines have lots of details and exceptions.

To address this issues, we present <img src="../assets/GoLLIE.png" width="20"> GoLLIE, a Large Language Model trained to follow annotation guidelines.



## Schema definition and inference

## Results

## Conclusions

## References

1. Mike Mintz, Steven Bills, Rion Snow, and Daniel Jurafsky. 2009. Distant supervision for relation extraction without labeled data. In Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP, pages 1003–1011, Suntec, Singapore. Association for Computational Linguistics.
