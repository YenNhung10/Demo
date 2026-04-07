import streamlit as st

# ===== Page config =====
st.set_page_config(page_title="Movie App", layout="wide", page_icon="🎬")

# ===== Style CSS =====
st.markdown("""
<style>

/* Card */
.movie-card {
    background: linear-gradient(145deg, #1f1f2e, #2a2a40);
    padding: 12px;
    border-radius: 16px;
    text-align: center;
    margin-bottom: 15px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    position: relative;
    overflow: hidden;
}
/* Background toàn app */
[data-testid="stAppViewContainer"] {
    background: url("https://images.unsplash.com/photo-1524985069026-dd778a71c7b4");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}            

/* Glow khi hover */
.movie-card:hover {
    transform: translateY(-5px) scale(1.03);
    box-shadow: 0 8px 25px rgba(255, 0, 150, 0.4);
}

/* Viền highlight động */
.movie-card {
    background: #23232b; /* xám đậm */
    padding: 12px;
    border-radius: 16px;
    text-align: center;
    margin-bottom: 15px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0,0,0,0.5);
}

/* hover sáng nhẹ */
.movie-card:hover {
    background: #2a2a35;
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.7);
}

/* Poster */
.movie-card img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    border-radius: 12px;
    transition: 0.3s;
}

.movie-card:hover img {
    filter: brightness(1.1);
}

/* Title */
.movie-title {
    font-size: 15px;
    font-weight: bold;
    margin-top: 8px;
    color: #ffffff;
}

/* Info */
.movie-info {
    font-size: 13px;
    color: #bbb;
}

/* Rating highlight */
.movie-rating {
    margin-top: 5px;
    font-size: 13px;
    color: #ffd700;
    font-weight: bold;
}

/* Badge nổi */
.movie-badge {
    position: absolute;
    top: 8px;
    left: 8px;
    background: linear-gradient(45deg, #ff4ecd, #ff9a9e);
    color: white;
    padding: 3px 8px;
    font-size: 11px;
    border-radius: 8px;
    font-weight: bold;
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

    "Spider-Man: No Way Home": {"poster":"https://image.tmdb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg","trailer":"https://www.youtube.com/watch?v=JfVOs4VSpmA","genres":["Action","Adventure","Sci-Fi"],"rating":8.2,"popularity":97,"year":2021},

    "The Batman": {"poster":"https://image.tmdb.org/t/p/w500/74xTEgt7R36Fpooo50r9T25onhq.jpg","trailer":"https://www.youtube.com/watch?v=mqqft2x_Aa4","genres":["Action","Crime","Drama"],"rating":7.9,"popularity":93,"year":2022},

    "Maleficent": {"poster":"https://image.tmdb.org/t/p/w500/bDG3yei6AJlEAK3A5wN7RwFXQ7V.jpg","trailer":"https://www.youtube.com/watch?v=n0OFH4xpPr4","genres":["Fantasy","Adventure","Family"],"rating":7.0,"popularity":88,"year":2014},

    "Barbie": {"poster":"https://image.tmdb.org/t/p/w500/iuFNMS8U5cb6xfzi51Dbkovj7vM.jpg","trailer":"https://www.youtube.com/watch?v=pBk4NYhWNMM","genres":["Comedy","Fantasy"],"rating":7.3,"popularity":96,"year":2023},

    "Luca": {"poster":"https://image.tmdb.org/t/p/w500/jTswp6KyDYKtvC52GbHagrZbGvD.jpg","trailer":"https://www.youtube.com/watch?v=mYfJxlgR2jw","genres":["Animation","Family","Fantasy"],"rating":7.5,"popularity":84,"year":2021},

    "The Lion King": {"poster":"https://image.tmdb.org/t/p/w500/sKCr78MXSLixwmZ8DyJLrpMsd15.jpg","trailer":"https://www.youtube.com/watch?v=4sj1MT05lAA","genres":["Animation","Adventure","Drama"],"rating":8.5,"popularity":95,"year":1994},

    "Harry Potter and the Goblet of Fire": {"poster":"https://image.tmdb.org/t/p/w500/fECBtHlr0RB3foNHDiCBXeg9Bv9.jpg","trailer":"https://www.youtube.com/watch?v=3EGojp4Hh6I","genres":["Fantasy","Adventure"],"rating":7.7,"popularity":94,"year":2005},

    "Minions": {"poster":"https://image.tmdb.org/t/p/w500/dr02BdCNAUPVU07aOodwPYv6HCf.jpg","trailer":"https://www.youtube.com/watch?v=eisKxhjBnZ0","genres":["Animation","Comedy","Family"],"rating":6.4,"popularity":90,"year":2015},

    "Kung Fu Panda": {"poster":"https://image.tmdb.org/t/p/w500/wWt4JYXTg5Wr3xBW2phBrMKgp3x.jpg","trailer":"https://www.youtube.com/watch?v=PXi3Mv6KMzY","genres":["Animation","Action","Comedy"],"rating":7.6,"popularity":89,"year":2008},

    "Finding Nemo": {"poster":"https://image.tmdb.org/t/p/w500/eHuGQ10FUzK1mdOY69wF5pGgEf5.jpg","trailer":"https://www.youtube.com/watch?v=wZdpNglLbt8","genres":["Animation","Adventure","Family"],"rating":8.2,"popularity":91,"year":2003},

    "The Nun": {"poster":"https://upload.wikimedia.org/wikipedia/en/3/34/TheNunPoster.jpg","trailer":"https://www.youtube.com/watch?v=pzD9zGcUNrw","genres":["Horror","Mystery","Thriller"],"rating":5.3,"popularity":87,"year":2018},

    "The Jungle Book": {"poster":"https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_%282016%29.jpg","trailer":"https://www.youtube.com/watch?v=5mkm22yO-bs","genres":["Adventure","Family","Fantasy"],"rating":7.4,"popularity":88,"year":2016},

    "The Secret Life of Pets": {"poster":"https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg","trailer":"https://www.youtube.com/watch?v=i-80SGWfEjM","genres":["Animation","Comedy","Family"],"rating":6.5,"popularity":86,"year":2016},

    "Se7en": {"poster":"https://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg","trailer":"https://www.youtube.com/watch?v=znmZoVkCjpI","genres":["Crime","Thriller"],"rating":8.6,"popularity":92,"year":1995},

    "Twilight": {"poster":"https://upload.wikimedia.org/wikipedia/en/b/b6/Twilight_%282008_film%29_poster.jpg","trailer":"https://www.youtube.com/watch?v=uxjNDE2fMjI","genres":["Romance","Fantasy"],"rating":5.2,"popularity":85,"year":2008},

    "The Godfather": {"poster":"https://upload.wikimedia.org/wikipedia/en/a/af/The_Godfather%2C_The_Game.jpg","trailer":"https://www.youtube.com/watch?v=sY1S34973zA","genres":["Crime","Drama"],"rating":9.2,"popularity":99,"year":1972},

    "Train to Busan": {"poster":"https://upload.wikimedia.org/wikipedia/en/9/95/Train_to_Busan.jpg","trailer":"https://www.youtube.com/watch?v=pyWuHv2-Abk","genres":["Action","Horror","Thriller"],"rating":7.6,"popularity":93,"year":2016},

    "The Shawshank Redemption": {"poster":"https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg","trailer":"https://www.youtube.com/watch?v=6hB3S9bIaco","genres":["Drama"],"rating":9.3,"popularity":100,"year":1994},

    "Home Alone": {"poster":"https://upload.wikimedia.org/wikipedia/en/7/76/Home_alone_poster.jpg","trailer":"https://www.youtube.com/watch?v=jEDaVHmw7r4","genres":["Comedy","Family"],"rating":7.7,"popularity":90,"year":1990},


    "Moana": {"poster":"https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg","trailer":"https://www.youtube.com/watch?v=LKFuXETZUsI","genres":["Animation","Adventure","Family"],"rating":7.6,"popularity":91,"year":2016},

    "Encanto": {"poster":"https://upload.wikimedia.org/wikipedia/en/8/83/Encanto_poster.jpg","trailer":"https://www.youtube.com/watch?v=CaimKeDcudo","genres":["Animation","Family","Fantasy"],"rating":7.2,"popularity":88,"year":2021},

    "John Wick": {"poster":"https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg","trailer":"https://www.youtube.com/watch?v=qEVUtrk8_B4","genres":["Action","Crime","Thriller"],"rating":7.4,"popularity":94,"year":2014},

    "Inside Out": {"poster":"https://image.tmdb.org/t/p/w500/2H1TmgdfNtsKlU9jKdeNyYL5y8T.jpg","trailer":"https://www.youtube.com/watch?v=rOYhoc4CTX0","genres":["Animation","Family","Drama"],"rating":8.1,"popularity":93,"year":2015}
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
# Khởi tạo
if "visible_count" not in st.session_state:
    st.session_state.visible_count = 5

if "last_search" not in st.session_state:
    st.session_state.last_search = ""

if "last_genre" not in st.session_state:
    st.session_state.last_genre = "Tất cả"

# Reset CHỈ khi người dùng đổi search hoặc genre
if search_text != st.session_state.last_search or selected_genre != st.session_state.last_genre:
    st.session_state.visible_count = 5
    st.session_state.last_search = search_text
    st.session_state.last_genre = selected_genre
if st.session_state.visible_count < len(filtered_movies):
    if st.button("Xem thêm"):
        st.session_state.visible_count += 5

# ===== HIỂN THỊ KẾT QUẢ =====
st.markdown("---")
st.subheader("🎥 Kết quả phim")


# lấy danh sách hiển thị
display_movies = filtered_movies[:st.session_state.visible_count]

if filtered_movies:

    cols = st.columns(5)

    for i, m in enumerate(display_movies):
        with cols[i % 5]:

            st.markdown(f"""
            <div class="movie-card">
                <img src="{movies[m]["poster"]}">
                <div class="movie-title">{m}</div>
                <div class="movie-info">📅 {movies[m]['year']}</div>
                <div class="movie-info">⭐ {movies[m]['rating']}</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"🎬 Trailer", key=f"trailer_{m}"):
                st.video(movies[m]["trailer"])

    # nút xem thêm
    if st.session_state.visible_count < len(filtered_movies):
        if st.button("🔽 Xem thêm"):
            st.session_state.visible_count += 5

else:
    st.write("Không tìm thấy phim phù hợp.")
# ===== TOP 10 YÊU THÍCH =====
st.markdown("---")
st.subheader("🏆 Top 10 yêu thích")
top_movies = sorted(movies.items(), key=lambda x: x[1]["popularity"], reverse=True)[:10]

cols = st.columns(6)
for i, (m, info) in enumerate(top_movies):
    with cols[i%6]:
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
