<h1><img src="https://github.com/hitz-zentroa/GoLLIE/blob/main/assets/GoLLIE.png?raw=true" width="25"> GoLLIE: Guideline-following Large Language Model for Information Extraction</h1>

**Authors:** [Oscar Sainz](https://osainz59.github.io/), [Iker García-Ferrero](https://ikergarcia1996.github.io/Iker-Garcia-Ferrero/), [Rodrigo Agerri](https://ragerri.github.io/), [Oier Lopez de Lacalle](https://oierldl.github.io/), [German Rigau](https://adimen.si.ehu.es/~rigau/) and [Eneko Agirre](https://eagirre.github.io/)

<p align="justify">
<b>TL;DR</b> We present GoLLIE, a Large Language Model trained to follow annotation guidelines. GoLLIE outperforms previous approaches on zero-shot Information Extraction and allows the user to perform inferences with annotation schemas defined on the fly. Different from previous approaches, GoLLIE is able to follow detailed definitions and does not only rely on the knowledge already encoded in the LLM. 
</p>

<p align="justify">
Information Extraction (IE) is a challenging task, often requiring to follow strict and highly detailed guidelines in order to perform the task correctly. Traditionally, large amounts of annotations were used to train models to mimic expert annotators. This approach, however, is very expensive and rarely applicable in low-resource domains. Since several years ago, data-augmentation techniques like Distant Supervision [<a href="#references">1</a>] were developed to tackle data-scarcity. More recently, with the recent advances in NLP, zero and few-shot methods [<a href="#references">2</a>] were created exploiting the internal knowledge of LLMs.
</p>

<p align="justify">
Despite the recent advances, the models still struggle to follow annotation guidelines details. We hypothesize that the main reason why that occurs is because models have a strong preconception of the labels meaning, and, when more details are needed, the models just ignore them. For instance, this is an example of ChatGPT annotating person entities:
</p>

<table border="0">
 <tr>
   <td><img src="assets/user.svg" width="80em"></td>
   <td>Can you annotate person entities if I give you a sentence? The "person" entity is defined as follows: "Each distinct person, or set of people, mentioned in a document refers to an entity of type Person. For example, people may be specified by name ("John Smith"), occupation ("the butcher"), family relation ("mum"), pronoun ("they"), etc., or by some combination of these."</td>
 </tr>
</table>

<table border="0">
 <tr>
   <td>Certainly, I can help you annotate person entities in a sentence based on the definition you provided. Please provide the sentence you'd like me to annotate for person entities, and I'll do my best to identify and annotate them for you.</td>
   <td><img src="assets/openai.svg" width="50px"></td>
 </tr>
</table>

<table border="0">
 <tr>
   <td><img src="assets/user.svg" width="25em"></td>
   <td>Sentence: "I go from Lasarte to Donosti to work at the University of the Basque Country every day."</td>
 </tr>
</table>

<table border="0">
 <tr>
   <td>In the sentence you provided, there are <b>no explicit mentions of distinct persons or people</b> by name, occupation, family relation, <b>pronoun</b>, or any combination of these. Therefore, there are no person entities to annotate in this sentence. If you have any other sentences or text where you'd like person entities annotated, please feel free to provide them, and I'll assist you accordingly.</td>
   <td><img src="assets/openai.svg" width="90px"></td>
 </tr>
</table>
<p align="center">You can find the original chat <a href="https://chat.openai.com/share/e44e9b0e-3f6b-49a0-b84d-48386e0b5118">here</a></p>

<p align="justify">Although the given sentence is quite easy to annotate, the example above shows that, even when prompted with the instructions to annotate <b>pronouns</b> as person entities, ChatGPT ignores the instruction and forgets to annotate "I" as person. This imposes a problem when detailed instructions are needed to perform the task, something common on the field of IE where the task guidelines have lots of details and exceptions.</p>

<p align="justify">To address these issues, we present <img src="https://github.com/hitz-zentroa/GoLLIE/blob/main/assets/GoLLIE.png?raw=true" width="20"> GoLLIE, a Large Language Model trained to follow annotation guidelines. GoLLIE outperforms previous approaches on zero-shot Information Extraction and allows the user to perform inferences with annotation schemas defined on the fly. Different from previous approaches, GoLLIE is able to follow detailed definitions and does not only rely on the knowledge already encoded in the LLM. GoLLIE is based on Code-Llama. Our code and models are publicly available. In the following sections we will introduce in more detail how the model works, and show some interesting insights. We recommend the reader to read the <a href="https://arxiv.org/abs/2310.03668">paper</a> for more details.</p>


## Schema definition and inference

<p align="justify">Our model allows the user to define custom schemas using Python code! Python classes allows to write human-readable code that is also familiar with current LLMs. Imagine that we want to extract information about space missions, the following Python code will define the guidelines for two <b>new types</b> of entities: <code>Launcher</code> and <code>Mission</code>.</p>

<p align="center">
<img src="https://github.com/hitz-zentroa/GoLLIE/blob/main/assets/snippets/space_guidelines.png?raw=true">
</p>

<p align="justify">Here, the labels are represented as Python classes, and the guidelines or instructions are introduced as docstrings. For some tasks, we would also like to have some additional information about our mentions, like, for example, the <code>space_company</code> or the <code>crew</code> of the launcher. We can add that additional information as attributes of the task, with their corresponding guideline as comments.</p>

<p align="justify">Once we defined our new labels, it is time to provide the model with a text to annotate. We can do that by simply creating a Python variable with the name <code>text</code> and assign our desired text to it. We can also add a comment to help the model understand what we want. In addition, we use  <a href="https://black.readthedocs.io/en/stable/">Black</a> code formatter to standarize the input.</p>

<p align="center">
<img src="https://github.com/hitz-zentroa/GoLLIE/blob/main/assets/snippets/space_text.png?raw=true">
</p>
After this, we just need to run the model to generate our annotations!

<p align="center">
<img src="https://github.com/hitz-zentroa/GoLLIE/blob/main/assets/snippets/space_result.png?raw=true">
</p>
<p align="justify">As you can see, the generated output can be directly evaluated as it is Python working code. This allows the user to directly parse and interpret the output. The model's output also satisfy the type constraints defined in the guidelines, for instance, we defined every attribute as strings, except for the crew, which is a list. Another constraints can also be applied, such as <code>Optional</code> attributes or more detailed types like <code>Name</code>, <code>Value</code> or <code>String</code> types.</p>

Please, have a look to our <a href="https://github.com/hitz-zentroa/GoLLIE/tree/main/notebooks">Notebooks</a> to get started with the model.

## Evaluation

<p align="justify">We have evaluated GoLLIE on a set of diverse tasks across different datasets. Our primary goal is the zero-shot evaluation, although we also report the results obtained on the supervised datasets in the <a href="https://arxiv.org/abs/2310.03668">paper</a>. The following figure shows a great summary of what our model is capable of:</p> 

![Zero-Shot NER Results.](https://github.com/hitz-zentroa/GoLLIE/raw/main/assets/zero_shot_results.png)

<p align="justify">We compared our model with GPT-3.5[<a href="#references">2</a>] and Instruct-UIE[<a href="#references">3</a>] (SOTA) on MIT Movie[<a href="#references">4</a>], MIT Restaurant[<a href="#references">4</a>] and CrossNER[<a href="#references">5</a>] Named Entity Recognition (NER)datasets. Our model outperforms previous approaches on almost all the datasets, and performs similar to the SOTA on the rest. In addition to those results showed in the figure, we also evaluated the model on Event Extraction (EE) and Event Argument Extraction (EAE) datasets. Please, check the <a href="https://arxiv.org/abs/2310.03668">paper</a> or run the <a href="https://huggingface.co/collections/HiTZ/gollie-651bf19ee315e8a224aacc4f">models</a> yourself for more detailed results.</p>

## Conclusions

We present the first model that effectively leverages annotation guidelines to enhance zero-shot Information Extraction. Our model, available in 7B, 13B, and 34B variants, establishes a new state-of-the-art, surpassing previous approaches.

In our initial iteration, we focused on demonstrating that instructing LLMs to adhere to guidelines is both possible and advantageous. Our next step is to train models on many more tasks and datasets to expand the model's capabilities. Ultimately, our goal is to develop a model that can tackle any information extraction task as proficiently as a human without the necessity of manually annotating data.

<table border="0" align="center">
 <tr>
   <td><a href="https://arxiv.org/abs/2310.03668"><img src="https://img.shields.io/badge/Paper-20B2AA?style=for-the-badge"></a></td>
   <td><a href="https://github.com/hitz-zentroa/GoLLIE"><img src="https://img.shields.io/badge/Code-20B2AA?style=for-the-badge"></a></td>
   <td><a href="https://huggingface.co/collections/HiTZ/gollie-651bf19ee315e8a224aacc4f"><img src="https://img.shields.io/badge/Models-20B2AA?style=for-the-badge"></a></td>
   <td><a href="https://github.com/hitz-zentroa/GoLLIE/tree/main/notebooks"><img src="https://img.shields.io/badge/Example Notebooks-20B2AA?style=for-the-badge"></a></td>
 </tr>
</table>


## References

1. Mike Mintz, Steven Bills, Rion Snow, and Daniel Jurafsky. 2009. Distant supervision for relation extraction without labeled data. In Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP, pages 1003–1011, Suntec, Singapore. Association for Computational Linguistics.
2. Ashok, D., & Lipton, Z. C. 2023. PromptNER: Prompting For Named Entity Recognition. arXiv preprint: 2305.15444.
3. Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, and Chunsai Du. 2023. Instructuie: Multi-task instruction tuning for unified information extraction. arXiv preprint: 2304.08085
4. Jingjing Liu, Panupong Pasupat, Scott Cyphers, and James R. Glas. 2013. Asgard: A portable architecture for multilingual dialogue systems. In 2013 IEEE International Conference on Acoustics, Speech and Signal Processing (pp. 8386-8390). IEEE.
5. Zihan Liu, Yan Xu, Tiezheng Yu, Wenliang Dai, Ziwei Ji, Samuel Cahyawijaya, Andrea Madotto, and Pascale Fung. 2021. Crossner: Evaluating cross-domain named entity recognition. In Thirty-Fifth AAAI Conference on Artificial Intelligence.
