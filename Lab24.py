class DNASequence:
    def __init__(self, seq,id="DNA_1"):
        self.id=id
        self.seq = seq
        self.cleaned_seq = ''.join(seq.split()).upper()
        self.length_seq = len(self.cleaned_seq)
        self.counts = {}
        self.gc = 0

    def __str__(self): #special method which is automatically called when an object is printed
        return f'Input sequence:{self.seq} \nCleaned sequence:{self.cleaned_seq} \nCleaned sequence ID:{self.id}'

    def length(self):
        return self.length_seq

    def count_bases(self):
        self.counts={base:self.cleaned_seq.count(base) for base in self.cleaned_seq}
        print("Count of bases:",self.counts)
        return

    def gc_percentage(self):
        self.gc=((self.counts['G']+self.counts['C'])/self.length_seq)*100
        print("GC Percentage:",self.gc,"%")
        return

    #1. Write complement(). Pair A with T and G with C using a dictionary, and return a new DNASequence whose ID is the old ID plus "_comp".
    def complement(self):
        pairs={'A':'T','C':'G','G':'C','T':'A'}
        complement_seq="".join([pairs[base] for base in self.cleaned_seq])
        self.comp_id = self.id + "_comp" #create an instance attribute-accessible outside method using the object
        return complement_seq

    #2. Write reverse_complement(). Call self.complement(), reverse its sequence, and return a new DNASequence with the ID suffix "_revcomp".
    def reverse_complement(self):
        comp=self.complement()
        reversed_seq=comp[::-1]
        self.rev_id = self.id + "_revcomp" #create an instance attribute-accessible outside method using the object
        return reversed_seq

    #3. Write transcribe(), which returns the mRNA as a string, with every T replaced by U.
    def transcribe(self):
        transcribed_seq= self.cleaned_seq.replace('T', 'U')
        print("Transcribed sequence:",transcribed_seq)

    #4. Write find_site(site), which returns a list of every position where site occurs, counting from 1. Return an empty list if there are none.
    def find_site(self,site):
        site = site.upper()
        positions = []
        for i in range(len(self.cleaned_seq) - len(site) + 1):
            if self.cleaned_seq[i:i+len(site)] == site:
                positions.append(i + 1)
        return positions

    #5. To check if the given DNA sequence is valid
    def is_valid(self):
        for base in self.cleaned_seq:
            if base not in 'ATGC':
                print("The given Sequence is not valid.")
        print("The given Sequence is valid.")

    #6. To extract a particular region
    def subsequence(self, start, end):
        return self.cleaned_seq[start - 1:end]

    #7. To calculate the frequency of each nucleotide as a percentage
    def nucleotide_frequency(self):
        bases = ['A', 'T', 'G', 'C']
        freq = {base: round((self.cleaned_seq.count(base) / self.length_seq) * 100, 2) for base in bases}
        return freq

    #8. To translate the sequence
    def translate(self):
        codon_table = {'ATG': 'M', 'TTT': 'F', 'TTC': 'F','TAA': '*', 'TAG': '*', 'TGA': '*','GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A'}
        protein = ''
        start = self.cleaned_seq.find('ATG')
        if start == -1:
            return "No start codon found"
        for i in range(start, len(self.cleaned_seq) - 2, 3):
            codon = self.cleaned_seq[i:i + 3]
            if codon in ('TAA', 'TAG', 'TGA'):
                break
            protein += codon_table.get(codon, 'X')
        return protein


input_seq = ' AatgcTT AAGGCC TT'
dna_seq = DNASequence(input_seq) #creating an object dna_seq
print(dna_seq) #this calls dna_seq.__str__()
print("Length of the DNA sequence:",dna_seq.length())
dna_seq.count_bases()
dna_seq.gc_percentage()
print("Complementary Sequence:",dna_seq.complement())
print("Complementary Sequence ID:",dna_seq.comp_id)
print("Reverse Complement Sequence:",dna_seq.reverse_complement())
print("Reverse Complement Sequence ID:",dna_seq.rev_id)
dna_seq.transcribe()
print("List of positions where site occurs:",dna_seq.find_site('TT'))
dna_seq.is_valid()
print("The subsequence is:",dna_seq.subsequence(2,5))
print("The frequency of each nucleotide(%):",dna_seq.nucleotide_frequency())
print("Translated Sequence:",dna_seq.translate())




