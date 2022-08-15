def read_dna(dna_file):
    """
    Read a DNA string from a file.
    the file contains data in the following format:
    A <-> T
    G <-> C
    G <-> C
    C <-> G
    G <-> C
    T <-> A
    Output a list of touples:
    [
        ('A', 'T'),
        ('G', 'C'),
        ('G', 'C'),
        ('C', 'G'),
        ('G', 'C'),
        ('T', 'A'),
    ]
    Where either (or both) elements in the string might be missing:
    <-> T
    G <->
    G <-> C
    <->
    <-> C
    T <-> A
    Output:
    [
        ('', 'T'),
        ('G', ''),
        ('G', 'C'),
        ('', ''),
        ('', 'C'),
        ('T', 'A'),
    ]
    """
    import re

    output = []
    infile = open(dna_file)
    for line in infile:
        pattern = re.search('([A-Z])? ?<-> ?([A-Z])?', line)
        left = pattern.group(1)
        right = pattern.group(2)
        if left == None:
            left = ''
        if right == None:
            right = ''
        tuple = (left, right)
        output.append(tuple)
    return output


def is_rna(dna):
    """
    Given DNA in the aforementioned format,
    return the string "DNA" if the data is DNA,
    return the string "RNA" if the data is RNA,
    return the string "Invalid" if the data is neither DNA nor RNA.
    DNA consists of the following bases:
    Adenine  ('A'),
    Thymine  ('T'),
    Guanine  ('G'),
    Cytosine ('C'),
    RNA consists of the following bases:
    Adenine  ('A'),
    Uracil   ('U'),
    Guanine  ('G'),
    Cytosine ('C'),
    The data is DNA if at least 90% of the bases are one of the DNA bases.
    The data is RNA if at least 90% of the bases are one of the RNA bases.
    The data is invalid if more than 10% of the bases are not one of the DNA or RNA bases.
    Empty bases should be ignored.
    """
    list = []
    for tuple in dna:
        list.append(tuple[0])
        list.append(tuple[1])
    dna_count = 0
    rna_count = 0
    for item in list:
        if item == 'A' or item == 'T' or item == 'G' or item == 'C':
            dna_count += 1
        if item == 'A' or item == 'U' or item == 'G' or item == 'C':
            rna_count += 1
    if dna_count/len(list) >= 0.9:
        return "DNA"
    elif rna_count/len(list) >= 0.9:
        return "RNA"
    else:
        return "Invalid"

def clean_dna(dna):
    """
    Given DNA in the aforementioned format,
    If the pair is incomplete, ('A', '') or ('', 'G'), ect
    Fill in the missing base with the match base.
    In DNA 'A' matches with 'T', 'G' matches with 'C'
    In RNA 'A' matches with 'U', 'G' matches with 'C'
    If a pair contains an invalid base the pair should be removed.
    Pairs of empty bases should be ignored.
    """
    list = []
    for tuple in dna:
        list.append(tuple[0])
        list.append(tuple[1])
    dna_count = 0
    rna_count = 0
    for item in list:
        if item == 'A' or item == 'T' or item == 'G' or item == 'C':
            dna_count += 1
        if item == 'A' or item == 'U' or item == 'G' or item == 'C':
            rna_count += 1
    if dna_count/len(list) >= 0.9:
        type = "DNA"
    elif rna_count/len(list) >= 0.9:
        type = "RNA"
    else:
        type = "Invalid"

    new_list = []
    for tuple in dna:
        if type == "DNA":
            if tuple[0] != '' and tuple[1] != '':
                new_list.append(tuple)
            elif tuple[0] != '' and tuple[1] == '':
                if tuple[0] == 'A':
                    new_list.append((tuple[0],'T'))
                elif tuple[0] == 'T':
                    new_list.append((tuple[0],'A'))
                elif tuple[0] == 'C':
                    new_list.append((tuple[0],'G'))
                elif tuple[0] == 'G':
                    new_list.append((tuple[0],'C'))
            elif tuple[0] == '' and tuple[1] != '':
                if tuple[1] == 'A':
                    new_list.append(('T',tuple[1]))
                elif tuple[1] == 'T':
                    new_list.append(('A',tuple[1]))
                elif tuple[1] == 'C':
                    new_list.append(('G',tuple[1]))
                elif tuple[1] == 'G':
                    new_list.append(('C',tuple[1]))
        elif type == "RNA":
            if tuple[0] != '' and tuple[1] != '':
                new_list.append(tuple)
            elif tuple[0] != '' and tuple[1] == '':
                if tuple[0] == 'A':
                    new_list.append((tuple[0],'U'))
                elif tuple[0] == 'U':
                    new_list.append((tuple[0],'A'))
                elif tuple[0] == 'C':
                    new_list.append((tuple[0],'G'))
                elif tuple[0] == 'G':
                    new_list.append((tuple[0],'C'))
            elif tuple[0] == '' and tuple[1] != '':
                if tuple[1] == 'A':
                    new_list.append(('U',tuple[1]))
                elif tuple[1] == 'U':
                    new_list.append(('A',tuple[1]))
                elif tuple[1] == 'C':
                    new_list.append(('G',tuple[1]))
                elif tuple[1] == 'G':
                    new_list.append(('C',tuple[1]))
    return new_list
            

def mast_common_base(dna):
    """
    Given DNA in the aforementioned format,
    return the most common first base:
    eg. given:
    A <-> T
    G <-> C
    G <-> C
    C <-> G
    G <-> C
    T <-> A
    The most common first base is 'G'.
    Empty bases should be ignored.
    """
    list = []
    for tuple in dna:
        list.append(tuple[0])
    A_count = 0
    T_count = 0
    U_count = 0
    G_count = 0
    C_count = 0
    for item in list:
        if item == 'A':
            A_count += 1
        if item == 'T':
            T_count += 1
        if item == 'U':
            U_count += 1
        if item == 'G':
            G_count += 1
        if item == 'C':
            C_count += 1
    max_num = max(A_count,T_count,U_count,G_count,C_count)
    if A_count == max_num:
        return "A"
    elif T_count == max_num:
        return "T"
    elif U_count == max_num:
        return "U"
    elif G_count == max_num:
        return "G"
    elif C_count == max_num:
        return "C"

def base_to_name(base):
    """
    Given a base, return the name of the base.
    The base names are:
    Adenine  ('A'),
    Thymine  ('T'),
    Guanine  ('G'),
    Cytosine ('C'),
    Uracil   ('U'),
    return the string "Unknown" if the base isn't one of the above.
    """
    if base == 'A':
        return "Adenine"
    elif base == 'T':
        return "Thymine"
    elif base == 'U':
        return "Uracil"
    elif base == 'G':
        return "Guanine"
    elif base == 'C':
        return "Cytosine"