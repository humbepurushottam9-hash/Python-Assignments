import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# Step 1: Get Data
def LoadData(FileName):
    df = pd.read_csv(FileName)

    # Remove unnecessary index column
    if "Unnamed: 0" in df.columns:
        df = df.drop("Unnamed: 0", axis=1)

    return df


# Step 2: Clean, Prepare and Manipulate Data
def PrepareData(df):
    WeatherEncoder = LabelEncoder()
    TemperatureEncoder = LabelEncoder()
    PlayEncoder = LabelEncoder()

    df["Wether"] = WeatherEncoder.fit_transform(df["Wether"])
    df["Temperature"] = TemperatureEncoder.fit_transform(df["Temperature"])
    df["Play"] = PlayEncoder.fit_transform(df["Play"])

    return df, WeatherEncoder, TemperatureEncoder, PlayEncoder


# Step 3: Train Data
def TrainData(df):
    X = df[["Wether", "Temperature"]]
    Y = df["Play"]

    Model = KNeighborsClassifier(n_neighbors=3)

    # Train using whole dataset
    Model.fit(X, Y)

    return Model


# Step 4: Test Data
def TestData(Model, WeatherEncoder, TemperatureEncoder, PlayEncoder):

    print("\n-------------------------------")
    print("Enter Weather Details")
    print("-------------------------------")

    Weather = input("Enter Weather (Sunny/Overcast/Rainy): ")
    Temperature = input("Enter Temperature (Hot/Mild/Cool): ")

    # Convert string into numeric value
    WeatherValue = WeatherEncoder.transform([Weather])[0]
    TemperatureValue = TemperatureEncoder.transform([Temperature])[0]

    # Prediction
    Result = Model.predict([[WeatherValue, TemperatureValue]])

    # Convert numeric result back to Yes/No
    ResultLabel = PlayEncoder.inverse_transform(Result)

    print("\nPrediction:", ResultLabel[0])


# Step 5: Calculate Accuracy
def CheckAccuracy(df):

    X = df[["Wether", "Temperature"]]
    Y = df["Play"]

    # Divide dataset into two equal parts
    TrainingSize = len(df) // 2

    XTrain = X.iloc[:TrainingSize]
    XTest = X.iloc[TrainingSize:]

    YTrain = Y.iloc[:TrainingSize]
    YTest = Y.iloc[TrainingSize:]

    print("\n-------------------------------")
    print("Accuracy for Different K Values")
    print("-------------------------------")

    for K in range(1, 11):

        Model = KNeighborsClassifier(n_neighbors=K)

        Model.fit(XTrain, YTrain)

        YPrediction = Model.predict(XTest)

        Accuracy = accuracy_score(YTest, YPrediction)

        print("K =", K, "Accuracy =", Accuracy * 100, "%")


def main():

    print("-------------------------------")
    print("Marvellous Play Predictor")
    print("-------------------------------")

    # Step 1
    FileName = "MarvellousInfosystems_PlayPredictor.csv"
    df = LoadData(FileName)

    print("\nDataset:")
    print(df)

    # Step 2
    df, WeatherEncoder, TemperatureEncoder, PlayEncoder = PrepareData(df)

    print("\nEncoded Dataset:")
    print(df)

    # Step 3
    Model = TrainData(df)

    print("\nModel training completed successfully.")

    # Step 4
    TestData(
        Model,
        WeatherEncoder,
        TemperatureEncoder,
        PlayEncoder
    )

    # Step 5
    CheckAccuracy(df)


if __name__ == "__main__":
    main()