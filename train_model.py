import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

def generate_synthetic_data(n_samples=2000):
    np.random.seed(42)
    data = []
    
    for _ in range(n_samples):
        q1 = np.random.randint(0, 5)
        q2 = np.random.randint(0, 5)
        q3 = np.random.randint(0, 5)
        q4 = np.random.randint(0, 5)
        q5 = np.random.randint(0, 5)
        q6 = np.random.randint(0, 5)
        q7 = np.random.randint(0, 5)
        q8 = np.random.randint(0, 5)
        q9 = np.random.randint(0, 5)
        q10 = np.random.randint(0, 5)
        
        total_score = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10
        
        if total_score <= 13:
            stress_level = 0  # Low
        elif total_score <= 26:
            stress_level = 1  # Moderate
        else:
            stress_level = 2  # High
            
        data.append([q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, stress_level])
        
    df = pd.DataFrame(data, columns=[
        'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'stress_level'
    ])
    return df

def main():
    print("Generating synthetic dataset...")
    df = generate_synthetic_data()
    df.to_csv('data/stress_dataset.csv', index=False)
    print(f"Dataset saved to data/stress_dataset.csv with {len(df)} samples")
    
    X = df.drop('stress_level', axis=1)
    y = df['stress_level']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("Training Random Forest model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    y_pred = model.predict(X_test_scaled)
    print("\nModel Evaluation:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Low', 'Moderate', 'High']))
    
    joblib.dump(model, 'models/stress_model.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    print("\nModel and scaler saved to models/ directory")

if __name__ == "__main__":
    main()
