# AI Learning Coach application

This project aims to develop a personalized learning coach application using a fine-tuned Large Language Model (LLM). By leveraging advanced learning techniques, we enhance the model's ability to align with human educational goals and individual values, providing tailored educational support.

## What is the Project About?

We are focusing on enhancing a pre-trained LLM using reinforcement learning from human feedback (RLHF) and supervised learning. This approach aims to improve how the model understands and responds to educational queries, adapting it to the specific needs and preferences of individual learners.

Due to the time constraints, we managed to develop an application only with supervised techniques not with human values(RLHF). But, RLHF will be done in the future which will help to develop an learning coach application with human values and individual educational needs.  

### Key Features and Tasks

1: Dataset Creation: Develop a diverse dataset with educational content and feedback for training the model.

2: Model Refinement: Enhance the model's educational interaction capabilities.

3: Model Comparison: Evaluate improvements by comparing the refined model to the original.

4: Implementation: Use Langchain to deploy the refined model in a user-friendly learning coach application(Chatbot).

#### Files

**Dataset Folder**: This folder contains the datasets and related documents necessary for training and refining our AI Learning Coach application. It is crucial for developing the model's ability to provide personalized educational experiences.

**Dataset/Pythonlearn**: This document serves as the primary source for creating our educational dataset. It contains comprehensive material on Python programming, which we use to extract questions, answers, as dataset. This structured dataset is essential for ensuring that the model can accurately understand and respond to educational queries related to Python programming.

**src/modules/Q&A Generation.py**: This script takes a PDF file, generates question and answers from the pdf using advanced NLP techniques. It processes the text from the PDF, creates questions, refines this questions and then finds the best answers from the text. The final question-answer pairs are saved to a CSV file.

*Chance of error*: 

**src/Converting-dataset.ipynb** 



