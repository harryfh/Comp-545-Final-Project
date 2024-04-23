## Code for the ImageCoDe Challenge: Leveraging Chain-Of-Thought Prompting Techniques

### Instructions

#### Clip Evaluation

Simply change the hardcoded filepaths to run the code.

#### Gemini prompting

This is just an API call using the Google Cloud VertexAI API. To use it, you can replace the project name with your own after authenticating.

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
