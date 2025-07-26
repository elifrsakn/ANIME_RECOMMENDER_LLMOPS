import streamlit as st
from pathlib import Path
from dotenv import load_dotenv
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pipeline.pipeline import AnimeRecommendationPipeline

st.set_page_config(page_title="Anime Recommender", layout="wide")
load_dotenv()

from pathlib import Path
import streamlit as st

# Dinamik olarak app.py'nin bulunduğu klasöre göre path oluştur
image_path = Path(__file__).resolve().parent / "image" / "elif_anime.png"

if image_path.exists():
    st.image(
        str(image_path),
        caption="Anime-style Portrait by Elif Rana Sakin",
        width=400
    )

else:
    st.warning("Görsel bulunamadı. Lütfen 'images/elif_anime.png' dosyasının proje içinde olduğundan emin olun.")

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your anime preferences e.g.: light hearted anime with school settings")
if query:
    with st.spinner("Fetching recommendations for you....."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)
