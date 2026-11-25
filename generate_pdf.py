import sys
import os
class SimplePDF:
    def __init__(self):
        self.pages = []
        self.current_page_commands = []
        
    def add_page(self):
        if self.current_page_commands:
            self.pages.append(self.current_page_commands)
            self.current_page_commands = []
    def set_font(self, font_name, size):
        self.current_page_commands.append(f"/{font_name} {size} Tf")
    def draw_text(self, x, y, text):
        clean_text = text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
        self.current_page_commands.append(f"BT {x:.2f} {y:.2f} Td ({clean_text}) Tj ET")
    def draw_line(self, x1, y1, x2, y2, width=0.5, r=0.2, g=0.2, b=0.2):
        self.current_page_commands.append(f"{width} w {r:.2f} {g:.2f} {b:.2f} RG {x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S")
    def draw_rect(self, x, y, w, h, fill_r=0.95, fill_g=0.95, fill_b=0.95):
        self.current_page_commands.append(f"{fill_r:.2f} {fill_g:.2f} {fill_b:.2f} rg {x:.2f} {y:.2f} {w:.2f} {h:.2f} re f")
    def build(self, filename):
        if self.current_page_commands:
            self.pages.append(self.current_page_commands)
            self.current_page_commands = []
        page_count = len(self.pages)
        objects = []
        
        # 1: Catalog
        objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
        
        # 2: Pages
        kids_refs = [f"{3 + i*2} 0 R" for i in range(page_count)]
        kids_str = " ".join(kids_refs)
        objects.append(f"<< /Type /Pages /Kids [{kids_str}] /Count {page_count} >>".encode('latin1'))
        # Fonts: F1 (Helvetica), F2 (Helvetica-Bold), F3 (Helvetica-Oblique)
        font_f1 = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"
        font_f2 = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>"
        font_f3 = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique >>"
        
        font_f1_idx = 3 + page_count * 2
        font_f2_idx = font_f1_idx + 1
        font_f3_idx = font_f2_idx + 1
        for i, page_cmds in enumerate(self.pages):
            content_idx = 4 + i * 2
            page_obj = f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595.28 841.89] /Resources << /Font << /F1 {font_f1_idx} 0 R /F2 {font_f2_idx} 0 R /F3 {font_f3_idx} 0 R >> >> /Contents {content_idx} 0 R >>".encode('latin1')
            objects.append(page_obj)
            
