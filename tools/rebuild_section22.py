#!/usr/bin/env python3
"""Rebuild section 2.2 (Overview of the studies) of Chapter 2.

Reads the pristine chapter (chapters/Chapter 2.original.docx) and writes
chapters/Chapter 2.docx with:

  * the rewritten overview paragraph,
  * the existing transition paragraph kept unchanged,
  * Table 2.1 (Papers 1 to 7) rebuilt as a six-column overview,
  * Table 2.2 (Papers 8 to 13) added on the same pattern,
  * the old five-column table, the figure, the figure caption, the figure
    note and the yellow editorial note removed.

Every cell is checked against the published papers in papers/.
Run from the repository root:  python3 tools/rebuild_section22.py
"""

import copy
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, Twips
from docx.table import Table
from docx.text.paragraph import Paragraph

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "chapters" / "Chapter 2.original.docx"
DST = ROOT / "chapters" / "Chapter 2.docx"

BODY = 11        # pt, matches Normal
CELL = 8         # pt, table cells
NOTE = 9         # pt, table notes
TOTAL_W = 9360   # twips, usable width on Letter with 1in margins

# ---------------------------------------------------------------- content

OVERVIEW = (
    "The thirteen studies fall into three groups. Six cross-country studies come first. "
    "They cover public energy research, development, and demonstration (RD&D) budgets, "
    "artificial intelligence (AI), industrial robots, and the role of environmental governance. "
    "They ask whether the environmental effect depends on how budgets are allocated, "
    "on skills and institutions, and on the stage of adoption. "
    "A regional study of the Middle East and North Africa (MENA) then turns to technology "
    "that enters through foreign direct investment (FDI) and asks whether its effect depends "
    "on the sector that receives the investment. "
    "Six studies of Algeria come last and focus on one hydrocarbon-dependent economy over "
    "long quarterly series. They relate emissions and the ecological footprint to innovation, "
    "energy use, policy uncertainty, efficiency, finance, and resource rents, and five of them "
    "separate rises from falls. "
    "Table 2.1 summarises Papers 1 to 7, and Table 2.2 summarises Papers 8 to 13."
)

T1_CAPTION_NUM = "Table 2.1. "
T1_CAPTION_TXT = "Overview of the global, comparative, and regional studies (Papers 1 to 7)"
T1_HEADER = ["Paper", "Sample", "Period", "Main variables", "Methods", "Main finding"]
T1_ROWS = [
    ["1", "Eight top energy RD&D investors", "1990\u20132023, monthly",
     "LCF; total, clean, and dirty energy RD&D budgets", "MQQKRLS; QQGC",
     "Clean budgets raise LCF; effects vary by country and quantile"],
    ["2", "29 advanced and developing economies", "2005\u20132024",
     "LCF; AI patents; labour structure; institutional adaptability",
     "Two-way fixed effects; 2SLS",
     "AI raises LCF; skills and institutions magnify the gain"],
    ["3", "29 advanced and developing economies", "2005\u20132023",
     "CO\u2082 emissions; AI patents; energy intensity; skills; institutions",
     "Two-way fixed effects; 2SLS",
     "AI patents lower emissions, most under adaptable institutions"],
    ["4", "G7 economies", "2000\u20132019, monthly",
     "LCF; operational stock of industrial robots", "MQQR",
     "Robot effect modest early, strong at mature adoption"],
    ["5", "Nine OECD countries", "1997\u20132020",
     "Eco-efficiency; resource overuse; environmental governance; their interaction", "MMQR",
     "Governance restrains overuse most where eco-efficiency is low"],
    ["6", "50 countries", "2000\u20132024",
     "Biocapacity; robot density; institutional flexibility; green patents; "
     "industrial upgrading",
     "Two-way fixed effects; mediation; panel threshold regression",
     "Three upgrading regimes; green innovation the dominant channel"],
    ["7", "13 MENA countries", "1990\u20132022, four-year averages",
     "Total and sectoral CO\u2082; total, extraction, manufacturing, and services FDI",
     "System GMM",
     "Extraction and manufacturing FDI raise emissions; services FDI lowers them"],
]
T1_NOTE = (
    "Notes: LCF, load capacity factor; RD&D, research, development, and demonstration; "
    "AI, artificial intelligence; FDI, foreign direct investment; MQQKRLS, multivariate "
    "quantile-on-quantile kernel-based regularized least squares; QQGC, quantile-on-quantile "
    "Granger causality; 2SLS, two-stage least squares; MQQR, multivariate quantile-on-quantile "
    "regression; MMQR, method of moments quantile regression; GMM, generalized method of "
    "moments. Periods are annual unless stated. The methods column reports the principal "
    "estimators; robustness procedures and identification strategies are described in the "
    "papers, reproduced in the second part of the thesis."
)

