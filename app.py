import streamlit as st

# ===== Page config =====
st.set_page_config(page_title="Movie App", layout="wide", page_icon="🎬")

# ===== Style CSS =====
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #1f1c2c, #928dab);
    color: #ffffff;
}
.title {
    font-size: 48px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
}
.subtitle {
    font-size: 24px;
    font-weight: bold;
    color: #ffdd00;
}
.poster img {
    border-radius: 15px;
    transition: transform 0.3s;
}
.poster img:hover {
    transform: scale(1.05);
}
.stButton button {
    background-color: #ff5722;
    color: white;
    border-radius: 10px;
    padding: 0.5em 1em;
    font-weight: bold;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# ===== DATA =====
movies = {
    "Avatar": {"poster":"https://image.tmdb.org/t/p/w500/8YFL5QQVPy3AgrEQxNYVSgiPEbe.jpg","trailer":"https://www.youtube.com/watch?v=5PSNL1qE6VY","genres":["Action","Adventure","Fantasy"],"rating":7.8,"popularity":95,"year":2009},
    "Titanic": {"poster":"https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg","trailer":"https://www.youtube.com/watch?v=kVrqfYjkTdQ","genres":["Romance","Drama"],"rating":7.9,"popularity":98,"year":1997},
    "Avengers": {"poster":"https://image.tmdb.org/t/p/w500/RYMX2wcKCBAr24UyPD7xwmjaTn.jpg","trailer":"https://www.youtube.com/watch?v=eOrNdBpGMv8","genres":["Action","Adventure","Sci-Fi"],"rating":8.0,"popularity":99,"year":2012},
    "Joker": {"poster":"https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg","trailer":"https://www.youtube.com/watch?v=zAGVQLHvwOY","genres":["Crime","Drama","Thriller"],"rating":8.5,"popularity":90,"year":2019},
    "Frozen": {"poster":"https://image.tmdb.org/t/p/w500/kgwjIb2JDHRhNk13lmSxiClFjVk.jpg","trailer":"https://www.youtube.com/watch?v=TbQm5doF_Uc","genres":["Animation","Family","Fantasy"],"rating":7.4,"popularity":85,"year":2013},
    "Inception": {"poster":"https://image.tmdb.org/t/p/w500/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg","trailer":"https://www.youtube.com/watch?v=YoHD9XEInc0","genres":["Action","Sci-Fi","Thriller"],"rating":8.8,"popularity":92,"year":2010},
    "Up": {"poster":"https://image.tmdb.org/t/p/w500/4q2NNj4S5dG2RLF9CpXsej7yXl.jpg","trailer":"https://www.youtube.com/watch?v=pkqzFUhGPJg","genres":["Animation","Adventure","Comedy"],"rating":8.2,"popularity":80,"year":2009}
}

# ===== HEADER =====
st.markdown('<div class="title">🎬 Movie Recommendation System</div>', unsafe_allow_html=True)

# ===== SEARCH & FILTER =====
st.subheader("🔍 Tìm phim hoặc lọc theo thể loại")

# Tất cả thể loại
all_genres = sorted({g for info in movies.values() for g in info["genres"]})
selected_genre = st.selectbox("Chọn thể loại:", ["Tất cả"] + all_genres)

search_text = st.text_input("Hoặc tìm theo tên phim:")

# Lọc phim theo thể loại & tên
def filter_movies(search="", genre="Tất cả"):
    results = []
    for name, info in movies.items():
        if (genre=="Tất cả" or genre in info["genres"]) and (search.lower() in name.lower()):
            results.append(name)
    return results

filtered_movies = filter_movies(search_text, selected_genre)

# ===== HIỂN THỊ KẾT QUẢ =====
st.markdown("---")
st.subheader("🎥 Kết quả phim")

if filtered_movies:
    cols = st.columns(len(filtered_movies))
    for i, m in enumerate(filtered_movies):
        with cols[i]:
            st.image(movies[m]["poster"], use_column_width=True)
            st.markdown(f"<h4 style='text-align:center'>{m} ({movies[m]['year']})</h4>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center'>⭐ {movies[m]['rating']}</p>", unsafe_allow_html=True)
            if st.button(f"🎬 Trailer {m}", key=m):
                st.video(movies[m]["trailer"])
else:
    st.write("Không tìm thấy phim phù hợp.")

# ===== TOP 10 YÊU THÍCH =====
st.markdown("---")
st.subheader("🏆 Top 10 yêu thích")
top_movies = sorted(movies.items(), key=lambda x: x[1]["popularity"], reverse=True)[:10]

cols = st.columns(5)
for i, (m, info) in enumerate(top_movies):
    with cols[i%5]:
        st.image(info["poster"], use_column_width=True)
        st.markdown(f"<h4 style='text-align:center'>{m} ({info['year']})</h4>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center'>⭐ {info['rating']}</p>", unsafe_allow_html=True)
        if st.button(f"🎬 Trailer {m}", key=f"top_{i}"):
            st.video(info["trailer"])

# ===== GỢI Ý PHIM THEO PHIM CHỌN =====
st.markdown("---")
st.subheader("🔥 Gợi ý phim dựa trên phim bạn chọn")

selected_movie2 = st.selectbox("Chọn phim để gợi ý:", list(movies.keys()), key="recommend")

def recommend(movie, top_n=4):
    selected_genres = set(movies[movie]["genres"])
    scores = []
    for m, info in movies.items():
        if m == movie:
            continue
        genre_overlap = len(selected_genres & set(info["genres"]))
        rating_diff = abs(info["rating"] - movies[movie]["rating"])
        popularity = info["popularity"]
        score = genre_overlap * 2 - rating_diff + popularity/50
        scores.append((score, m))
    scores.sort(reverse=True)
    return [m for _, m in scores[:top_n]]

cols = st.columns(4)
for i, m in enumerate(recommend(selected_movie2)):
    with cols[i]:
        st.image(movies[m]["poster"], use_column_width=True)
        st.markdown(f"<h4 style='text-align:center'>{m} ({movies[m]['year']})</h4>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center'>⭐ {movies[m]['rating']}</p>", unsafe_allow_html=True)
        if st.button(f"🎬 Trailer {m}", key=f"rec_{m}"):
            st.video(movies[m]["trailer"])