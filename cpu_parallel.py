from joblib import Parallel, delayed
import multiprocessing

class CPUProcessor:
    def __init__(self, n_jobs=None):
        self.n_jobs = n_jobs or multiprocessing.cpu_count()
        
    def parallel_mean(self, encrypted_data):
        def chunk_mean(chunk):
            return sum(chunk) / len(chunk)
        
        chunk_size = len(encrypted_data) // self.n_jobs
        chunks = [encrypted_data[i:i+chunk_size] for i in range(0, len(encrypted_data), chunk_size)]
        
        results = Parallel(n_jobs=self.n_jobs)(
            delayed(chunk_mean)(chunk) for chunk in chunks
        )
        return sum(results) / len(results)