T2_CAPTION_NUM = "Table 2.2. "
T2_CAPTION_TXT = "Overview of the Algerian studies (Papers 8 to 13)"
T2_ROWS = [
    ["8", "Algeria", "1980Q1\u20132021Q4",
     "CO\u2082; total patents; fossil fuel energy; renewable energy",
     "NARDL; asymmetric causality",
     "Innovation and fossil shocks asymmetric; renewable gains one-sided"],
    ["9", "Algeria", "1990Q1\u20132022Q4",
     "Ecological footprint; green technology patents",
     "NARDL; asymmetric causality",
     "Green patents lower footprint in both directions, expansion more"],
    ["10", "Algeria", "1980Q1\u20132022Q4",
     "CO\u2082 per capita; policy uncertainty; green technology; income",
     "Fourier NARDL",
     "Rising uncertainty and green patents lower emissions; EKC holds"],
    ["11", "Algeria", "1990Q1\u20132022Q4",
     "CO\u2082 per capita; material efficiency; energy productivity; green patents",
     "Fourier ADL cointegration; NARDL",
     "Energy productivity gains strongest; its losses have no significant effect"],
    ["12", "Algeria", "1990Q1\u20132021Q4",
     "Ecological footprint; green patents; financial development; their interaction",
     "Fourier ARDL",
     "Finance raises footprint; green technology mitigates the harm"],
    ["13", "Algeria", "1970Q1\u20132022Q4",
     "Ecological footprint; total and five resource rents",
     "NARDL; spectral Granger causality",
     "Rent expansion raises footprint more than contraction lowers it"],
]
T2_NOTE = (
    "Notes: NARDL, nonlinear autoregressive distributed lag; ARDL and ADL, autoregressive "
    "distributed lag; EKC, environmental Kuznets curve; CO\u2082, carbon dioxide. All series "
    "are quarterly. Fourier NARDL and Fourier ARDL add trigonometric terms for smooth "
    "structural breaks."
)

WIDTHS = [640, 1560, 1150, 2100, 1600, 2310]   # sums to TOTAL_W

# ---------------------------------------------------------------- helpers


def _spacing(pPr, before=None, line=276):
    sp = OxmlElement("w:spacing")
    if before is not None:
        sp.set(qn("w:before"), str(before))
    sp.set(qn("w:line"), str(line))
    sp.set(qn("w:lineRule"), "auto")
    pPr.append(sp)


def body_paragraph(doc, text, before=None, size=BODY, indent=False):
    """A body paragraph in the chapter's own geometry (1.15 spacing)."""
    p = doc.add_paragraph()
    pPr = p._p.get_or_add_pPr()
    _spacing(pPr, before=before)
    if not indent:
        ind = OxmlElement("w:ind")
        ind.set(qn("w:firstLine"), "0")
        pPr.append(ind)
    run = p.add_run(text)
    run.font.size = Pt(size)
    return p._p


def caption(doc, number, title):
    p = doc.add_paragraph()
    pPr = p._p.get_or_add_pPr()
    _spacing(pPr, before=240)
    num = p.add_run(number)
    num.bold = True
    num.font.size = Pt(BODY)
    rest = p.add_run(title)
    rest.font.size = Pt(BODY)
    return p._p


