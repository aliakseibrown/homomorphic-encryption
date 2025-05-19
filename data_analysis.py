import pandas as pd
import numpy as np

class MedicalData:
    def __init__(self, n_samples=1000):
        self.data = self.generate_synthetic_data(n_samples)
    
    def generate_synthetic_data(self, n_samples):
        return pd.DataFrame({
            'age': np.random.randint(18, 90, n_samples),
            'blood_pressure': np.random.normal(120, 20, n_samples),
            'cholesterol': np.random.gamma(2, 2, n_samples)
        })
    
    def analyze_encrypted(self, encrypted_data):
        # Przykładowa analiza na zaszyfrowanych danych
        mean = encrypted_data.mean()
        variance = encrypted_data.variance()
        return {'mean': mean, 'variance': variance}