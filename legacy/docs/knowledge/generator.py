import os
import markdown2
from fpdf import FPDF

class PolymathKnowledgePDF(FPDF):
    def header(self):
        self.set_fill_color(11, 11, 11)
        self.rect(0, 0, 210, 297, 'F') # Full page background
        self.set_font('Helvetica', 'B', 8)
        self.set_text_color(85, 85, 85)
        self.cell(0, 10, 'POLYMATH.SYS // THE KNOWLEDGE BASE & RETROSPECTIVE', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(68, 68, 68)
        self.cell(0, 10, f'Page {self.page_no()} -- SYSTEM MEMORY CORE', 0, 0, 'C')

def generate_pdf(md_file, pdf_file):
    # 1. READ MARKDOWN
    with open(md_file, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # 2. INITIALIZE PDF
    pdf = PolymathKnowledgePDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # 3. SANITIZE UNICODE (fpdf2 default fonts only support latin-1)
    replacements = {
        '\u2014': '-',  # em dash
        '\u2013': '-',  # en dash
        '\u201c': '"',  # left double quote
        '\u201d': '"',  # right double quote
        '\u2018': "'",  # left single quote
        '\u2019': "'",  # right single quote
        '\u2022': '*',  # bullet
    }
    for unicode_char, ascii_char in replacements.items():
        md_text = md_text.replace(unicode_char, ascii_char)

    # Final sweep for any remaining non-latin-1 characters
    md_text = md_text.encode('latin-1', 'replace').decode('latin-1')

    # 4. PARSE AND RENDER (Simplified Parser for FPDF)
    lines = md_text.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            pdf.ln(5)
            continue
            
        if line.startswith('# '):
            pdf.ln(10)
            pdf.set_font('Helvetica', 'B', 24)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(0, 15, line[2:], ln=True)
            pdf.set_draw_color(35, 35, 35)
            pdf.line(pdf.get_x(), pdf.get_y(), pdf.get_x() + 170, pdf.get_y())
            pdf.ln(5)
        elif line.startswith('## '):
            pdf.ln(8)
            pdf.set_font('Helvetica', 'B', 16)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(0, 12, line[3:].upper(), ln=True)
            pdf.ln(2)
        elif line.startswith('### '):
            pdf.ln(5)
            pdf.set_font('Helvetica', 'B', 12)
            pdf.set_text_color(200, 200, 200)
            pdf.cell(0, 10, line[4:], ln=True)
        elif line.startswith('- ') or line.startswith('* '):
            pdf.set_font('Helvetica', '', 10)
            pdf.set_text_color(180, 180, 180)
            pdf.multi_cell(0, 7, f"  * {line[2:]}") # Fixed bullet
        elif line.startswith('> '):
            pdf.set_font('Helvetica', 'I', 10)
            pdf.set_text_color(136, 136, 136)
            pdf.multi_cell(0, 7, f"    {line[2:]}", border='L')
        else:
            pdf.set_font('Helvetica', '', 11)
            pdf.set_text_color(237, 237, 237)
            # Handle basic bold
            cleaned_line = line.replace('**', '')
            pdf.multi_cell(0, 7, cleaned_line)

    pdf.output(pdf_file)
    print(f"Success! PDF generated at: {pdf_file}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_md = os.path.join(current_dir, "knowledge.md")
    output_pdf = os.path.join(current_dir, "knowledge.pdf")
    generate_pdf(input_md, output_pdf)
