from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["OOPs Concept/ClutteredFolder/file1.pdf", "OOPs Concept/ClutteredFolder/file2.pdf", "OOPs Concept/ClutteredFolder/file3.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
