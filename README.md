## Code for the ImageCoDe Challenge: Leveraging Chain-Of-Thought Prompting Techniques

### Instructions

#### Clip Evaluation

Simply change the hardcoded filepaths to run the code.

#### MMICL prompting

This runs the model from a pre-trained checkpoint from HuggingFace. In the python notebook, there is code taken from the open-source MMICL github that is required in order to make it run correctly. These parts are clearly indicated. They seem to be previous versions of the open-source InstructBLIP models that are now in the transformers library.

#### Gemini prompting

This is just an API call using the Google Cloud VertexAI API. To use it, you can replace the project name with your own after authenticating.

#### Data

The image data can be found on Benno Krojer's github: https://github.com/McGill-NLP/imagecode/tree/main

#### Results Evaluation

Run accuracy_test.py on the code, the results should a JSON with formatted as such:

```
[
  {
    "img1":
    "img2":
    "caption":
    "label":
    "response":
  },
]
```
