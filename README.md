# AIML Data Science Challenge

An implementation of AI and Machine Learning concepts using Python, developed and tested in GitHub Codespaces.

## Objective:
Your task is to build a predictive model to determine whether a customer will churn (leave the bank). Using the Bank Customer Churn Dataset from Kaggle, you will load, clean, analyze the data, and develop a machine learning model to predict customer churn.

---

## Getting Started
1. After accepting the assignment, you will be redirected to your own copy of the repository
2. The repo is forked, and you only need to commit the changes that you make in the Python files. 
3. **Use GitHub Codespaces**:
   - Click on the green **Code** button in your forked repository.
   - Select **Codespaces** and choose "Create codespace on main" to open your development environment.

4. The repository includes a pre-configured `devcontainer.json` file, which automatically sets up the Python environment in Codespaces.
5. Once the Codespace is ready and the environment is set up, review the code in the Python files to understand the structure.
6. A `requirement.txt` file is added in the repo, which pre-installs the required libraries for the challenge (do not modify; if modified, rerun `pip` to install). 
7. `.devcontainer`, `tests`, `.gitignore` and `.github` folders are protected and they **SHOULD NOT** be altered. 
8. Complete the missing functions, indicated by **TODO** comments within the Python files.
9. Test your implementation by running the appropriate scripts in the `/src` folder inside GitHub Codespaces. 
10. Once the Codespace changes are committed, your project will be automatically submitted for review. 

---

## Steps to Follow
1. Accept the assignment to obtain your forked repository and set up your environment using **GitHub Codespaces**.

2. ### task 1: Data Exploration(8 marks)

**`data_exploration.py`**: implement logic to load and analyze the dataset `bank_churn.csv`. Check for missing values, generate summary statistics.

3. ### task 2: Feature engineering(12 marks)

**`feature_engineering.py`**: Implement steps to handle missing values, encode categorical features, and create useful columns.

4. ### task 3: Model Training(20 marks)

**`model_training.py`**: define features, split the data, and train your machine learning model.


5. Run the codes inside **GitHub Codespaces terminal** and executing the command `pytest` to verify your implementation..

6. Commit the changes using the **COMMIT** button (green) available in the codespace.

---

## Tips
- Handle different data types (strings, integers, floats) correctly during data processing.
- Use pandas for data manipulation and scikit-learn for building machine learning models.
- Implement data quality checks after each processing step to ensure data integrity.

---

## Submission Guidelines
After completing the challenge, commit the changes using the commit button available in the codespace. Make sure the changes have been successfully committed.

---

## Evaluation Criteria
- Correctness of data loading and cleaning steps.
- Quality of data exploration and feature engineering.
- Successful model training and evaluation.
- Proper repository structure and code organization.
- Successful execution of the project within **GitHub Codespaces**.

Good luck, and happy coding!
