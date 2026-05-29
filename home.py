import streamlit as st

st.set_page_config(page_title="UPS Operativo — Tools Center", page_icon="📦")

st.title("UPS Operativo — Tools Center")
st.write("Seleziona uno strumento per aprire l'app dedicata.")

st.markdown("---")

# ============================================================
# 1) LQR TOOL
# ============================================================
st.subheader("📦 LQR Tool")
st.write("Generatore LQR con barcode vettoriali.")
st.link_button(
    "Apri LQR Tool",
    "https://ups-lqr-tool-zqyegq7codzd542fo4s36x.streamlit.app/"
)

st.markdown("---")

# ============================================================
# 2) BINDELLI BARCODE GENERATOR
# ============================================================
st.subheader("🏷️ Bindelli Barcode Generator")
st.write("Generatore di etichette con barcode per Bindelli.")
st.link_button(
    "Apri Bindelli Barcode Generator",
    "https://bindelli-barcode-generator-sdfozmjhtff7vrv7sc6xnd.streamlit.app/"
)

st.markdown("---")

# ============================================================
# 3) UNISCI PDF
# ============================================================
st.subheader("🧾 Unisci PDF")
st.write("Strumento per unire più PDF in un unico file.")
st.link_button(
    "Apri Unisci PDF",
    "https://unisci-pdf-jietc4xahcuou8e3mqvdyf.streamlit.app/"
)

st.markdown("---")

# ============================================================
# 4) STAMPA TRACKING (TXT → PDF)
# ============================================================
st.subheader("📄 Stampa Tracking UPS (TXT → PDF)")
st.write("Carica un file .txt e genera un PDF con etichette barcode UPS.")
st.link_button(
    "Apri Stampa Tracking",
    "https://stampa-trk-gqbnhcjdzyg7jjknbflbfo.streamlit.app/"
)

st.markdown("---")

st.info("Puoi aggiungere qui tutte le app future.")
