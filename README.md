# Loan_Elligibility_prediction

This repository houses a machine learning project focused on predicting loan eligibility for individuals. Utilizing a decision tree classifier, the project analyzes a dataset of loan applicants with diverse features such as gender, income, credit history, etc. Additionally, it features a user-friendly web application, enabling users to input their information and receive a prediction regarding their loan eligibility.

## Files and Folders

1. **`loan_elligibility.ipynb`**: 
    - Jupyter notebook containing the code for data analysis, model construction, and evaluation.

2. **`loan_train.csv`**: 
    - CSV file comprising the training data for the model, encompassing 614 rows and 13 columns.

3. **`Loan_predicted.pkl`**: 
    - Pickle file storing the trained model for seamless prediction.

4. **`Loan_Tree.png`**: 
    - Image file visualizing the decision tree model.

5. **`app.py`**: 
    - Python file containing code for the web application implemented using the Flask framework.

6. **`templates`**: 
    - Folder housing HTML files crucial for the web application's functionality.

## Getting Started

To explore the project and interact with the loan eligibility prediction model:

1. Review the Jupyter notebook (`loan_elligibility.ipynb`) for in-depth insights into data analysis, model development, and evaluation.

2. Access the training data in the `loan_train.csv` file to understand the dataset used for model training.

3. Utilize the trained model stored in `Loan_predicted.pkl` for making predictions.

4. Visualize the decision tree model through the image file `Loan_Tree.png`.

5. Experience the loan eligibility prediction in real-time by running the web application. Execute `app.py` and navigate to the provided local address.

## Dependencies

Ensure you have the necessary dependencies installed by using the following command:

```bash
pip install -r requirements.txt
```

## Usage

Follow these steps to deploy the web application locally:

```bash
python app.py
```

Visit `http://localhost:5000` in your web browser to interact with the loan eligibility prediction tool.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.
Alternatively, you can access the web application online at http://sairaju.pythonanywhere.com/.
