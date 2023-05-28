import os
os.system("clear")

class DnaAnalyse:
    def __init__(self, seq):
        self.seq = seq.lower()

    def __str__(self):
        return f"DNA with this sequence : {self.seq}"

    def __len__(self):
        return len(self.seq)

    def nucleotide_to_protein(self):
        dict_NP = {
            "ttt" : "P",
            "ttc" : "P",
            "tta" : "L",
            "ttg" : "L",
            "ctt" : "L",
            "ctc" : "L",
            "cta" : "L",
            "ctg" : "L",
            "att" : "I",
            "atc" : "I",
            "ata" : "I",
            "atg" : "M",
            "gtt" : "V",
            "gtc" : "V",
            "gta" : "V",
            "gtg" : "V",
            "tct" : "S",
            "tcc" : "S",
            "tca" : "S",
            "tcg" : "S",
            "cct" : "P",
            "ccc" : "P",
            "cca" : "P",
            "ccg" : "P",
            "act" : "T",
            "acc" : "T",
            "aca" : "T",
            "acg" : "T",
            "gct" : "A",
            "gcc" : "A",
            "gca" : "A",
            "gcg" : "A",
            "tat" : "Y",
            "tac" : "Y",
            "taa" : "STOP",
            "tag" : "STOP",
            "cat" : "H",
            "cac" : "H",
            "caa" : "Q",
            "cag" : "Q",
            "aat" : "N",
            "aac" : "N",
            "aaa" : "K",
            "aag" : "K",
            "gat" : "D",
            "gac" : "D",
            "gaa" : "E",
            "gag" : "E",
            "tgt" : "C",
            "tgc" : "C",
            "tga" : "STOP",
            "tgg" : "W",
            "cgt" : "R",
            "cgc" : "R",
            "cga" : "R",
            "cgg" : "R",
            "agt" : "S",
            "agc" : "S",
            "aga" : "R",
            "agg" : "R",
            "ggt" : "G",
            "ggc" : "G",
            "gga" : "G",
            "ggg" : "G",

        }
        protein = []
        three_codons = []
        start = 0
        end = 3
        if len(self.seq) % 3 == 0:
            for i in range(0, len(self.seq) // 3):
                three_codons.append((self.seq[start : end]))
                start = end
                end += 3    
        else:
            print("the number of your codon in not a multiple of 3")
            
        for i in three_codons:
            protein.append(dict_NP[i])
        return "".join(protein).upper()

dna1 = DnaAnalyse(
"""ACCGAACAGTATTGGAAAAGGATCTGAAAGTTTGTGAATGGATGTTGCAAGTCGTCAAAGTAGGATGGCGTGTTGCAAGTCGTCAAAGTA"""
)
print(dna1.nucleotide_to_protein())
print(f'DNA length is : {len(dna1)}')


        # dict_NP = {
        #     "uuu" : "P",
        #     "uuc" : "P",
        #     "uua" : "L",
        #     "uug" : "L",
        #     "cuu" : "L",
        #     "cuc" : "L",
        #     "cua" : "L",
        #     "cug" : "L",
        #     "auu" : "I",
        #     "auc" : "I",
        #     "aua" : "I",
        #     "aug" : "M",
        #     "guu" : "V",
        #     "guc" : "V",
        #     "gua" : "V",
        #     "gug" : "V",
        #     "ucu" : "S",
        #     "ucc" : "S",
        #     "uca" : "S",
        #     "ucg" : "S",
        #     "ccu" : "P",
        #     "ccc" : "P",
        #     "cca" : "P",
        #     "ccg" : "P",
        #     "acu" : "T",
        #     "acc" : "T",
        #     "aca" : "T",
        #     "acg" : "T",
        #     "gcu" : "A",
        #     "gcc" : "A",
        #     "gca" : "A",
        #     "gcg" : "A",
        #     "uau" : "Y",
        #     "uac" : "Y",
        #     "uaa" : "STOP",
        #     "uag" : "STOP",
        #     "cau" : "H",
        #     "cac" : "H",
        #     "caa" : "Q",
        #     "cag" : "Q",
        #     "aau" : "N",
        #     "aac" : "N",
        #     "aaa" : "K",
        #     "aag" : "K",
        #     "gau" : "D",
        #     "gac" : "D",
        #     "gaa" : "E",
        #     "gag" : "E",
        #     "ugu" : "C",
        #     "ugc" : "C",
        #     "uga" : "STOP",
        #     "ugg" : "W",
        #     "cgu" : "R",
        #     "cgc" : "R",
        #     "cga" : "R",
        #     "cgg" : "R",
        #     "agu" : "S",
        #     "agc" : "S",
        #     "aga" : "R",
        #     "agg" : "R",
        #     "ggu" : "G",
        #     "ggc" : "G",
        #     "gga" : "G",
        #     "ggg" : "G",
        # }