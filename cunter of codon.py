def counte_of_codon(codon, dna):# fined of codon in DNA
    number_of_codon = 0
    for counter in dna:
        if codon in counter:
            number_of_codon += 1
    return number_of_codon
print(counte_of_codon('t', 'cccttcgctattttccgttag'))

    