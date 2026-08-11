import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    Border = "-"*100

    # Step 1: Get Data
    print(Border)
    print("Step 1: Get Data")
    print(Border)

    df = pd.read_csv("WinePredictor.csv")

    print("Dataset loaded successfully")
    print("Shape of Dataset: ",df.shape)
    print(df.head())

    print(Border)
    
    # Step 2: Clean, prepare and manipulate data
    print(Border)
    print("Step 2: Clean, prepare and manipulate data")
    print(Border)

    # Check for missing values
    print("\nMissing values")
    print(df.isnull().sum())

    # Saperate independant variables and dependent variables
    X = df.drop("Class", axis = 1)
    Y = df["Class"]

    print("\nFeatures")
    print(X.columns)

    print("\nTarget")
    print("Class")

    print(Border)

    # Step 3: Train Data
    print(Border)
    print("Step 3: Train Data")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Training records: ",X_train.shape[0])
    print("Testing records: ",X_train.shape[0])

    # Create machine learning model
    model = DecisionTreeClassifier(random_state=42)

    # Train the model
    model.fit(X_train,Y_train)
    print("Model trained successfully")

    print(Border)

    # Step 4: Test Data
    print(Border)
    print("Step 4: Test Data")
    print(Border)

    Y_pred = model.predict(X_test)

    print("Acutal values: ")
    print(Y_test.values)

    print(Border)

    # Step 5: Calculate Accuracy
    print(Border)
    print("Step 5: Calculate Accuracy")
    print(Border)

    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy percentage: ",accuracy * 100,"%")

    print(Border)
    

if __name__=="__main__":
    main()