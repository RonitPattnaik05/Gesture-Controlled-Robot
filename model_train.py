import pandas as pd 
import joblib 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score 
 
df = pd.read_csv("gesture_dataset_cleaned.csv") 
 
X = df.drop("label", axis=1) 
y = df["label"] 
 
scaler = StandardScaler() 
X_scaled = scaler.fit_transform(X) 
 
X_train, X_test, y_train, y_test = train_test_split( 
    X_scaled, y, test_size=0.2, random_state=42, stratify=y 
 
 
) 
 
model = RandomForestClassifier(n_estimators=200, random_state=42) 
model.fit(X_train, y_train) 
 
y_pred = model.predict(X_test) 
print("Accuracy:", accuracy_score(y_test, y_pred)) 
 
joblib.dump(model, "gesture_model.pkl") 
joblib.dump(scaler, "scaler.pkl") 
print("Model saved")
