# **Clash Royale Machine Learning Project**

![Clash Royale Match Prediction](./images/Clash-royale-match-prediction.jpg)

Welcome to the **Clash Royale Match Prediction** project! This repository provides tools to fetch, clean, and analyze battle data from the Clash Royale API, with the option to develop predictive models for match outcomes. It's a perfect starting point for Clash Royale enthusiasts looking to delve into data science or machine learning.

🌐 **Check out our webpage for more details and updates:**  
[https://grandediw.github.io/Clash-Royale-Project/](https://grandediw.github.io/Clash-Royale-Project/)


## Table of Contents
1. [Introduction](#introduction)  
2. [Methods](#methods)  
   - [Historical Dataset](#historical-dataset)  
   - [API](#api)  
3. [Data Representation and Preprocessing](#data-representation-and-preprocessing)  
   - [Deck Representation](#deck-representation-using-one-hot-encoding)  
   - [Outcome Encoding](#outcome-encoding-and-dataframe-creation)  
   - [Data Preprocessing](#data-preprocessing)  
4. [Modeling and Evaluation](#modeling-and-evaluation)  
   - [Models Tested](#models-tested)  
   - [Performance Metrics](#performance-metrics)  
5. [Conclusion](#conclusion)  
6. [Discussion](#discussion)  
7. [How to Run the Code](#how-to-run-the-code)  
8. [Try the Interface](#try-the-interface)

---

## Introduction
This project aims to create a predictive system for **Clash Royale**, a strategy-based card game with 181 unique cards. Players build eight-card decks, and the synergy, counter-abilities, and balance of the deck significantly impact match outcomes.

The system predicts the probability of winning based on two opponents' decks using historical match data and machine learning models. It provides insights into how card combinations influence match results.

---

## Methods

### Historical Dataset
The dataset consists of **2.5 million matches** sourced from Hugging Face. It includes:
- **Deck Composition**: The cards in each player's eight-card deck.
- **Match Outcome**: Indicates the winner.

Each card was mapped to a unique identifier for encoding purposes, and key features were extracted for modeling.

### API
The project also integrates the **Clash Royale API** to fetch real-time player match data. For each player tag, the API provides:
- Deck composition
- Match outcomes for the last 30 matches

This combination of historical and real-time data ensures accurate and relevant predictions.

---

## Data Representation and Preprocessing

### Deck Representation Using One-Hot Encoding
Each of the 181 cards is represented as a binary vector. A deck is encoded as a single vector of 181 elements, where positions corresponding to the deck's cards are set to `1`, and others are set to `0`. This approach avoids biases and maintains interpretability.

### Outcome Encoding and Dataframe Creation
Match outcomes were encoded as:
- `1` for Player 1 wins
- `0` for Player 2 wins

The dataset was structured into a dataframe where each row corresponds to a match with:
- Encoded Player 1 deck
- Encoded Player 2 deck
- Match outcome

### Data Preprocessing
Key preprocessing steps included:
1. Mapping each card to its one-hot encoded vector.
2. Structuring the dataset such that each row represents a match.
3. Randomizing player positions to prevent biases.

---

## Modeling and Evaluation

### Models Tested
1. **Neural Network (TensorFlow)**  
   - Input Layer: 128 neurons with ReLU activation  
   - Hidden Layer: 64 neurons with ReLU activation  
   - Output Layer: 1 neuron with tanh activation  

   Trained using Adam optimizer and Mean Squared Error (MSE) loss over 20 epochs.

2. **XGBoost Classifier**  
   - Gradient boosting algorithm configured for classification tasks.  
   - Evaluated using the log-loss metric.  

### Performance Metrics
Models were evaluated based on:
- **Accuracy**: Correctly predicted outcomes.
- **Precision and Recall**: Ability to identify wins and losses.
- **Validation Loss**: Monitors overfitting during training.

---

## Conclusion

### Model Performance
- **XGBoost** achieved an accuracy of **84.3%** and a macro F1-score of **83%**, outperforming the neural network.
- The neural network achieved only **56.62% accuracy**, highlighting challenges in capturing the complexity of card interactions.

### Why XGBoost Was Chosen
1. **Higher Accuracy**  
2. **Efficiency**: Faster training and tuning.  
3. **Robustness**: Better handling of high-dimensional data.

---

## Discussion
The predictive system successfully estimates match outcomes for Clash Royale using a combination of historical and real-time data.

### Limitations
1. Dependence on API availability for live data.  
2. Reduced accuracy for unconventional decks.  

### Future Improvements
1. Explore deep learning techniques like attention mechanisms for better card interaction modeling.  
2. Enhance predictions for unconventional deck strategies.

---

## How to Run the Code
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/clash-royale-predictor.git
   cd clash-royale-predictor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Deploy the system using the provided code.

4. Access the system via the provided URL to input player tags or decks and view predictions.

---

## Try the Interface
Test the interactive Clash Royale prediction system directly on Hugging Face Spaces:  
[**Try the Interface Here!**](https://huggingface.co/spaces/Grandediw/Clash_Royale_Prediction)

---

## References
1. [Clash Royale Dataset on Kaggle](https://www.kaggle.com/datasets/s1m0n38/clash-royale-games)  
2. [Clash Royale API Documentation](https://developer.clashroyale.com/#/)

---
