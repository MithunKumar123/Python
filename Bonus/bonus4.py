contents = ["Mithun is working at arm",
            "Monisha is working at cognizant",
            "Ivanshika is a new born baby, just 7 months"]

files = ["mithun.txt",
         "monisha.txt",
         "iva.txt"]

for content, file in zip(contents, files):
    filePtr = open(f"../files/{file}", "w")
    filePtr.write(content)