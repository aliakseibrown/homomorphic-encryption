import tenseal as ts

class HESystem:
    def __init__(self, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 40, 60]):
        self.context = ts.context(
            ts.SCHEME_TYPE.CKKS,
            poly_modulus_degree=poly_mod_modulus_degree,
            coeff_mod_bit_sizes=coeff_mod_bit_sizes
        )
        self.context.generate_galois_keys()
        self.context.global_scale = 2**40

    def encrypt(self, data):
        return ts.ckks_vector(self.context, data)
    
    def decrypt(self, encrypted_vector):
        return encrypted_vector.decrypt()
    
    def optimize_parameters(self, new_poly_degree, new_coeff_sizes):
        self.context = ts.context(
            ts.SCHEME_TYPE.CKKS,
            poly_modulus_degree=new_poly_degree,
            coeff_mod_bit_sizes=new_coeff_sizes
        )