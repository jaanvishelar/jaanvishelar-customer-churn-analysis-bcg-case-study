import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv("data/final_model_data.csv")

print(df.shape)
print(df.head())

# Split features & target
X = df.drop(["churn", "id"], axis=1)
y = df["churn"]

# Convert categorical variables into numbers
X = pd.get_dummies(X, drop_first=True)

# Handle missing values
X = X.fillna(0)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))