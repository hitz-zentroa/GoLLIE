---
name: "\U0001F41B Bug report and Issues"
about: Submit a bug report to help us improve GoLLIE
title: "[BUG] Bug or issue report"
labels: ''
assignees: ''

---

**Describe the task**
1. Model: Which GoLLIE model are you attemping to run?
2. Task: Which task are you attemping to run (training, evaluation, generate the dataset,...)?

**Describe the bug**
A clear and concise description of what the bug is. You can add the error traceback or screenshots here. 

**To Reproduce**
Steps to reproduce the behavior:
1. Load model X
```Python
model, tokenizer = load_model(
    inference=True,
    model_weights_name_or_path="HiTZ/GoLLIE-7B",
    quantization=None,
    use_lora=False,
    force_auto_device_map=True,
    use_flash_attention=True,
    torch_dtype="bfloat16"
)
```
2. Run X function
```Python
model_ouput = model.generate(
    **model_input.to(model.device),
    max_new_tokens=128,
    do_sample=False,
    min_new_tokens=0,
    num_beams=1,
    num_return_sequences=1,
)
```
3. Any other step required to reproduce the behaviour 

**Expected behavior**
A clear and concise description of what you expected to happen.

**System Info**
1. GPU: (i.e Nvidia A100)
2. Pytorch version:
3. Transformers version:
4. Model configuration: Are you using 4 / 8 bits quantization? Are you using mGPU? etc..
5. Any other relevant information:


**Additional context**
Add any other context about the problem here.
