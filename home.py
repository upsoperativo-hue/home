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

st.markdown("---")

col1, col2 = st.columns([1, 3])

with col1:
    st.markdown(
        """
        <div style="
            background-color:#351c15;
            color:white;
            width:70px;
            height:70px;
            border-radius:12px;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:32px;
            font-weight:bold;
        ">
            📅
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style="
            background-color:#f5f1e8;
            border-left:6px solid #351c15;
            padding:12px 16px;
            border-radius:8px;
        ">
            <div style="font-size:20px; font-weight:600; color:#351c15;">
                MAGIC (WONDER)
                <span style="
                    background-color:#d89b2b;
                    color:white;
                    font-size:11px;
                    font-weight:700;
                    padding:2px 6px;
                    border-radius:6px;
                    margin-left:8px;
                ">
                    NEW
                </span>
            </div>
            <div style="font-size:13px; color:#4a3b32; margin-top:4px;">
                You know what you can do <b>Magic = 1</b> that's fine
                yes! <b>MAGIC</b> in formato <b>.xlsm</b> you can.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.link_button(
    "Apri MAGIC",
    "https://tsphrgi5vh7thxezejgwm4.streamlit.app"
)

