import streamlit as st
from PIL import Image, ImageFilter
import numpy as np
import io
import streamlit.components.v1 as components

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="AI Image Dashboard", layout="wide")

# 👉 Center UI
st.markdown("""
<style>
.block-container {
    max-width: 1100px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.title("✨ AI Image Dashboard")

# =========================
# NAVIGATION TABS
# =========================
tab1, tab2 = st.tabs(["🖼 Image Editor", "🚀 Advanced AI Tools"])

# =========================
# TAB 1 → YOUR ORIGINAL TOOL
# =========================
with tab1:

    st.info("👉 Upload an image from the sidebar")

    st.sidebar.title("🧰 Tools")

    uploaded_file = st.sidebar.file_uploader(
        "📤 Upload Image", type=["png", "jpg", "jpeg"]
    )

    tool = st.sidebar.radio(
        "Select Tool",
        ["🎨 Background Change", "✨ Enhance Image"]
    )

    col1, col2 = st.columns(2)

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        image.thumbnail((600, 600))

        with col1:
            st.subheader("📸 Original Image")
            st.image(image, use_column_width=True)

        # 🎨 Background Change
        if tool == "🎨 Background Change":
            st.sidebar.subheader("🎨 Settings")

            color_hex = st.sidebar.color_picker("Pick Background Color", "#00ffaa")
            color = tuple(int(color_hex[i:i+2], 16) for i in (1, 3, 5))

            if st.sidebar.button("🚀 Apply Background"):
                with st.spinner("Processing..."):
                    img_array = np.array(image)

                    gray = np.mean(img_array, axis=2)
                    mask = gray > 200

                    img_array[mask] = color
                    result = Image.fromarray(img_array)

                with col2:
                    st.subheader("✅ Result")
                    st.image(result, use_column_width=True)

                buf = io.BytesIO()
                result.save(buf, format="PNG")

                st.download_button("📥 Download", buf.getvalue(), "background.png")

        # ✨ Enhance Image
        elif tool == "✨ Enhance Image":
            st.sidebar.subheader("✨ Settings")

            strength = st.sidebar.slider("Sharpness", 1, 5, 2)

            if st.sidebar.button("🚀 Enhance"):
                with st.spinner("Enhancing image..."):
                    result = image

                    for _ in range(strength):
                        result = result.filter(ImageFilter.SHARPEN)

                with col2:
                    st.subheader("✅ Result")
                    st.image(result, use_column_width=True)

                buf = io.BytesIO()
                result.save(buf, format="PNG")

                st.download_button("📥 Download", buf.getvalue(), "enhanced.png")

    else:
        st.warning("👈 Upload image to start")

# =========================
# TAB 2 → ALL ADVANCED TOOLS INSIDE APP
# =========================
with tab2:

    st.markdown("## 🚀 Advanced AI Tools")

    tool_choice = st.radio(
        "Choose Tool",
        ["🧽 Erase Tool", "🌫 Blur Tool", "❌ Remove Object", "🌄 Background Tool"],
        horizontal=True
    )

    st.markdown("---")

    # 👉 EMBED TOOLS INSIDE APP
    if tool_choice == "🧽 Erase Tool":
        components.iframe(
            "https://skyhostpro32-dev.github.io/erase-tool/",
            height=600,
            scrolling=True
        )

    elif tool_choice == "🌫 Blur Tool":
        components.iframe(
            "https://skyhostpro32-dev.github.io/index./",
            height=600
        )

    elif tool_choice == "❌ Remove Object":
        components.iframe(
            "https://l3c2ddsnh8gkka5rnezbak.streamlit.app/",
            height=600
        )

    elif tool_choice == "🌄 Background Tool":
        components.iframe(
            "https://import-cus7p2zpohpwkbavzyrmpl.streamlit.app/",
            height=600
        )

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("🚀 Built with Streamlit | All-in-One AI Image Dashboard")
