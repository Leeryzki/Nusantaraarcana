"""
🔮 NUSANTARA ARCANA — Petualangan Informatika Kelas 7 (SMP)
Materi : Analisis Data • Algoritma & Pemrograman • Pengenalan AI
Jalankan: streamlit run app.py
"""

import random
import statistics
from collections import Counter

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Nusantara Arcana • Petualangan Informatika",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ════════════════════════════════════════════════════════════════
#  TEMA: PETUALANGAN & MAGICAL MYSTERY
# ════════════════════════════════════════════════════════════════
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;800&family=Nunito:wght@400;600;800&display=swap');

html, body, [class*="css"], .stApp { font-family: 'Nunito', sans-serif; }

.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(168,85,247,.28) 0, transparent 40%),
        radial-gradient(circle at 85% 20%, rgba(251,191,36,.12) 0, transparent 35%),
        radial-gradient(circle at 50% 100%, rgba(14,165,233,.18) 0, transparent 45%),
        linear-gradient(160deg, #0b0720 0%, #150d33 45%, #0a1230 100%);
    color: #ede9fe;
}
/* bintang berkelip */
.stApp::before {
    content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 0;
    background-image:
        radial-gradient(2px 2px at 20px 30px, #fff, transparent),
        radial-gradient(1.5px 1.5px at 120px 80px, #fde68a, transparent),
        radial-gradient(2px 2px at 220px 160px, #c4b5fd, transparent),
        radial-gradient(1.5px 1.5px at 330px 40px, #fff, transparent),
        radial-gradient(2px 2px at 420px 120px, #a5f3fc, transparent);
    background-size: 460px 220px; opacity: .55;
    animation: twinkle 5s ease-in-out infinite alternate;
}
@keyframes twinkle { from {opacity:.25} to {opacity:.7} }
@keyframes floaty { 0%,100% {transform: translateY(0)} 50% {transform: translateY(-8px)} }
@keyframes glow { 0%,100% {box-shadow:0 0 12px rgba(251,191,36,.25)} 50% {box-shadow:0 0 28px rgba(251,191,36,.55)} }

h1, h2, h3, h4 { font-family: 'Cinzel', serif !important; color: #fde68a !important; letter-spacing: .5px; }
.stMarkdown p, .stMarkdown li, label p, .stCaption, [data-testid="stWidgetLabel"] p { color: #ede9fe !important; }

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a1040 0%, #0d0a28 100%);
    border-right: 1px solid rgba(253,230,138,.25);
}
[data-testid="stHeader"] { background: transparent; }

.hero {
    text-align: center; padding: 34px 20px; border-radius: 26px; margin-bottom: 22px;
    background: linear-gradient(135deg, rgba(124,58,237,.45), rgba(14,165,233,.25));
    border: 1px solid rgba(253,230,138,.4);
    box-shadow: 0 0 40px rgba(124,58,237,.35);
}
.hero .orb { font-size: 64px; display:inline-block; animation: floaty 3.5s ease-in-out infinite; }
.hero h1 { font-size: 2.5rem; margin: 6px 0 4px; text-shadow: 0 0 18px rgba(253,230,138,.6); }
.hero p { font-size: 1.05rem; color: #ddd6fe !important; margin: 0; }

.card {
    background: linear-gradient(145deg, rgba(30,20,70,.85), rgba(15,12,45,.85));
    border: 1px solid rgba(167,139,250,.35); border-radius: 20px;
    padding: 18px 22px; margin: 10px 0;
    box-shadow: 0 6px 24px rgba(0,0,0,.35);
}
.card h4 { margin-top: 0; }
.scroll {
    background: linear-gradient(145deg, #2a1b52, #1b1240);
    border-left: 5px solid #fbbf24; border-radius: 14px; padding: 14px 18px; margin: 12px 0;
}
.tip {
    background: rgba(16,185,129,.12); border: 1px dashed #34d399; border-radius: 14px;
    padding: 12px 16px; margin: 10px 0;
}
.stat {
    text-align: center; padding: 16px; border-radius: 18px;
    background: rgba(124,58,237,.25); border: 1px solid rgba(253,230,138,.35);
}
.stat .n { font-family:'Cinzel',serif; font-size: 2rem; color:#fde68a; font-weight:800; }
.stat .l { font-size:.85rem; color:#c4b5fd; }

.lvl {
    border-radius: 18px; padding: 14px; text-align:center; margin-bottom: 6px;
    background: rgba(20,14,55,.9); border: 2px solid var(--c);
    box-shadow: 0 0 16px color-mix(in srgb, var(--c) 45%, transparent);
}
.lvl .ic { font-size: 34px; }
.lvl .nm { font-family:'Cinzel',serif; font-weight:800; color: var(--c); font-size: 1.05rem; }
.lvl .ds { font-size:.78rem; color:#c4b5fd; }
.lvl.locked { filter: grayscale(1) brightness(.6); box-shadow:none; }

.qbox {
    border-radius: 16px; padding: 14px 18px; margin: 12px 0 4px;
    background: rgba(30,20,70,.8); border: 1px solid rgba(167,139,250,.4);
}
.ok  { border-left: 6px solid #34d399; background: rgba(16,185,129,.12); border-radius: 12px; padding: 10px 14px; margin: 8px 0; }
.bad { border-left: 6px solid #fb7185; background: rgba(244,63,94,.12);  border-radius: 12px; padding: 10px 14px; margin: 8px 0; }

.badge {
    display:inline-block; padding: 6px 14px; margin: 4px; border-radius: 999px;
    background: linear-gradient(90deg,#f59e0b,#fde047); color:#2b1b00; font-weight:800;
    animation: glow 3s ease-in-out infinite;
}
.badge.off { background:#2a2350; color:#7c74a8; animation:none; }

.stButton > button, .stFormSubmitButton > button {
    background: linear-gradient(90deg,#7c3aed,#a855f7,#ec4899); color: white; font-weight: 800;
    border: 1px solid rgba(253,230,138,.5); border-radius: 14px; padding: .55rem 1.2rem;
    transition: all .2s ease;
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
    transform: translateY(-2px) scale(1.02); box-shadow: 0 0 22px rgba(236,72,153,.6); color:#fff;
}
.stButton > button:disabled { background:#2a2350; color:#7c74a8; border-color:#3b3470; }
[data-testid="stTabs"] button { font-weight: 800; }
.stProgress > div > div > div { background: linear-gradient(90deg,#fbbf24,#f472b6,#a855f7) !important; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def H(html: str):
    st.markdown(html, unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  DATA LEVEL & BANK SOAL
# ════════════════════════════════════════════════════════════════
LEVELS = [
    {"name": "Beginner", "icon": "🌱", "color": "#7cfc9a", "desc": "Gerbang Hutan Awal"},
    {"name": "Normal", "icon": "🧭", "color": "#5eead4", "desc": "Jalan Setapak Kompas"},
    {"name": "Medium", "icon": "🗺️", "color": "#60a5fa", "desc": "Peta Kuno Lembah"},
    {"name": "Hard", "icon": "⚔️", "color": "#a78bfa", "desc": "Benteng Batu Rune"},
    {"name": "Master", "icon": "🔮", "color": "#e879f9", "desc": "Menara Kristal"},
    {"name": "Grandmaster", "icon": "🐉", "color": "#fb7185", "desc": "Sarang Naga Algoritma"},
    {"name": "Legend", "icon": "👑", "color": "#fbbf24", "desc": "Singgasana Raja Data"},
    {"name": "Mythical", "icon": "🌌", "color": "#f0abfc", "desc": "Gerbang Semesta Misteri"},
]
PASS_MIN = 3  # minimal benar (dari 5) untuk membuka level berikutnya


def Q(q, options, answer, why, code=None):
    return {"q": q, "options": options, "answer": answer, "why": why, "code": code}


QUESTIONS = {
    0: [
        Q("Kumpulan fakta atau keterangan mentah yang belum diolah disebut …",
          ["Data", "Program", "Algoritma", "Robot"], "Data",
          "Data adalah fakta mentah. Setelah diolah, data menjadi informasi."),
        Q("Fungsi Python yang dipakai untuk menampilkan tulisan ke layar adalah …",
          ["print()", "input()", "len()", "range()"], "print()",
          "print() menampilkan keluaran (output) ke layar."),
        Q("AI adalah singkatan dari …",
          ["Artificial Intelligence", "Automatic Internet", "Active Input", "Advanced Interface"],
          "Artificial Intelligence", "AI = Artificial Intelligence atau kecerdasan buatan."),
        Q("Langkah-langkah berurutan untuk menyelesaikan suatu masalah disebut …",
          ["Algoritma", "Variabel", "Grafik", "Sensor"], "Algoritma",
          "Algoritma adalah urutan langkah logis untuk menyelesaikan masalah."),
        Q("Tipe data dari \"Halo\" di Python adalah …",
          ["str (string)", "int", "float", "bool"], "str (string)",
          "Teks yang diapit tanda kutip bertipe str."),
    ],
    1: [
        Q("Rata-rata dari 4, 6, 8, dan 10 adalah …",
          ["7", "6", "8", "28"], "7", "(4+6+8+10) : 4 = 28 : 4 = 7."),
        Q("Manakah contoh penerapan AI dalam kehidupan sehari-hari?",
          ["Asisten suara di ponsel", "Kipas angin biasa", "Penggaris", "Lampu senter"],
          "Asisten suara di ponsel", "Asisten suara memahami ucapan manusia, itu penerapan AI."),
        Q("Tanda untuk membuat komentar satu baris di Python adalah …",
          ["#", "//", "/* */", "--"], "#", "Python memakai # untuk komentar."),
        Q("Pada diagram alir (flowchart), bentuk belah ketupat menandakan …",
          ["Keputusan (percabangan)", "Mulai/Selesai", "Proses", "Keluaran"],
          "Keputusan (percabangan)", "Belah ketupat dipakai untuk pertanyaan Ya/Tidak."),
        Q("Hasil kode berikut adalah …", ["7", "5", "2", "x"], "7",
          "x awalnya 5, lalu x = 5 + 2 = 7.", code="x = 5\nx = x + 2\nprint(x)"),
    ],
    2: [
        Q("Median dari data 3, 9, 1, 7, 5 adalah …",
          ["5", "7", "1", "9"], "5", "Urutkan: 1, 3, 5, 7, 9. Nilai tengahnya 5."),
        Q("Perulangan sebanyak 5 kali di Python ditulis …",
          ["for i in range(5):", "if i == 5:", "print(5)", "def i(5):"],
          "for i in range(5):", "for + range(5) mengulang 5 kali (0 sampai 4)."),
        Q("Machine learning adalah cabang AI di mana komputer …",
          ["Belajar pola dari data", "Dimatikan otomatis", "Hanya menyimpan file", "Dikendalikan sepenuhnya manusia"],
          "Belajar pola dari data", "Machine learning belajar dari contoh data tanpa diprogram satu per satu."),
        Q("Manakah yang termasuk data kualitatif?",
          ["Warna baju favorit", "Tinggi badan", "Jumlah buku", "Suhu udara"],
          "Warna baju favorit", "Data kualitatif berupa kategori atau deskripsi, bukan angka."),
        Q("Hasil kode berikut adalah …", ["4", "3", "10", "[1,2,3,4]"], "4",
          "len() menghitung jumlah elemen dalam list.", code="print(len([1, 2, 3, 4]))"),
    ],
    3: [
        Q("Modus dari data 2, 3, 3, 5, 7, 3, 5 adalah …",
          ["3", "5", "2", "7"], "3", "Angka 3 muncul paling sering (3 kali)."),
        Q("Hasil kode berikut adalah …", ["1", "3", "0", "3.33"], "1",
          "Operator % menghasilkan sisa bagi. 10 dibagi 3 bersisa 1.", code="print(10 % 3)"),
        Q("Urutan yang tepat dalam analisis data adalah …",
          ["Kumpulkan → bersihkan → analisis → simpulkan",
           "Simpulkan → analisis → kumpulkan → bersihkan",
           "Bersihkan → simpulkan → kumpulkan → analisis",
           "Analisis → kumpulkan → simpulkan → bersihkan"],
          "Kumpulkan → bersihkan → analisis → simpulkan",
          "Data harus dikumpulkan dan dibersihkan dulu sebelum dianalisis."),
        Q("Bias pada AI umumnya muncul karena …",
          ["Data latih yang tidak seimbang", "Layar yang terlalu terang", "Baterai lemah", "Kabel terlalu panjang"],
          "Data latih yang tidak seimbang", "AI meniru pola dari data. Data berat sebelah menghasilkan keputusan berat sebelah."),
        Q("Jika nilai = 70, apa keluaran kode berikut?", ["Remedial", "Lulus", "Error", "70"], "Remedial",
          "70 tidak memenuhi syarat nilai >= 75, jadi cabang else yang berjalan.",
          code="nilai = 70\nif nilai >= 75:\n    print('Lulus')\nelse:\n    print('Remedial')"),
    ],
    4: [
        Q("Keluaran kode berikut adalah …", ["2 4 6 (tiap angka baris baru)", "1 2 3", "2 4 6 8", "6"],
          "2 4 6 (tiap angka baris baru)", "i bernilai 1, 2, 3 sehingga i*2 menghasilkan 2, 4, 6.",
          code="for i in range(1, 4):\n    print(i * 2)"),
        Q("Grafik yang paling cocok untuk menunjukkan perubahan suhu tiap jam adalah …",
          ["Grafik garis", "Grafik lingkaran", "Tabel warna", "Gambar peta"], "Grafik garis",
          "Grafik garis memperlihatkan tren dari waktu ke waktu."),
        Q("Cara mencari nilai terbesar dalam sebuah list secara algoritmik adalah …",
          ["Simpan nilai maksimum sementara lalu bandingkan satu per satu",
           "Ambil nilai pertama saja", "Jumlahkan semua nilai", "Acak urutan list"],
          "Simpan nilai maksimum sementara lalu bandingkan satu per satu",
          "Bandingkan setiap elemen dengan maksimum sementara dan perbarui jika lebih besar."),
        Q("Pada supervised learning, data yang dipakai berupa …",
          ["Data berlabel (ada jawaban benar)", "Data tanpa isi", "Data rahasia saja", "Data gambar saja"],
          "Data berlabel (ada jawaban benar)", "Model belajar dari contoh yang sudah diberi label."),
        Q("Keluaran kode berikut adalah …", ["6.0", "18", "6", "3"], "6.0",
          "sum = 18, len = 3, 18/3 = 6.0 (pembagian / selalu menghasilkan float).",
          code="data = [4, 8, 6]\nprint(sum(data) / len(data))"),
    ],
    5: [
        Q("Keluaran kode berikut adalah …", ["6", "12", "2", "9"], "6",
          "Hanya i genap (2 dan 4) yang dijumlahkan: 2 + 4 = 6.",
          code="total = 0\nfor i in range(1, 6):\n    if i % 2 == 0:\n        total += i\nprint(total)"),
        Q("Outlier dalam data adalah …",
          ["Nilai yang sangat berbeda jauh dari data lainnya", "Nilai rata-rata", "Data yang hilang total", "Nama kolom"],
          "Nilai yang sangat berbeda jauh dari data lainnya",
          "Outlier bisa memengaruhi rata-rata dan perlu dicek apakah itu kesalahan atau data asli."),
        Q("Bubble sort pada [3, 1, 2]: hasil setelah putaran pertama adalah …",
          ["[1, 2, 3]", "[3, 1, 2]", "[1, 3, 2]", "[2, 1, 3]"], "[1, 2, 3]",
          "Bandingkan 3 dan 1 lalu tukar → [1,3,2]. Bandingkan 3 dan 2 lalu tukar → [1,2,3]."),
        Q("Teknologi AI yang membuat chatbot memahami bahasa manusia disebut …",
          ["Natural Language Processing (NLP)", "Hardware Driver", "Defragmentasi", "Overclocking"],
          "Natural Language Processing (NLP)", "NLP mengolah dan memahami bahasa manusia."),
        Q("Kode yang benar untuk menghitung banyaknya bilangan genap di list angka adalah …",
          ["jml = 0\nfor a in angka:\n    if a % 2 == 0:\n        jml += 1",
           "jml = 0\nfor a in angka:\n    if a / 2 == 0:\n        jml += 1",
           "jml = 0\nfor a in angka:\n    jml = a % 2",
           "jml = len(angka) % 2"],
          "jml = 0\nfor a in angka:\n    if a % 2 == 0:\n        jml += 1",
          "Bilangan genap bersisa 0 jika dibagi 2 (a % 2 == 0), lalu tambah penghitung."),
    ],
    6: [
        Q("Binary search pada 1.000 data terurut membutuhkan paling banyak sekitar … langkah.",
          ["10", "500", "1.000", "100"], "10",
          "Tiap langkah membuang separuh data. log₂(1000) ≈ 10."),
        Q("Keluaran kode berikut adalah …", ["16", "4", "8", "2"], "16",
          "f(2) = 4, lalu f(4) = 16.",
          code="def f(n):\n    return n * n\n\nprint(f(f(2)))"),
        Q("Overfitting terjadi ketika model …",
          ["Sangat bagus pada data latih tetapi buruk pada data baru",
           "Tidak pernah dilatih", "Selalu menebak acak", "Terlalu kecil ukuran filenya"],
          "Sangat bagus pada data latih tetapi buruk pada data baru",
          "Model terlalu menghafal data latih sehingga gagal menggeneralisasi."),
        Q("Tindakan yang paling etis dalam menggunakan data untuk melatih AI adalah …",
          ["Meminta izin dan melindungi data pribadi", "Mengambil foto siapa saja tanpa izin",
           "Menjual data teman", "Menyebarkan data sekolah"],
          "Meminta izin dan melindungi data pribadi", "Privasi dan persetujuan adalah dasar etika data."),
        Q("Keluaran kode berikut adalah …", ["c", "a", "b", "Error"], "c",
          "Indeks -1 mengambil elemen terakhir dari list.",
          code="kata = ['a', 'b', 'c']\nprint(kata[-1])"),
    ],
    7: [
        Q("Keluaran kode berikut adalah …", ["12", "9", "10", "13"], "12",
          "i: 0 → 3 → 6 → 9 → 12. Saat i = 12, syarat i < 10 salah dan perulangan berhenti.",
          code="i = 0\nwhile i < 10:\n    i += 3\nprint(i)"),
        Q("Dari 100 siswa, 90 lulus. Model AI selalu menebak \"lulus\" dan akurasinya 90%. Kesimpulan terbaik adalah …",
          ["Akurasi tinggi menyesatkan karena data tidak seimbang dan model tidak benar-benar belajar",
           "Model sempurna", "Model pasti salah semua", "Data harus dihapus"],
          "Akurasi tinggi menyesatkan karena data tidak seimbang dan model tidak benar-benar belajar",
          "Model tidak pernah mampu mengenali siswa yang tidak lulus."),
        Q("Keluaran kode berikut adalah …",
          ["[1, 4, 9, 16]", "[1, 2, 3, 4]", "[2, 4, 6, 8]", "[1, 4, 9]"], "[1, 4, 9, 16]",
          "List comprehension mengkuadratkan 1 sampai 4.",
          code="print([x * x for x in range(1, 5)])"),
        Q("Nilai dari fakt(4) pada kode berikut adalah …", ["24", "10", "12", "16"], "24",
          "Rekursi: 4×3×2×1 = 24.",
          code="def fakt(n):\n    return 1 if n <= 1 else n * fakt(n - 1)\n\nprint(fakt(4))"),
        Q("Mengapa data uji harus dipisah dari data latih?",
          ["Agar kemampuan model pada data baru dapat diukur dengan jujur",
           "Agar file lebih kecil", "Agar model lebih cepat dilatih", "Agar data latih bertambah"],
          "Agar kemampuan model pada data baru dapat diukur dengan jujur",
          "Seperti ujian: soalnya tidak boleh sama dengan soal latihan."),
    ],
}

RANKS = [
    (0, "Pengembara Baru"), (100, "Pencari Jejak"), (300, "Penjelajah Hutan"),
    (600, "Penyihir Muda"), (1000, "Ksatria Kode"), (1500, "Penakluk Naga"),
    (2200, "Raja Data"), (3000, "Arsitek Semesta"),
]


# ════════════════════════════════════════════════════════════════
#  STATE
# ════════════════════════════════════════════════════════════════
def init_state():
    ss = st.session_state
    ss.setdefault("page", "🏰 Beranda")
    ss.setdefault("xp", 0)
    ss.setdefault("best", {})          # level -> skor terbaik
    ss.setdefault("read", set())       # materi yang selesai dibaca
    ss.setdefault("sel_level", None)
    ss.setdefault("attempt", 0)
    ss.setdefault("result", None)
    ss.setdefault("perm", {})


def go(page):
    st.session_state.page = page


def unlocked(i):
    return i == 0 or st.session_state.best.get(i - 1, -1) >= PASS_MIN


def rank_name():
    xp = st.session_state.xp
    name = RANKS[0][1]
    for need, n in RANKS:
        if xp >= need:
            name = n
    return name


def max_xp():
    return sum((i + 1) * 10 * 5 for i in range(len(LEVELS))) + 60


def parse_nums(text):
    out = []
    for p in text.replace(";", ",").replace(" ", ",").split(","):
        p = p.strip()
        if p:
            out.append(float(p))
    return out


init_state()

# ════════════════════════════════════════════════════════════════
#  SIDEBAR
# ════════════════════════════════════════════════════════════════
PAGES = ["🏰 Beranda", "📜 Gulungan Materi", "⚔️ Arena Kuis", "🏆 Jurnal Petualang"]

with st.sidebar:
    H("<div style='text-align:center;font-size:54px;animation:floaty 3.5s ease-in-out infinite'>🔮</div>")
    H("<h3 style='text-align:center;margin-top:0'>Nusantara Arcana</h3>")
    st.radio("Navigasi", PAGES, key="page", label_visibility="collapsed")
    st.divider()
    st.markdown(f"**Gelar:** {rank_name()}")
    st.markdown(f"**✨ XP:** {st.session_state.xp}")
    st.progress(min(st.session_state.xp / max_xp(), 1.0))
    st.caption(f"Level lulus: {sum(1 for v in st.session_state.best.values() if v >= PASS_MIN)}/{len(LEVELS)}")

page = st.session_state.page


# ════════════════════════════════════════════════════════════════
#  HALAMAN: BERANDA
# ════════════════════════════════════════════════════════════════
def page_home():
    H("""
<div class="hero">
  <div class="orb">🔮</div>
  <h1>Nusantara Arcana</h1>
  <p>Petualangan Informatika di negeri penuh misteri. Pelajari sihir <b>Data</b>, <b>Algoritma</b>,
  dan <b>Kecerdasan Buatan</b>, lalu taklukkan 8 level kuis untuk menjadi legenda!</p>
</div>""")
    c1, c2, c3, c4 = st.columns(4)
    lulus = sum(1 for v in st.session_state.best.values() if v >= PASS_MIN)
    for col, n, l in [
        (c1, st.session_state.xp, "✨ Total XP"),
        (c2, rank_name(), "🎖️ Gelar"),
        (c3, f"{len(st.session_state.read)}/3", "📜 Materi Selesai"),
        (c4, f"{lulus}/8", "⚔️ Level Lulus"),
    ]:
        col.markdown(f'<div class="stat"><div class="n" style="font-size:{"1.2rem" if isinstance(n, str) and len(n) > 6 else "2rem"}">{n}</div><div class="l">{l}</div></div>',
                     unsafe_allow_html=True)

    st.markdown("### 🗺️ Peta Petualangan")
    cols = st.columns(4)
    for i, lv in enumerate(LEVELS):
        lock = "" if unlocked(i) else " locked"
        status = "🔒 Terkunci" if not unlocked(i) else (
            f"✅ Skor {st.session_state.best[i]}/5" if i in st.session_state.best else "⚔️ Siap ditempuh")
        cols[i % 4].markdown(
            f'<div class="lvl{lock}" style="--c:{lv["color"]}"><div class="ic">{lv["icon"]}</div>'
            f'<div class="nm">{lv["name"]}</div><div class="ds">{lv["desc"]}</div>'
            f'<div class="ds" style="margin-top:6px">{status}</div></div>',
            unsafe_allow_html=True)

    st.markdown("### 🧙 Cara Bermain")
    H("""
<div class="card">
<b>1.</b> Buka <b>📜 Gulungan Materi</b> dan baca 3 bab sihir, lengkap dengan percobaan interaktif.<br>
<b>2.</b> Masuk ke <b>⚔️ Arena Kuis</b> dan mulai dari level <i>Beginner</i>.<br>
<b>3.</b> Jawab 5 soal. Benar minimal <b>3</b> untuk membuka level berikutnya.<br>
<b>4.</b> Kumpulkan XP, naikkan gelar, dan raih lencana di <b>🏆 Jurnal Petualang</b>.
</div>""")
    a, b = st.columns(2)
    a.button("📜 Mulai Belajar Materi", on_click=go, args=("📜 Gulungan Materi",), use_container_width=True)
    b.button("⚔️ Langsung ke Arena Kuis", on_click=go, args=("⚔️ Arena Kuis",), use_container_width=True)


# ════════════════════════════════════════════════════════════════
#  HALAMAN: MATERI
# ════════════════════════════════════════════════════════════════
def mark_read(key, label):
    done = key in st.session_state.read
    if done:
        st.success("Materi ini sudah kamu selesaikan ✅")
    elif st.button(f"✅ Tandai '{label}' selesai (+20 XP)", key=f"read_{key}"):
        st.session_state.read.add(key)
        st.session_state.xp += 20
        st.balloons()
        st.rerun()


def materi_data():
    H("<div class='scroll'><b>📊 Bab 1 — Sihir Analisis Data</b><br>Mengubah tumpukan angka menjadi cerita yang bermakna.</div>")
    t1, t2, t3, t4 = st.tabs(["🔎 Apa itu Data?", "📐 Mean, Median, Modus", "📈 Visualisasi", "🧪 Coba Sendiri"])
    with t1:
        st.markdown("""
**Data** adalah fakta mentah, misalnya nilai ulangan, tinggi badan, atau jumlah siswa.
Jika data sudah diolah dan punya makna, hasilnya disebut **informasi**.

| Jenis Data | Penjelasan | Contoh |
|---|---|---|
| Kuantitatif | Berupa angka | Tinggi badan 150 cm |
| Kualitatif | Berupa kategori atau deskripsi | Warna favorit: biru |

**Tahapan analisis data:**
1. 📥 **Mengumpulkan** data (survei, pengamatan, sensor)
2. 🧹 **Membersihkan** data (hapus data ganda atau salah)
3. 🧮 **Menganalisis** (hitung rata-rata, cari pola)
4. 📊 **Menyajikan** (tabel dan grafik)
5. 💡 **Menyimpulkan** dan mengambil keputusan
""")
        H("<div class='tip'>💡 <b>Ingat:</b> data yang kotor menghasilkan kesimpulan yang salah!</div>")
    with t2:
        st.markdown("""
Misalkan nilai: **70, 80, 80, 90, 100**

- **Mean (rata-rata)** = jumlah data : banyak data → (70+80+80+90+100) : 5 = **84**
- **Median** = nilai tengah setelah diurutkan → **80**
- **Modus** = nilai yang paling sering muncul → **80**
""")
        st.code("""import statistics

nilai = [70, 80, 80, 90, 100]
print("Mean  :", statistics.mean(nilai))
print("Median:", statistics.median(nilai))
print("Modus :", statistics.mode(nilai))""", language="python")
    with t3:
        st.markdown("""
Memilih grafik yang tepat:
- 📊 **Grafik batang**: membandingkan kategori (misal nilai tiap siswa)
- 📈 **Grafik garis**: melihat perubahan dari waktu ke waktu
- 🥧 **Grafik lingkaran**: menunjukkan bagian dari keseluruhan (persentase)
""")
        st.code("""import pandas as pd
df = pd.DataFrame({"Siswa": ["Ani", "Budi", "Cici"], "Nilai": [85, 70, 95]})
print(df)""", language="python")
    with t4:
        st.markdown("**🧪 Laboratorium Data:** masukkan angka dipisah koma, lalu lihat hasilnya.")
        txt = st.text_input("Data angka", "70, 80, 80, 90, 100", key="demo_data")
        try:
            nums = parse_nums(txt)
            if nums:
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Mean", f"{statistics.mean(nums):.2f}")
                c2.metric("Median", f"{statistics.median(nums):g}")
                cnt = Counter(nums)
                top = max(cnt.values())
                modes = sorted(k for k, v in cnt.items() if v == top)
                c3.metric("Modus", ", ".join(f"{m:g}" for m in modes) if top > 1 else "Tidak ada")
                c4.metric("Rentang", f"{max(nums) - min(nums):g}")
                st.bar_chart(pd.DataFrame({"Nilai": nums}))
        except ValueError:
            st.warning("Masukkan hanya angka yang dipisahkan koma ya 🙂")
    mark_read("data", "Analisis Data")


def bubble_steps(arr):
    a = arr[:]
    steps = [("Awal", a[:])]
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
                steps.append((f"Tukar {a[j + 1]} dan {a[j]}", a[:]))
        if not swapped:
            break
    return steps


def materi_algo():
    H("<div class='scroll'><b>🧩 Bab 2 — Mantra Algoritma & Pemrograman Python</b><br>Menyusun perintah agar komputer menuruti kehendakmu.</div>")
    t1, t2, t3, t4 = st.tabs(["🪄 Algoritma", "🐍 Dasar Python", "🔁 Percabangan & Perulangan", "🧪 Coba Sendiri"])
    with t1:
        st.markdown("""
**Algoritma** adalah langkah-langkah logis dan berurutan untuk menyelesaikan masalah.
Contoh algoritma membuat teh manis:
1. Siapkan gelas 2. Masukkan teh dan gula 3. Tuang air panas 4. Aduk 5. Selesai ☕

Algoritma dapat ditulis dengan **pseudocode** atau digambar sebagai **flowchart**:

| Simbol | Arti |
|---|---|
| ⬭ Oval | Mulai / Selesai |
| ▭ Persegi panjang | Proses |
| ◇ Belah ketupat | Keputusan (Ya/Tidak) |
| ▱ Jajargenjang | Masukan / Keluaran |

**Ciri algoritma yang baik:** jelas, berurutan, berhingga (ada akhirnya), dan menghasilkan keluaran.
""")
    with t2:
        st.markdown("**Variabel** adalah wadah untuk menyimpan data. **Tipe data** dasar: `int`, `float`, `str`, `bool`.")
        st.code("""nama = "Raka"        # str
umur = 12            # int
tinggi = 150.5       # float
suka_koding = True   # bool

print("Halo,", nama)
print("Tahun depan umurmu", umur + 1)

# Masukan dari pengguna
kota = input("Kamu tinggal di mana? ")
print("Wah, keren! Salam dari", kota)""", language="python")
        st.markdown("**Operator:** `+` `-` `*` `/` (bagi), `//` (hasil bagi bulat), `%` (sisa bagi), `**` (pangkat).")
    with t3:
        st.markdown("**Percabangan** (`if`) membuat program mengambil keputusan, sedangkan **perulangan** (`for`, `while`) mengulang perintah.")
        st.code("""nilai = 82
if nilai >= 90:
    print("Sangat baik")
elif nilai >= 75:
    print("Baik")
else:
    print("Perlu belajar lagi")

for i in range(1, 6):       # 1 sampai 5
    print("Langkah", i)

energi = 3
while energi > 0:
    print("Energi:", energi)
    energi -= 1""", language="python")
        H("<div class='tip'>💡 <b>Tips:</b> Python sangat peka terhadap <b>indentasi</b> (spasi di awal baris). Blok kode harus rapi!</div>")
    with t4:
        st.markdown("**🧪 Penyihir Pengurut (Bubble Sort):** lihat bagaimana algoritma mengurutkan angka langkah demi langkah.")
        txt = st.text_input("Masukkan maksimal 8 angka", "5, 2, 9, 1, 4", key="demo_sort")
        try:
            nums = [int(x) for x in parse_nums(txt)][:8]
            if len(nums) >= 2:
                steps = bubble_steps(nums)
                st.caption(f"Total {len(steps) - 1} penukaran.")
                for title, arr in steps:
                    boxes = " ".join(
                        f"<span style='display:inline-block;min-width:34px;text-align:center;padding:6px;margin:2px;"
                        f"border-radius:10px;background:#4c1d95;border:1px solid #fde68a'>{v}</span>" for v in arr)
                    H(f"<div style='margin:4px 0'><small style='color:#c4b5fd'>{title}</small><br>{boxes}</div>")
                st.success(f"Hasil terurut: {sorted(nums)}")
        except ValueError:
            st.warning("Gunakan bilangan bulat dipisah koma ya 🙂")
    mark_read("algo", "Algoritma & Pemrograman")


def materi_ai():
    H("<div class='scroll'><b>🤖 Bab 3 — Rahasia Kecerdasan Buatan (AI)</b><br>Mesin yang belajar berpikir dari contoh.</div>")
    t1, t2, t3, t4 = st.tabs(["✨ Apa itu AI?", "🧠 Cara AI Belajar", "⚖️ Etika & Bias", "🧪 Coba Sendiri"])
    with t1:
        st.markdown("""
**Kecerdasan Buatan (Artificial Intelligence)** adalah kemampuan komputer atau mesin untuk melakukan tugas
yang biasanya membutuhkan kecerdasan manusia, seperti mengenali wajah, memahami suara, atau menerjemahkan bahasa.

**Contoh AI di sekitarmu:** 🎙️ asisten suara • 🌐 penerjemah otomatis • 🎵 rekomendasi lagu/video •
📷 filter kamera • 🗺️ prediksi kemacetan di peta

**Bukan AI:** kalkulator biasa atau kipas angin, karena hanya mengikuti aturan tetap tanpa belajar.
""")
    with t2:
        st.markdown("""
AI belajar dari **data**, dengan alur sederhana berikut:

`Data → Latih model → Uji model → Gunakan (prediksi)`

| Jenis Belajar | Penjelasan | Contoh |
|---|---|---|
| **Supervised** | Belajar dari data berlabel | Mengenali foto kucing vs anjing |
| **Unsupervised** | Mencari kelompok sendiri tanpa label | Mengelompokkan pelanggan |
| **Reinforcement** | Belajar dari hadiah dan hukuman | AI bermain game |

⚠️ Data latih dan data uji harus **dipisah** agar penilaian model jujur.
""")
    with t3:
        st.markdown("""
AI sangat membantu, tetapi harus digunakan **bijak**:
- 🔒 **Privasi:** lindungi data pribadi dan minta izin sebelum memakai data orang lain.
- ⚖️ **Bias:** jika data latih berat sebelah, hasil AI bisa tidak adil.
- 🕵️ **Hoaks & deepfake:** AI bisa membuat gambar/suara palsu. Selalu periksa sumber!
- 🧑‍🤝‍🧑 **Tanggung jawab:** manusia tetap penentu keputusan akhir.
""")
        H("<div class='tip'>💡 <b>Ingat:</b> AI adalah alat. Etika ada pada manusia yang menggunakannya.</div>")
    with t4:
        st.markdown("**🧪 Mini Peramal Suasana Hati:** model sederhana berbasis aturan untuk menebak kalimat positif atau negatif.")
        pos = {"senang", "bagus", "keren", "suka", "hebat", "indah", "bahagia", "asyik", "mantap"}
        neg = {"sedih", "buruk", "jelek", "benci", "marah", "takut", "bosan", "capek", "kesal"}
        s = st.text_input("Tulis satu kalimat", "Hari ini aku senang sekali, pelajarannya keren!", key="demo_ai")
        words = [w.strip(".,!?").lower() for w in s.split()]
        p, n = sum(w in pos for w in words), sum(w in neg for w in words)
        if p > n:
            st.success(f"😊 Positif (kata positif: {p}, negatif: {n})")
        elif n > p:
            st.error(f"😟 Negatif (kata positif: {p}, negatif: {n})")
        else:
            st.info("😐 Netral atau belum dikenali")
        st.caption("Catatan: ini hanya aturan sederhana. AI sungguhan belajar dari jutaan contoh data!")
        st.code("""kata_positif = {"senang", "keren", "hebat"}
kata_negatif = {"sedih", "buruk", "marah"}

kalimat = input("Tulis kalimat: ").lower().split()
skor = sum(k in kata_positif for k in kalimat) - sum(k in kata_negatif for k in kalimat)
print("Positif" if skor > 0 else "Negatif" if skor < 0 else "Netral")""", language="python")
    mark_read("ai", "Pengenalan AI")


def page_materi():
    st.markdown("## 📜 Gulungan Materi")
    st.caption("Baca ketiga bab ini sebelum memasuki arena kuis. Tiap bab punya percobaan interaktif!")
    tabs = st.tabs(["📊 Analisis Data", "🧩 Algoritma & Python", "🤖 Pengenalan AI"])
    with tabs[0]:
        materi_data()
    with tabs[1]:
        materi_algo()
    with tabs[2]:
        materi_ai()
    st.divider()
    st.button("⚔️ Aku siap! Menuju Arena Kuis", on_click=go, args=("⚔️ Arena Kuis",))


# ════════════════════════════════════════════════════════════════
#  HALAMAN: KUIS
# ════════════════════════════════════════════════════════════════
def select_level(i):
    st.session_state.sel_level = i
    st.session_state.attempt += 1
    st.session_state.result = None
    # acak urutan pilihan sekali per percobaan
    st.session_state.perm = {}
    for qi, q in enumerate(QUESTIONS[i]):
        opts = q["options"][:]
        random.shuffle(opts)
        st.session_state.perm[qi] = opts


def back_to_map():
    st.session_state.sel_level = None
    st.session_state.result = None


def page_quiz():
    st.markdown("## ⚔️ Arena Kuis")
    sel = st.session_state.sel_level

    if sel is None:
        st.caption(f"Lulus tiap level dengan minimal {PASS_MIN} jawaban benar dari 5 soal untuk membuka level berikutnya.")
        cols = st.columns(4)
        for i, lv in enumerate(LEVELS):
            ok = unlocked(i)
            with cols[i % 4]:
                lock = "" if ok else " locked"
                sub = f"✅ Terbaik: {st.session_state.best[i]}/5" if i in st.session_state.best else (
                    f"+{(i + 1) * 10} XP / jawaban benar" if ok else "🔒 Selesaikan level sebelumnya")
                H(f'<div class="lvl{lock}" style="--c:{lv["color"]}"><div class="ic">{lv["icon"]}</div>'
                  f'<div class="nm">{lv["name"]}</div><div class="ds">{lv["desc"]}</div>'
                  f'<div class="ds" style="margin-top:6px">{sub}</div></div>')
                st.button("Masuk" if ok else "Terkunci", key=f"enter_{i}", disabled=not ok,
                          on_click=select_level, args=(i,), use_container_width=True)
        return

    lv = LEVELS[sel]
    H(f'<div class="card" style="border-color:{lv["color"]}"><h4>{lv["icon"]} Level {sel + 1}: {lv["name"]} — {lv["desc"]}</h4>'
      f'Jawab semua soal lalu tekan <b>Kirim Jawaban</b>. Hadiah: <b>{(sel + 1) * 10} XP</b> per jawaban benar.</div>')

    questions = QUESTIONS[sel]
    result = st.session_state.result

    if result is None:
        with st.form(f"form_{sel}_{st.session_state.attempt}"):
            answers = {}
            for qi, q in enumerate(questions):
                H(f'<div class="qbox"><b>Soal {qi + 1}.</b> {q["q"]}</div>')
                if q["code"]:
                    st.code(q["code"], language="python")
                opts = st.session_state.perm.get(qi, q["options"])
                answers[qi] = st.radio(f"Soal {qi + 1}", opts, index=None,
                                       key=f"ans_{sel}_{qi}_{st.session_state.attempt}",
                                       label_visibility="collapsed")
            submitted = st.form_submit_button("🔮 Kirim Jawaban", use_container_width=True)
        if submitted:
            if any(a is None for a in answers.values()):
                st.warning("Masih ada soal yang belum dijawab. Lengkapi dulu ya! ✍️")
            else:
                correct = sum(1 for qi, q in enumerate(questions) if answers[qi] == q["answer"])
                prev = st.session_state.best.get(sel, 0)
                gain = 0
                if correct > prev:
                    gain = (correct - prev) * (sel + 1) * 10
                    st.session_state.xp += gain
                st.session_state.best[sel] = max(prev, correct)
                st.session_state.result = {"answers": answers, "correct": correct, "gain": gain}
                st.rerun()
        st.button("⬅️ Kembali ke Peta Level", on_click=back_to_map)
        return

    # ── tampilan hasil
    correct, gain = result["correct"], result["gain"]
    passed = correct >= PASS_MIN
    if correct == 5:
        st.balloons()
        H("<div class='hero'><div class='orb'>🏆</div><h1>SEMPURNA!</h1><p>Kamu menaklukkan level ini tanpa cela!</p></div>")
    elif passed:
        st.snow()
        H(f"<div class='hero'><div class='orb'>🎉</div><h1>LEVEL LULUS!</h1><p>Skor {correct}/5. Gerbang berikutnya telah terbuka!</p></div>")
    else:
        H(f"<div class='hero'><div class='orb'>🌫️</div><h1>Belum Berhasil</h1><p>Skor {correct}/5. Tenang, pelajari materinya lalu coba lagi!</p></div>")
    st.markdown(f"**Skor:** {correct}/5   •   **XP didapat:** +{gain}   •   **Gelar:** {rank_name()}")

    st.markdown("### 📖 Pembahasan")
    for qi, q in enumerate(questions):
        mine = result["answers"][qi]
        good = mine == q["answer"]
        H(f'<div class="qbox"><b>Soal {qi + 1}.</b> {q["q"]}</div>')
        if q["code"]:
            st.code(q["code"], language="python")
        if good:
            H(f'<div class="ok">✅ <b>Benar!</b> Jawabanmu: <code>{mine}</code><br>💡 {q["why"]}</div>'.replace("\n", "<br>"))
        else:
            H(f'<div class="bad">❌ Jawabanmu: <code>{mine}</code><br>✔️ Jawaban benar: <code>{q["answer"]}</code><br>💡 {q["why"]}</div>'.replace("\n", "<br>"))

    c1, c2, c3 = st.columns(3)
    c1.button("🔄 Ulangi Level", on_click=select_level, args=(sel,), use_container_width=True)
    if passed and sel + 1 < len(LEVELS):
        c2.button("➡️ Level Berikutnya", on_click=select_level, args=(sel + 1,), use_container_width=True)
    c3.button("🗺️ Peta Level", on_click=back_to_map, use_container_width=True)


# ════════════════════════════════════════════════════════════════
#  HALAMAN: JURNAL
# ════════════════════════════════════════════════════════════════
def page_journal():
    st.markdown("## 🏆 Jurnal Petualang")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="stat"><div class="n">{st.session_state.xp}</div><div class="l">✨ Total XP</div></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="stat"><div class="n" style="font-size:1.3rem">{rank_name()}</div><div class="l">🎖️ Gelar Saat Ini</div></div>', unsafe_allow_html=True)
    nxt = next((f"{n} ({need} XP)" for need, n in RANKS if need > st.session_state.xp), "Gelar tertinggi!")
    c3.markdown(f'<div class="stat"><div class="n" style="font-size:1.1rem">{nxt}</div><div class="l">🎯 Gelar Berikutnya</div></div>', unsafe_allow_html=True)

    st.markdown("### 📋 Catatan Level")
    rows = []
    for i, lv in enumerate(LEVELS):
        b = st.session_state.best.get(i)
        rows.append({
            "Level": f"{lv['icon']} {lv['name']}",
            "Wilayah": lv["desc"],
            "Skor Terbaik": f"{b}/5" if b is not None else "-",
            "Status": "✅ Lulus" if (b is not None and b >= PASS_MIN) else ("🔓 Terbuka" if unlocked(i) else "🔒 Terkunci"),
        })
    st.dataframe(pd.DataFrame(rows), hide_index=True, use_container_width=True)

    st.markdown("### 🎖️ Lencana")
    badges = [
        ("📜 Pembaca Gulungan", len(st.session_state.read) == 3),
        ("🌱 Langkah Pertama", 0 in st.session_state.best and st.session_state.best[0] >= PASS_MIN),
        ("⚔️ Penakluk Benteng", st.session_state.best.get(3, 0) >= PASS_MIN),
        ("🐉 Pembunuh Naga", st.session_state.best.get(5, 0) >= PASS_MIN),
        ("👑 Raja Data", st.session_state.best.get(6, 0) >= PASS_MIN),
        ("🌌 Penjaga Semesta", st.session_state.best.get(7, 0) >= PASS_MIN),
        ("💎 Skor Sempurna", any(v == 5 for v in st.session_state.best.values())),
    ]
    H("".join(f'<span class="badge{"" if ok else " off"}">{n}</span>' for n, ok in badges))

    st.divider()
    if st.button("🗑️ Reset Semua Progres"):
        for k in ["xp", "best", "read", "sel_level", "attempt", "result", "perm"]:
            st.session_state.pop(k, None)
        st.session_state.page = "🏰 Beranda"
        st.rerun()


# ════════════════════════════════════════════════════════════════
#  ROUTER
# ════════════════════════════════════════════════════════════════
if page == PAGES[0]:
    page_home()
elif page == PAGES[1]:
    page_materi()
elif page == PAGES[2]:
    page_quiz()
else:
    page_journal()
