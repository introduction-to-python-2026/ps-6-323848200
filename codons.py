def create_codon_dict(file_path):
    codon_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            
            if not line:
                continue
                
            parts = line.split()
            
            if len(parts) >= 4:
                codon, amino_acid, single_letter, full_name = parts[:4]
                codon_dict[codon] = single_letter
                
    return codon_dict
