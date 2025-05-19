import streamlit as st
import time
import matplotlib.pyplot as plt

from he_encryption import HESystem
from data_analysis import MedicalData
from cpu_parallel import CPUProcessor
from gpu_parallel import GPUProcessor

def main():
    st.title("Secure Medical Data Analysis")
    
    # Inicjalizacja komponentów
    he = HESystem()
    data = MedicalData()
    cpu = CPUProcessor()
    gpu = GPUProcessor()
    
    # Interfejs użytkownika
    uploaded_file = st.file_uploader("Upload medical data (CSV)")
    if uploaded_file:
        data.data = pd.read_csv(uploaded_file)
    
    if st.button("Run Analysis"):
        # Przetwarzanie surowych danych
        start = time.time()
        raw_mean = data.data['blood_pressure'].mean()
        raw_time = time.time() - start
        
        # Przetwarzanie z HE i CPU
        encrypted_data = [he.encrypt(row) for row in data.data['blood_pressure']]
        
        start = time.time()
        cpu_result = cpu.parallel_mean(encrypted_data)
        cpu_time = time.time() - start
        
        # Wizualizacja
        fig, ax = plt.subplots()
        times = [raw_time, cpu_time]
        labels = ['Raw Data', 'Encrypted (CPU)']
        ax.bar(labels, times)
        st.pyplot(fig)
        
if __name__ == "__main__":
    main()