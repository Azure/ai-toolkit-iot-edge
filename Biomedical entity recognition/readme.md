# IoT Scenario - Biomedical Entity Extraction

Biomedical named entity recognition is a critical step for complex biomedical NLP tasks such as:
Extraction of diseases, symptoms from electronic medical or health records.
Drug discovery
Understanding the interactions between different entity types such as drug-drug interaction, drug-disease relationship and gene-protein relationship.
Our use case scenario focuses on how a large amount of unstructured unlabeled data corpus such as PubMed article abstracts can be analyzed to train a domain-specific word embedding model. Then the output embeddings are considered as automatically generated features to train a neural entity extraction model using Keras with TensorFlow deep learning framework as backend and a small amoht of labeled data. 

We have also included a Docker container with the final model. This container can be deployed to an IoT device via Azure IoT Hub.

## Link to the Microsoft DOCS site

The detailed documentation for this real world scenario includes the step-by-step walkthrough:

[https://docs.microsoft.com/en-us/azure/machine-learning/preview/scenario-tdsp-biomedical-recognition](https://docs.microsoft.com/en-us/azure/machine-learning/preview/scenario-tdsp-biomedical-recognition)

## Link to the Azure Machine Learning Gallery GitHub repository

The public GitHub repository for this real world scenario contains all the code samples:

[https://github.com/Azure/MachineLearningSamples-BiomedicalEntityExtraction](https://github.com/Azure/MachineLearningSamples-BiomedicalEntityExtraction)

