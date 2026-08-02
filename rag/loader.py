from pypdf import PdfReader

def load_resume(path="documents/ajeet_resume (4).pdf"):
    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"

    return text