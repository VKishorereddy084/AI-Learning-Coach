# AI Learning Coach application

This project aims to develop a personalized learning coach application using a fine-tuned Large Language Model (LLM). By leveraging advanced learning techniques, we enhance the model's ability to align with human educational goals and individual values, providing tailored educational support.

## What is the Project About?

We are focusing on enhancing a pre-trained LLM using reinforcement learning from human feedback (RLHF) and supervised learning. This approach aims to improve how the model understands and responds to educational queries, adapting it to the specific needs and preferences of individual learners.

Due to the time constraints, we managed to develop an application only with supervised techniques not with human values(RLHF). But, RLHF will be done in the future which will help to develop an learning coach application with human values and individual educational needs.  

### Key Features and Tasks

- 1: Dataset Creation: Develop a diverse dataset with educational content and feedback for training the model.

- 2: Model Refinement: Enhance the model's educational interaction capabilities.

- 3: Model Comparison: Evaluate improvements by comparing the refined model to the original.

- 4: Implementation: Use Langchain to deploy the refined model in a user-friendly learning coach application(Chatbot).

#### Files

  **dataset Folder**: This folder contains the datasets and related documents necessary for training and refining our LLM. 

  - ***dataset/Pythonlearn***: This document serves as the primary source for creating our educational dataset. It contains comprehensive material on Python programming, which we use to extract questions, answers, as dataset. This structured dataset is essential for ensuring that the model can accurately understand and respond to educational queries related to Python programming.

   **src/modules Folder**: This folder contains two python scripts that can preprocess the pdf data and generate Q&A pairs from the pdf data.
    
  - ***src/modules/Preprocessing.py***: A python script that preprocess the data by removing starting pages(Introduction and Index pages) of the pdf which we don't need and save the output of the preprocessed pdf.

  - ***src/modules/Q&A Generation.py***: This script takes a Preprocessed PDF file, generates question and answers from the pdf using advanced NLP techniques. It processes the text from the PDF, creates questions, refines this questions and then finds the best answers from the text. The final question-answer pairs are saved to a `CSV file`.

When you run the code, you will be asked to give the path of the PDF file. Please provide the correct path to ensure the script functions properly. 

*Chance of error*:
It is recommended to provide a 5-6 page PDF as input at a time. Processing a larger number of pages simultaneously can be very time-consuming and may heavily depend on the system's RAM capacity. Moreover, providing more pages can increase the risk of crashing the code. 

  **src/notebooks Folder**: This folder contains a series of Jupyter notebooks that are required for the developement of our AI learning coach application. Each notebook is designed for a specific part of the project workflow:

  - ***src/Converting_dataset.ipynb***: This script does two things. Pushing the raw dataset(Q&A pairs) by splitting it into train and test for evaluation to huggingface hub to specific repository for easy access and then converting it into a structured format that is suitable for  training machine learning models. Since we opted Llama2 for fine-tuning, the dataset is converted into Llama2 prompt template.

****Links****


  href="https://huggingface.co/datasets/Kishorereddy123/accurate_QA/"
  
  href= "https://huggingface.co/datasets/Kishorereddy123/transformed_QA"


- ***src/fine-tuning_dataset.ipynb***: This notebook explains the step-by-step  methods for enhancing a pre-trained LLM with our curated train dataset, aiming to improve its relevance and accuracy in educational contexts and also the evaluation of the fine-tuned model using different metrics with test dataset.

- ***src/RAG.ipynb***: In this notebook, we used `RAG` technique to evaluate the performance of the base model using `test` dataset. We used the same metrics that we used for fine-tuning.

- ***src/chatbot.ipynb***: This notebook demonstrates setting up a chatbot that utilizes the fine-tuned model using `Langchain` to interact and assist users with python programming.

#### Requirements and models that used.

- **Q&A Generation.py**: Make sure to install all the libraries required for the code to function. You can typically do this using pip, Python’s package installer.  Next, download the Zephyr model (`TheBloke/zephyr-7B-alpha-GGUF`) from Hugging Face. This model is essential for generating questions and answer from the input data.

- **Converting_dataset.ipynb**: This scripts takes csv file as an input. The libraries required for this are: `Pandas`, `HuggingFace`, `datasets`. You need to login to your huggingface to save the dataset by using following command

  ```
  from huggingface_hub import login
  login()


- **Fine-tuning_dataset.ipynb**: We have used Llama2 model for fine-tuning. To utilize the Llama2 model (meta-llama/Llama-2-7b-chat-hf), you must request access from Meta AI to ensure necessary permissions to use the model for your specific purposes.
  After fine-tuning the model, to store the new model in huggingface, we need merge the LoRA weights with base model. This process involves following steps because there is no straightforwardway to do this:
   - 1.  Load the base model in FP16 precision. This step is necessary to ensure compatibility with the updates.
   - 2.  Use the peft library to integrate the fine-tuned weights with the base model effectively.
   - 3.  Before merging the weights, clear the VRAM to prevent any memory issues. After clearing, restart the initial setup by rerunning the first three cells of the notebook.

  This way one can store the fine-tuned model in huggingface.


-**RAG.ipynb**:To run this code, you need to download the llama-2-7b-chat.Q4_K_M.gguf model from Hugging Face. This notebook takes pdf data as input. Provide the proper data path to load the pdf. 


###### Results

Results of fine-tuned model and base model.

<img src="./res/Fine-tuned Exact Match and F1 score.png"/>

<img src="./res/RAG Exact Match and F1 score.png"/>