def note_paragraph(doc, text):
    p = doc.add_paragraph()
    pPr = p._p.get_or_add_pPr()
    _spacing(pPr, before=60, line=240)
    ind = OxmlElement("w:ind")
    ind.set(qn("w:firstLine"), "0")
    pPr.append(ind)
    run = p.add_run(text)
    run.font.size = Pt(NOTE)
    return p._p


def build_table(doc, header, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(header))
    table.style = doc.styles["Plain Table 2"]
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False

    tbl = table._tbl
    tblPr = tbl.tblPr

    # fixed layout and full usable width
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    tblW = tblPr.find(qn("w:tblW"))
    tblW.set(qn("w:type"), "dxa")
    tblW.set(qn("w:w"), str(TOTAL_W))
    look = tblPr.find(qn("w:tblLook"))
    look.set(qn("w:val"), "04A0")
    look.set(qn("w:firstRow"), "1")
    look.set(qn("w:firstColumn"), "0")

    grid = tbl.find(qn("w:tblGrid"))
    for col, width in zip(grid.findall(qn("w:gridCol")), WIDTHS):
        col.set(qn("w:w"), str(width))

    for r_idx, values in enumerate([header] + rows):
        row = table.rows[r_idx]
        trPr = row._tr.get_or_add_trPr()
        cant = OxmlElement("w:cantSplit")
        trPr.append(cant)
        if r_idx == 0:
            hdr = OxmlElement("w:tblHeader")
            trPr.append(hdr)
        for c_idx, value in enumerate(values):
            cell = row.cells[c_idx]
            cell.width = Twips(WIDTHS[c_idx])
            para = cell.paragraphs[0]
            pPr = para._p.get_or_add_pPr()
            _spacing(pPr, line=240, before=0)
            ind = OxmlElement("w:ind")
            ind.set(qn("w:firstLine"), "0")
            pPr.append(ind)
            run = para.add_run(value)
            run.font.size = Pt(CELL)
            if r_idx == 0:
                run.bold = True
    return tbl


def find_heading(doc, prefix):
    for p in doc.paragraphs:
        if p.style.name.startswith("Heading") and p.text.strip().startswith(prefix):
            return p
    raise SystemExit(f"heading not found: {prefix}")


def main():
    if not SRC.exists():
        raise SystemExit(f"missing pristine copy: {SRC}")
    doc = Document(str(SRC))
    body = doc.element.body

    start = find_heading(doc, "2.2 Overview")._p
    end = find_heading(doc, "2.3 ")._p

    # keep the transition paragraph (starts "Two transitions in the sequence")
    children = list(body.iterchildren())
    i0, i1 = children.index(start), children.index(end)
    section = children[i0 + 1:i1]
    transition = None
    for el in section:
        if el.tag == qn("w:p"):
            if Paragraph(el, doc).text.strip().startswith("Two transitions"):
                transition = el
                break
    if transition is None:
        raise SystemExit("transition paragraph not found")

    # removed material, reported for the log
    removed = [Paragraph(el, doc).text.strip()[:60] if el.tag == qn("w:p") else "<table>"
               for el in section]

    # detach the whole old section, then rebuild
    transition_copy = copy.deepcopy(transition)
    for el in section:
        body.remove(el)

    new_elements = [
        body_paragraph(doc, OVERVIEW),
        transition_copy,
        caption(doc, T1_CAPTION_NUM, T1_CAPTION_TXT),
        build_table(doc, T1_HEADER, T1_ROWS),
        note_paragraph(doc, T1_NOTE),
        caption(doc, T2_CAPTION_NUM, T2_CAPTION_TXT),
        build_table(doc, T1_HEADER, T2_ROWS),
        note_paragraph(doc, T2_NOTE),
    ]

    anchor = end
    for el in new_elements:
        anchor.addprevious(el)

    doc.save(str(DST))

    print(f"written: {DST}")
    print("removed from the old section:")
    for r in removed:
        print("   -", r)


if __name__ == "__main__":
    main()
