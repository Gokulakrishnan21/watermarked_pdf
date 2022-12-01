import PyPDF2

sample = PyPDF2.PdfFileReader(open("super.pdf", "rb"))

watermarks = PyPDF2.PdfFileReader(open("watermark.pdf", "rb"))

output = PyPDF2.PdfFileWriter()

for i in range(sample.getNumPages()):
    page = sample.getPage(i)
    page.mergePage(watermarks.getPage(0))
    output.addPage(page)

    with open("watermarked.pdf", "wb") as file:
        output.write(file)


