# DNA sequence analyser

#1
import matplotlib.pyplot as plt

dna=(input("Enter DNA sequence:")).upper()

valid_bases="ATGC"
if all(base in valid_bases for base in dna):
   print("valid DNA sequence:",dna)
   

else:
   print("not valid DNA sequence ")
   print("use only A,T,G and C")

lenght=len(dna)
print("lenght of DNA sequence is:",lenght)


a=dna.count("A")
t=dna.count("T")
g=dna.count("G")
c=dna.count("C")
print("A:",a)
print("T:",t)
print("G:",g)
print("C:",c)

gc_content=((g+c)/lenght)*100

print("GC %:",gc_content)

at_content=100-gc_content
print("AT %:",at_content)

# bar graph

bases =["A","G","C","T"]
counts=[a,t,g,c]

plt.bar(bases,counts)
plt.xlabel("DNA Bases")
plt.ylabel("frequency")
plt.title("DNA Base frequency")
plt.show()


# pie chart

lables=["GC","AT"]
values=[gc_content,at_content]

plt.pie(values,labels=lables, autopct="%1.1f%%")
plt.title("GC vs AT content")
plt.show()



compliment=""

for base in dna:
   if base=="A":
      compliment+="T"
   elif base =="T":
      compliment+= "A"
   elif base =="G":
      compliment+="C"
   elif base =="C":
      compliment+="G"

print("compliment:",compliment)
   

rna=dna.replace("T","U")
print("RNA:",rna)

if "AUG" in rna:
   print("start codon found")
else:
   print("no start codon found")

stop_codons=["UAA","UAG","UGA"]

for stop in stop_codons:
   if stop in rna:
      print("stop codon found:",stop)

