#Question1
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
thrL = Seq("ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGA")
print("Length:", len(thrL))
print("GC content:",round((gc_fraction(thrL))* 100,2))
print("Translation:", thrL.translate())
print("Translation without stop:", thrL.translate(to_stop=True))
print("Number of ACC:", str(thrL).count("ACC"))
print("Last codon:", thrL[-3:])
print("First 12 bases of reverse complement:", thrL.reverse_complement()[:12])


#Question2
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
records = list(SeqIO.parse("lab_genes.fasta", "fasta"))
print("Number of records:", len(records))
print("\nID\tLength\tGC%\t\tProtein")
for record in records:
    seq = record.seq
    length = len(seq)
    gc = gc_fraction(seq) * 100
    protein = seq.translate(to_stop=True)
    print("{}\t{}\t{:.2f}%\t{}".format(record.id, length, gc, protein))
high_gc = []
for record in records:
    gc = gc_fraction(record.seq) * 100
    if gc >= 50:
        high_gc.append(record)
SeqIO.write(high_gc, "lab_high_gc.fasta", "fasta")
print("\nNumber of high GC genes:", len(high_gc))
sorted_records = sorted(records, key=lambda x: gc_fraction(x.seq), reverse=True)
print("\nIDs sorted by GC content (highest to lowest):")
for record in sorted_records:
    print(record.id)


#Question3
from Bio.Seq import Seq
mystery = Seq("CCATGGCTTGGAAATAGCATGCCCTAA")
for i in range(3): #forward strand
    frame = mystery[i:]
    frame = frame[:len(frame) - len(frame) % 3]
    print("Frame +{}: {}".format(i + 1, frame.translate()))
rev = mystery.reverse_complement() #reverse complement
for i in range(3):
    frame = rev[i:]
    frame = frame[:len(frame) - len(frame) % 3]
    print("Frame -{}: {}".format(i + 1, frame.translate()))

sequences = [mystery,mystery.reverse_complement()]
longest_orf = ""
for seq in sequences:
    for i in range(3):
        frame = seq[i:]
        frame = frame[:len(frame) - len(frame) % 3]
        protein = str(frame.translate())
        parts = protein.split("*")
        for part in parts[:-1]:
            if "M" in part:
                orf = part[part.index("M"):] + "*"
                if len(orf) > len(longest_orf):
                    longest_orf = orf
print("Longest ORF:", longest_orf)
print("Length:", len(longest_orf), "amino acids")


#Question4
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO
plasmid_seq = Seq("GGATCCTTATGGCTAGCAAAGGAGAAGAACTTTTCACTTAAGAATTCCC")

record = SeqRecord(plasmid_seq,id="PLAB001",name="PLAB001",description="Cloning construct")
record.annotations["molecule_type"] = "DNA"
bamhi = SeqFeature(FeatureLocation(0, 6),type="misc_feature",qualifiers={"note": ["BamHI site"]})
cds = SeqFeature(FeatureLocation(8, 41),type="CDS",qualifiers={"gene": ["labA"],"translation": ["MASKGEELFT"]})
ecori = SeqFeature(FeatureLocation(41, 47),type="misc_feature",qualifiers={"note": ["EcoRI site"]})
record.features = [bamhi, cds, ecori]
print("SeqRecord created successfully")
print(record)
SeqIO.write(record, "lab_construct.gb", "genbank")
print("\nGenBank file created successfully!")
record = SeqIO.read("lab_construct.gb", "genbank")
print("\nFeatures in the GenBank file:\n")
for feature in record.features:
    start = int(feature.location.start) + 1
    end = int(feature.location.end)
    print("Feature type:", feature.type)
    print("Start position:", start)
    print("End position:", end)
    print("Qualifiers:", feature.qualifiers)
    print()
for feature in record.features:
    if feature.type == "CDS":
        cds_seq = feature.extract(record.seq)
        protein = cds_seq.translate(to_stop=True)
        stored_translation = feature.qualifiers["translation"][0]
        print("CDS sequence:", cds_seq)
        print("Translated protein:", protein)
        print("Stored translation:", stored_translation)
        if str(protein) == stored_translation:
            print("Translation matches!")
        else:
            print("Translation does not match!")