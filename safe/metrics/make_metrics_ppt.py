#!/usr/bin/env python3
"""Generate slide PPTX: 3 paper metrik SAFE AI (SSL & Transformer/LLM). Tema gelap, 16:9."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# ---- Palet warna ----
BG      = RGBColor(0x0A, 0x0F, 0x1C)   # slate-950
PANEL   = RGBColor(0x13, 0x1C, 0x31)   # slate panel
INDIGO  = RGBColor(0x81, 0x8C, 0xF8)   # indigo-400 (aksen utama)
INDIGO_L= RGBColor(0xC7, 0xD2, 0xFE)   # indigo-200
ROSE    = RGBColor(0xF4, 0x3F, 0x5E)   # Secure
EMERALD = RGBColor(0x34, 0xD3, 0x99)   # Fair
BLUE    = RGBColor(0x60, 0xA5, 0xFA)   # Accountable
AMBER   = RGBColor(0xFB, 0xBF, 0x24)   # Explainable
VIOLET  = RGBColor(0xC0, 0x84, 0xFC)
WHITE   = RGBColor(0xF1, 0xF5, 0xF9)   # slate-100
GREY    = RGBColor(0x94, 0xA3, 0xB8)   # slate-400
GREY_D  = RGBColor(0x64, 0x74, 0x8B)   # slate-500
LINE    = RGBColor(0x33, 0x41, 0x55)

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
SW, SH = prs.slide_width, prs.slide_height


def slide():
    s = prs.slides.add_slide(BLANK)
    bg = s.shapes.add_shape(1, 0, 0, SW, SH)
    bg.fill.solid(); bg.fill.fore_color.rgb = BG
    bg.line.fill.background()
    bg.shadow.inherit = False
    s.shapes._spTree.remove(bg._element); s.shapes._spTree.insert(2, bg._element)
    return s


def box(s, x, y, w, h, fill=None, line=None, line_w=1.0):
    sp = s.shapes.add_shape(1, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None:
        sp.fill.background()
    else:
        sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line; sp.line.width = Pt(line_w)
    sp.shadow.inherit = False
    return sp


def text(s, x, y, w, h, runs, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
         space_after=6, line_spacing=1.05):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    for i, para in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.space_after = Pt(space_after); p.line_spacing = line_spacing
        for (t, sz, col, bold) in para:
            r = p.add_run(); r.text = t
            r.font.size = Pt(sz); r.font.color.rgb = col; r.font.bold = bold
            r.font.name = 'Calibri'
    return tb


def chip(s, x, y, label, color=INDIGO, w=1.9):
    box(s, x, y, w, 0.42, fill=PANEL, line=color, line_w=1.25)
    text(s, x, y, w, 0.42, [[(label, 11, color, True)]],
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, space_after=0)


def header(s, kicker, title, color=INDIGO, kw=1.9):
    chip(s, 0.6, 0.5, kicker, color, w=kw)
    text(s, 0.6 + kw + 0.15, 0.46, 12.0 - kw, 0.7, [[(title, 26, WHITE, True)]],
         anchor=MSO_ANCHOR.MIDDLE)
    box(s, 0.6, 1.32, 12.13, 0.02, fill=LINE)


def safe_tag(s, x, y, letter, name, col):
    box(s, x, y, 0.42, 0.42, fill=PANEL, line=col, line_w=1.25)
    text(s, x, y, 0.42, 0.42, [[(letter, 14, col, True)]],
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, space_after=0)
    text(s, x + 0.5, y, 2.0, 0.42, [[(name, 12, col, True)]], anchor=MSO_ANCHOR.MIDDLE)


# ============================================================= 1. JUDUL
s = slide()
text(s, 0.6, 1.7, 12.1, 1.0, [[("METRIK SAFE AI", 50, INDIGO, True)]], align=PP_ALIGN.CENTER)
text(s, 0.6, 2.75, 12.1, 0.8,
     [[("Mengukur Secure, Accountable, Fair & Explainable", 24, WHITE, True)]],
     align=PP_ALIGN.CENTER)
text(s, 0.6, 3.5, 12.1, 0.6,
     [[("pada Self-Supervised Learning & Transformer/LLM", 18, INDIGO_L, True)]],
     align=PP_ALIGN.CENTER)
box(s, 5.4, 4.45, 2.5, 0.02, fill=INDIGO)
text(s, 0.6, 4.65, 12.1, 0.5,
     [[("Telaah 3 paper kunci  ·  Trend Terkini Kecerdasan Mesin", 14, GREY, False)]],
     align=PP_ALIGN.CENTER)
# tiga chip paper
xs = [1.7, 5.2, 8.7]
labs = [("SoFCLR (2024)", EMERALD), ("DecodingTrust (NeurIPS'23)", ROSE), ("HELM (TMLR'23)", BLUE)]
for x, (lab, col) in zip(xs, labs):
    chip(s, x, 5.5, lab, col, w=3.0)

# ============================================================= 2. KENAPA METRIK
s = slide()
header(s, "PENGANTAR", "Kenapa Butuh Metrik SAFE?")
text(s, 0.6, 1.55, 12.1, 0.9,
     [[("SAFE = ", 16, GREY, False), ("S", 16, ROSE, True), ("ecure  ·  ", 16, GREY, False),
       ("A", 16, BLUE, True), ("ccountable  ·  ", 16, GREY, False),
       ("F", 16, EMERALD, True), ("air  ·  ", 16, GREY, False),
       ("E", 16, AMBER, True), ("xplainable", 16, GREY, False),
       (".  Empat dimensi ini hanya bermakna jika bisa ", 16, GREY, False),
       ("diukur dengan angka", 16, INDIGO_L, True), (".", 16, GREY, False)]],
     line_spacing=1.2)
# 4 dimensi + contoh metrik
dims = [
    ("S", "Secure", ROSE, "Attack Success Rate (ASR),\ncertified accuracy, robust acc."),
    ("A", "Accountable", BLUE, "Audit trail, model card,\nethics & toxicity score."),
    ("F", "Fair", EMERALD, "Demographic parity,\nequalized odds, base-rate parity."),
    ("E", "Explainable", AMBER, "Faithfulness, plausibility,\nkorelasi dgn SHAP/LIME."),
]
x = 0.6
for (h, name, col, m) in dims:
    box(s, x, 2.7, 2.93, 2.6, fill=PANEL, line=col, line_w=1.5)
    text(s, x+0.25, 2.9, 2.5, 0.7, [[(h, 32, col, True)]])
    text(s, x+0.25, 3.6, 2.5, 0.4, [[(name, 15, WHITE, True)]])
    text(s, x+0.25, 4.1, 2.5, 1.1, [[(m, 12, GREY, False)]], line_spacing=1.25)
    x += 3.04
box(s, 0.6, 5.6, 12.13, 1.2, fill=PANEL, line=INDIGO, line_w=1.5)
text(s, 0.85, 5.7, 11.6, 1.0,
     [[("Masalahnya: ", 14, INDIGO_L, True),
       ("metrik klasik mengandaikan model dengan label dan output yang jelas. SSL belajar tanpa label, "
        "dan LLM mengeluarkan teks bebas. Ketiga paper berikut menjawab bagaimana cara mengukurnya.",
        14, WHITE, False)]],
     anchor=MSO_ANCHOR.MIDDLE)

# ============================================================= 3. PETA 3 PAPER
s = slide()
header(s, "PETA", "Tiga Paper yang Dipakai")
cards = [
    ("1", "SoFCLR", "SSL / Contrastive", EMERALD,
     "Qi, Hu, Lin & Yang\narXiv:2406.05686 · 2024",
     "Bagaimana mengukur & memperbaiki FAIRNESS pada representasi yang dipelajari tanpa label."),
    ("2", "DecodingTrust", "Transformer / GPT", ROSE,
     "Wang et al.\nNeurIPS 2023 (Outstanding)",
     "Benchmark 8 perspektif kepercayaan LLM: robustness, privasi, bias, fairness, etika."),
    ("3", "HELM", "Transformer / LLM", BLUE,
     "Liang, Bommasani, Lee et al.\nTMLR 2023",
     "Evaluasi holistik: 7 metrik diukur serempak pada 16 skenario inti."),
]
x = 0.6
for (n, name, para, col, meta, desc) in cards:
    box(s, x, 1.6, 3.93, 5.1, fill=PANEL, line=col, line_w=1.5)
    text(s, x+0.3, 1.8, 3.4, 0.7, [[(n, 30, col, True)]])
    text(s, x+0.3, 2.55, 3.4, 0.5, [[(name, 20, WHITE, True)]])
    chip(s, x+0.3, 3.15, para, col, w=2.6)
    text(s, x+0.3, 3.8, 3.4, 0.9, [[(meta, 12, GREY_D, False)]], line_spacing=1.25)
    box(s, x+0.3, 4.75, 3.33, 0.02, fill=LINE)
    text(s, x+0.3, 4.95, 3.4, 1.6, [[(desc, 13, GREY, False)]], line_spacing=1.3)
    x += 4.06

# ============================================================= 4. PAPER 1 - SoFCLR
s = slide()
header(s, "PAPER 1 · SSL", "SoFCLR: Fairness Tanpa Label", color=EMERALD)
text(s, 0.6, 1.45, 12.1, 0.55,
     [[("Provable Optimization for Adversarial Fair Self-supervised Contrastive Learning",
        14, EMERALD, True)]])
text(s, 0.6, 1.95, 12.1, 0.45,
     [[("Qi, Hu, Lin & Yang (2024) · arXiv:2406.05686", 12, GREY_D, False)]])
left = [
    ("Masalah", "Contrastive learning (SimCLR dll.) belajar dari data tanpa label. "
     "Representasinya bisa diam-diam menyandi bias (gender, ras). Fairness sulit diukur karena tidak ada label."),
    ("Ide", "Adversarial fair representation learning: minimkan contrastive loss pada data tak berlabel, "
     "sambil maksimalkan loss penebak atribut sensitif pada sedikit data berlabel (permainan minimax)."),
]
y = 2.6
for (t, b) in left:
    box(s, 0.6, y, 6.0, 1.85, fill=PANEL, line=LINE)
    text(s, 0.85, y+0.15, 5.5, 0.4, [[(t, 14, EMERALD, True)]])
    text(s, 0.85, y+0.65, 5.5, 1.1, [[(b, 12.5, GREY, False)]], line_spacing=1.25)
    y += 2.0
# kanan: metrik & hasil
box(s, 6.83, 2.6, 5.9, 1.85, fill=PANEL, line=EMERALD, line_w=1.5)
text(s, 7.08, 2.75, 5.4, 0.4, [[("Metrik (dimensi Fair)", 14, EMERALD, True)]])
text(s, 7.08, 3.25, 5.4, 1.1,
     [[("Dievaluasi dengan 8 notasi fairness pada klasifikasi downstream, mis. ", 12.5, GREY, False),
       ("demographic parity", 12.5, WHITE, True), (" & ", 12.5, GREY, False),
       ("equalized odds", 12.5, WHITE, True), (".", 12.5, GREY, False)]],
     line_spacing=1.25)
box(s, 6.83, 4.6, 5.9, 1.85, fill=PANEL, line=LINE)
text(s, 7.08, 4.75, 5.4, 0.4, [[("Kontribusi", 14, EMERALD, True)]])
text(s, 7.08, 5.25, 5.4, 1.1,
     [[("Algoritma stokastik dengan jaminan konvergensi ", 12.5, GREY, False),
       ("tanpa perlu batch besar", 12.5, WHITE, True),
       (", menyiasati global contrastive loss yang mahal.", 12.5, GREY, False)]],
     line_spacing=1.25)

# ============================================================= 5. PAPER 1 - ALGORITMA (OBJEKTIF)
s = slide()
header(s, "PAPER 1 · ALGORITMA", "Cara Kerja SoFCLR", color=EMERALD)
text(s, 0.6, 1.45, 12.1, 0.45,
     [[("SoFCLR = Stochastic Optimization for Fair Contrastive Learning", 13, GREY, False)]])
# fungsi objektif
box(s, 1.4, 2.0, 10.5, 1.2, fill=PANEL, line=EMERALD, line_w=1.5)
text(s, 1.4, 2.0, 10.5, 1.2,
     [[("F(w, w′)  =  F_GCL(w)  +  α · F_fair(w, w′)", 23, EMERALD, True)]],
     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
text(s, 0.6, 3.3, 12.1, 0.4,
     [[("minimalkan terhadap encoder w  ·  maksimalkan terhadap diskriminator w′  ·  "
        "α = bobot trade-off (fairness ↔ akurasi)", 12, GREY, False)]],
     align=PP_ALIGN.CENTER)
box(s, 0.6, 3.9, 6.0, 2.7, fill=PANEL, line=EMERALD, line_w=1.5)
text(s, 0.85, 4.05, 5.5, 0.4, [[("Suku F_GCL  (representasi)", 15, EMERALD, True)]])
text(s, 0.85, 4.6, 5.5, 1.9,
     [[("Global contrastive loss: tarik dua augmentasi gambar yang sama agar berdekatan, "
        "dorong menjauh dari semua sampel lain. Menjaga representasi tetap kaya dan informatif.",
        13, GREY, False)]], line_spacing=1.3)
box(s, 6.73, 3.9, 6.0, 2.7, fill=PANEL, line=ROSE, line_w=1.5)
text(s, 6.98, 4.05, 5.5, 0.4, [[("Suku F_fair  (fairness)", 15, ROSE, True)]])
text(s, 6.98, 4.6, 5.5, 1.9,
     [[("Diskriminator berusaha menebak atribut sensitif (mis. gender) dari representasi. "
        "Encoder dilatih agar diskriminator ", 13, GREY, False),
       ("gagal", 13, WHITE, True),
       (", sehingga representasi tidak membawa informasi sensitif.", 13, GREY, False)]],
     line_spacing=1.3)

# ============================================================= 6. PAPER 1 - ALGORITMA (LANGKAH)
s = slide()
header(s, "PAPER 1 · ALGORITMA", "SoFCLR per Iterasi", color=EMERALD)
box(s, 0.6, 1.6, 7.0, 5.05, fill=PANEL, line=EMERALD, line_w=1.5)
text(s, 0.9, 1.78, 6.4, 0.4, [[("Langkah tiap iterasi", 15, EMERALD, True)]])
steps = [
    ("1", "Ambil 1 batch data tak berlabel + 1 batch kecil yang berlabel atribut sensitif."),
    ("2", "Buat 2 augmentasi tiap sampel; perbarui moving-average u (estimator suku contrastive)."),
    ("3", "Hitung gradien dari nilai u, lalu haluskan dengan momentum."),
    ("4", "Encoder turun gradien:   w ← w − η · g"),
    ("5", "Diskriminator naik gradien:   w′ ← w′ + η′ · v"),
]
y = 2.3
for (n, b) in steps:
    text(s, 0.95, y, 0.5, 0.8, [[(n, 18, EMERALD, True)]], anchor=MSO_ANCHOR.TOP)
    text(s, 1.5, y, 5.85, 0.85, [[(b, 13, GREY, False)]], line_spacing=1.2)
    y += 0.84
box(s, 7.8, 1.6, 4.93, 2.45, fill=PANEL, line=LINE)
text(s, 8.05, 1.78, 4.4, 0.4, [[("Kenapa pakai moving-average u?", 14, WHITE, True)]])
text(s, 8.05, 2.3, 4.4, 1.6,
     [[("Minibatch untuk contrastive bersifat bias karena tiap anchor seharusnya dibandingkan "
        "dengan seluruh dataset. Vektor u melacak nilai itu lintas iterasi sehingga error "
        "mengecil, tanpa perlu batch raksasa seperti SimCLR.", 12.5, GREY, False)]], line_spacing=1.25)
box(s, 7.8, 4.2, 4.93, 2.45, fill=PANEL, line=EMERALD, line_w=1.5)
text(s, 8.05, 4.38, 4.4, 0.4, [[("Jaminan konvergensi", 14, EMERALD, True)]])
text(s, 8.05, 4.9, 4.4, 1.6,
     [[("Terbukti mencapai titik ε-stationary dalam O(ε⁻⁴) iterasi: setara SGD untuk "
        "optimisasi non-convex, dan tanpa syarat batch besar.", 12.5, GREY, False)]], line_spacing=1.25)

# ============================================================= 7. PAPER 1 - INTI (TANTANGAN)
s = slide()
header(s, "PAPER 1 · INTI", "Tantangan Khas Fairness di SSL", color=EMERALD)
pts = [
    ("Tanpa label downstream", "Fairness biasanya butuh label kelas + atribut sensitif. SSL pra-latih "
     "tanpa keduanya, jadi metrik fairness harus dirancang ulang untuk tahap representasi."),
    ("Optimisasi sulit", "Minimax-nya non-convex non-concave, diperberat global contrastive loss yang "
     "membandingkan tiap sampel dengan semua sampel lain. SoFCLR memberi solusi terbukti (provable)."),
    ("Bukan otomatis adil", "Penulis menegaskan SSL tidak inheren adil; pra-pelatihan tetap dapat "
     "menyandi bias bila tidak diberi sinyal fairness eksplisit."),
]
y = 1.7
for i, (t, b) in enumerate(pts, 1):
    box(s, 0.6, y, 12.13, 1.5, fill=PANEL, line=EMERALD if i == 1 else LINE,
        line_w=1.5 if i == 1 else 1)
    text(s, 0.9, y, 0.9, 1.5, [[(str(i), 34, EMERALD, True)]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, 1.9, y+0.2, 10.6, 1.1,
         [[(t, 16, WHITE, True)], [(b, 13, GREY, False)]], space_after=4, anchor=MSO_ANCHOR.MIDDLE)
    y += 1.65

# ============================================================= 8. PAPER 2 - DecodingTrust
s = slide()
header(s, "PAPER 2 · LLM", "DecodingTrust: 8 Perspektif", color=ROSE)
text(s, 0.6, 1.45, 12.1, 0.55,
     [[("A Comprehensive Assessment of Trustworthiness in GPT Models  ·  Wang et al., NeurIPS 2023",
        13, ROSE, True)]])
# 8 perspektif dipetakan ke SAFE
groups = [
    ("SECURE", ROSE, ["Adversarial robustness", "OOD robustness", "Adv. demonstrations", "Privacy"]),
    ("FAIR", EMERALD, ["Stereotype bias", "Fairness"]),
    ("ACCOUNTABLE", BLUE, ["Machine ethics", "Toxicity"]),
]
x = 0.6
ws = [5.5, 3.3, 3.33]
for (gname, col, items), w in zip(groups, ws):
    box(s, x, 2.1, w, 2.5, fill=PANEL, line=col, line_w=1.5)
    text(s, x+0.25, 2.25, w-0.5, 0.4, [[(gname, 13, col, True)]])
    yy = 2.8
    for it in items:
        box(s, x+0.25, yy, 0.12, 0.32, fill=col)
        text(s, x+0.5, yy, w-0.8, 0.4, [[(it, 13, WHITE, False)]], anchor=MSO_ANCHOR.MIDDLE)
        yy += 0.45
    x += w + 0.13
box(s, 0.6, 4.85, 12.13, 1.85, fill=PANEL, line=ROSE, line_w=1.5)
text(s, 0.85, 5.0, 11.6, 1.6,
     [[("Metrik konkret.  ", 14, ROSE, True),
       ("Robustness diuji dengan benchmark AdvGLUE / AdvGLUE++ (serangan TextFooler, SemAttack, "
        "BERT-ATTACK). Attack Success Rate mencapai 89,2% pada GPT-4 (kasus transfer terbaik). ",
        13.5, WHITE, False)],
      [("Fairness diukur lewat base-rate parity antar kelompok demografi, dan menemukan trade-off "
        "akurasi-fairness: GPT-4 lebih akurat pada data seimbang, tapi lebih tidak adil pada data timpang.",
        13.5, GREY, False)]],
     anchor=MSO_ANCHOR.MIDDLE, space_after=6, line_spacing=1.2)

# ============================================================= 9. PAPER 3 - HELM
s = slide()
header(s, "PAPER 3 · LLM", "HELM: Evaluasi Holistik", color=BLUE)
text(s, 0.6, 1.45, 12.1, 0.55,
     [[("Holistic Evaluation of Language Models  ·  Liang, Bommasani, Lee et al., TMLR 2023",
        13, BLUE, True)]])
text(s, 0.6, 1.95, 12.1, 0.5,
     [[("Gagasan inti: ukur ", 13, GREY, False), ("banyak metrik sekaligus", 13, WHITE, True),
       (" untuk tiap skenario, bukan hanya akurasi. 98 dari 112 pasangan terukur (87,5%).",
        13, GREY, False)]])
# 7 metrik sebagai chip
metrics = [("Accuracy", GREY), ("Calibration", GREY), ("Robustness", ROSE),
           ("Fairness", EMERALD), ("Bias", EMERALD), ("Toxicity", BLUE), ("Efficiency", GREY)]
x = 0.6
for (m, col) in metrics:
    chip(s, x, 2.65, m, col, w=1.66)
    x += 1.74
text(s, 0.6, 3.25, 12.1, 0.4,
     [[("16 skenario inti  ×  7 metrik  ·  warna = dimensi SAFE terkait", 11, GREY_D, False)]])
# dua kotak: robustness & fairness operasionalisasi
box(s, 0.6, 3.85, 6.0, 2.7, fill=PANEL, line=ROSE, line_w=1.5)
text(s, 0.85, 4.0, 5.5, 0.4, [[("Robustness (Secure)", 15, ROSE, True)]])
text(s, 0.85, 4.55, 5.5, 1.9,
     [[("Performa worst-case atas transformasi ringan (mis. typo). Dua sifat: ", 13, GREY, False),
       ("invariance", 13, WHITE, True), (" (output tak berubah) & ", 13, GREY, False),
       ("equivariance", 13, WHITE, True), (" (output berubah sesuai), menangkap robustness lokal "
        "di sekitar tiap input.", 13, GREY, False)]],
     line_spacing=1.3)
box(s, 6.73, 3.85, 6.0, 2.7, fill=PANEL, line=EMERALD, line_w=1.5)
text(s, 6.98, 4.0, 5.5, 0.4, [[("Fairness (Fair)", 15, EMERALD, True)]])
text(s, 6.98, 4.55, 5.5, 1.9,
     [[("Diukur lewat perturbasi: ubah dialek (SAE→AAE) dan tukar istilah gender, lalu lihat "
        "worst-case accuracy. Dipakai karena ", 13, GREY, False),
       ("metadata demografi sering tak tersedia", 13, WHITE, True),
       ("; disparitas langsung diukur bila metadata ada.", 13, GREY, False)]],
     line_spacing=1.3)

# ============================================================= 10. SINTESIS MATRIKS
s = slide()
header(s, "SINTESIS", "Peta 3 Paper × 4 Dimensi SAFE")
# header kolom
cols = [("PAPER", 3.6, GREY), ("Secure", 2.1, ROSE), ("Accountable", 2.3, BLUE),
        ("Fair", 2.0, EMERALD), ("Explainable", 2.1, AMBER)]
x = 0.6
positions = []
for (c, w, col) in cols:
    box(s, x, 1.6, w, 0.55, fill=RGBColor(0x1E, 0x29, 0x3B))
    text(s, x, 1.6, w, 0.55, [[(c, 12, col, True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    positions.append((x, w))
    x += w + 0.05
matrix = [
    ("SoFCLR (SSL)", EMERALD, ["–", "–", "8 notasi", "(parsial)"]),
    ("DecodingTrust (LLM)", ROSE, ["AdvGLUE++ ASR", "etika+toxic", "base-rate", "–"]),
    ("HELM (LLM)", BLUE, ["worst-case", "toxic+calib", "perturbasi", "–"]),
]
y = 2.2
for (name, ncol, vals) in matrix:
    box(s, positions[0][0], y, positions[0][1], 0.7, fill=PANEL, line=LINE)
    text(s, positions[0][0]+0.15, y, positions[0][1]-0.2, 0.7, [[(name, 12.5, ncol, True)]],
         anchor=MSO_ANCHOR.MIDDLE)
    for (val, (px, pw)) in zip(vals, positions[1:]):
        filled = val not in ("–",)
        box(s, px, y, pw, 0.7, fill=PANEL, line=LINE)
        col = WHITE if filled else GREY_D
        text(s, px, y, pw, 0.7, [[(val, 11.5, col, filled)]],
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    y += 0.78
box(s, 0.6, 4.85, 12.13, 1.85, fill=PANEL, line=AMBER, line_w=1.5)
text(s, 0.85, 5.0, 11.6, 1.6,
     [[("Yang belum tertutup.  ", 14, AMBER, True),
       ("Explainable dan Accountable masih lemah: hanya diproksikan lewat etika/toxicity, "
        "belum ada metrik audit-trail / model-card yang baku. ", 13.5, WHITE, False)],
      [("AutoML tidak punya satu pun paper metrik SAFE yang lolos verifikasi. Ini gap riset nyata, "
        "bukan sekadar belum sempat dicari.", 13.5, GREY, False)]],
     anchor=MSO_ANCHOR.MIDDLE, space_after=6, line_spacing=1.2)

# ============================================================= 11. KESIMPULAN
s = slide()
header(s, "PENUTUP", "Tiga Pelajaran", color=INDIGO)
takeaways = [
    ("Metrik mengikuti paradigma", "Tiap arsitektur butuh metrik yang disesuaikan: SSL diukur di tahap "
     "representasi (tanpa label), LLM diukur lewat benchmark perilaku output."),
    ("Benchmark menyatukan dimensi", "DecodingTrust & HELM menunjukkan SAFE bisa diukur serempak dalam "
     "satu kerangka, bukan empat pengujian terpisah."),
    ("Selalu ada trade-off", "Akurasi vs fairness, robustness vs efisiensi. Metrik yang baik justru "
     "membuat trade-off itu terlihat dan bisa dikelola."),
]
y = 1.8
for i, (t, b) in enumerate(takeaways, 1):
    box(s, 0.6, y, 12.13, 1.25, fill=PANEL, line=INDIGO, line_w=1.25)
    text(s, 0.9, y, 1.0, 1.25, [[(str(i), 36, INDIGO, True)]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, 2.0, y+0.15, 10.5, 1.0,
         [[(t, 17, WHITE, True)], [(b, 13.5, GREY, False)]], space_after=3, anchor=MSO_ANCHOR.MIDDLE)
    y += 1.45
text(s, 0.6, 6.55, 12.1, 0.5,
     [[("Ketiga paper menyediakan metrik yang bisa langsung dipakai untuk menguji SAFE pada model nyata.",
        14, INDIGO_L, True)]],
     align=PP_ALIGN.CENTER)

# ============================================================= 12. REFERENSI
s = slide()
header(s, "REFERENSI", "3 Paper")
refs = [
    ("[1]", "Provable Optimization for Adversarial Fair Self-supervised Contrastive Learning",
     "Qi, Hu, Lin & Yang · 2024 · arXiv:2406.05686", EMERALD,
     "Paradigma SSL, dimensi Fairness. Metrik: 8 notasi fairness; metode minimax adversarial."),
    ("[2]", "DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models",
     "Wang et al. · NeurIPS 2023 (Outstanding Paper) · arXiv:2306.11698", ROSE,
     "LLM, dimensi Secure/Fair/Accountable. 8 perspektif; AdvGLUE++ ASR hingga 89,2%."),
    ("[3]", "Holistic Evaluation of Language Models (HELM)",
     "Liang, Bommasani, Lee et al. · TMLR 2023 · arXiv:2211.09110", BLUE,
     "LLM, evaluasi multi-metrik. 7 metrik × 16 skenario; robustness & fairness worst-case."),
]
y = 1.7
for (n, t, meta, col, why) in refs:
    box(s, 0.6, y, 12.13, 1.5, fill=PANEL, line=LINE)
    box(s, 0.6, y, 0.08, 1.5, fill=col)
    text(s, 0.85, y, 1.0, 1.5, [[(n, 22, col, True)]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, 1.8, y+0.15, 10.7, 1.25,
         [[(t, 15, WHITE, True)],
          [(meta, 12, INDIGO_L, False)],
          [(why, 12, GREY, False)]], space_after=3)
    y += 1.65

prs.save("/home/adb/awangga/awangga.github.io/safe/metrics/SAFE-AI-Metrics.pptx")
print("Saved SAFE-AI-Metrics.pptx  |  slides:", len(prs.slides._sldIdLst))
