from fpdf import FPDF

def export_results_to_pdf(player):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Quiz Results for {player.name}", ln=True)
    pdf.cell(200, 10, txt=f"Final Score: {player.score}", ln=True)
    pdf.cell(200, 10, txt="", ln=True)

    pdf.cell(200, 10, txt="Category-wise Stats:", ln=True)
    for category, data in player.stats.items():
        line = f"{category}: {data['correct']} / {data['total']}"
        pdf.cell(200, 10, txt=line, ln=True)

    filename = f"{player.name}_results.pdf"
    pdf.output(filename)
    print(f" PDF exported: {filename}")
