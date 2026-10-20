
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

st.title("🚲 Bike Sharing Analysis Dashboard")
st.write(
    "Dashboard interaktif untuk mengeksplorasi pola penyewaan "
    "sepeda berdasarkan waktu, musim, dan kondisi cuaca "
    "selama periode 2011–2012."
)

# Memuat dataset
DATA_PATH = Path(__file__).parent / "day.csv"


@st.cache_data
def load_data(path):
    data = pd.read_csv(path)
    data["dteday"] = pd.to_datetime(data["dteday"])

    data["year"] = data["yr"].map({0: 2011, 1: 2012})
    data["month_num"] = data["dteday"].dt.month

    data["season_name"] = data["season"].map({
        1: "Winter",
        2: "Spring",
        3: "Summer",
        4: "Fall"
    })

    data["weather_name"] = data["weathersit"].map({
        1: "Clear / Few Clouds",
        2: "Mist / Cloudy",
        3: "Light Rain / Snow",
        4: "Heavy Rain / Snow"
    })

    return data


if not DATA_PATH.exists():
    st.error(
        "File day.csv tidak ditemukan. "
        "Pastikan file berada di dalam folder data."
    )
    st.stop()

df = load_data(str(DATA_PATH))

# Filter pada sidebar
st.sidebar.header("Filter Data")

years = sorted(df["year"].dropna().unique())
selected_years = st.sidebar.multiselect(
    "Pilih Tahun",
    years,
    default=years
)

months = list(range(1, 13))
selected_months = st.sidebar.multiselect(
    "Pilih Bulan",
    months,
    default=months,
    format_func=lambda m: pd.Timestamp(
        year=2000, month=m, day=1
    ).strftime("%B")
)

seasons = ["Winter", "Spring", "Summer", "Fall"]
selected_seasons = st.sidebar.multiselect(
    "Pilih Musim",
    seasons,
    default=seasons
)

filtered_df = df[
    df["year"].isin(selected_years)
    & df["month_num"].isin(selected_months)
    & df["season_name"].isin(selected_seasons)
].copy()

if filtered_df.empty:
    st.warning("Tidak ada data untuk kombinasi filter ini.")
    st.stop()

# Ringkasan utama / KPI
total_rentals = int(filtered_df["cnt"].sum())
average_rentals = filtered_df["cnt"].mean()
casual_rentals = int(filtered_df["casual"].sum())
registered_rentals = int(filtered_df["registered"].sum())

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Rentals",
    f"{total_rentals:,}"
)

col2.metric(
    "Average Daily Rentals",
    f"{average_rentals:,.2f}"
)

col3.metric(
    "Casual Rentals",
    f"{casual_rentals:,}"
)

col4.metric(
    "Registered Rentals",
    f"{registered_rentals:,}"
)

st.divider()

# Grafik tren penyewaan harian
st.subheader("Daily Bike Rental Trend")
st.write(
    "Grafik ini menunjukkan jumlah penyewaan sepeda setiap hari "
    "pada periode yang dipilih. Perhatikan pola kenaikan dan penurunan "
    "untuk mengidentifikasi waktu dengan permintaan yang relatif tinggi "
    "atau rendah."
)

daily = filtered_df.sort_values("dteday")

fig_trend = px.line(
    daily,
    x="dteday",
    y="cnt",
    markers=True,
    title="Daily Bike Rentals Over Time",
    labels={
        "dteday": "Date",
        "cnt": "Number of Rentals"
    }
)

fig_trend.update_layout(
    yaxis_tickformat=",",
    hovermode="x unified"
)

st.plotly_chart(fig_trend, use_container_width=True)

st.caption(
    "Interpretasi: gunakan tren ini untuk melihat perubahan permintaan "
    "sepanjang waktu. Pola yang terlihat bersifat deskriptif dan tidak "
    "dengan sendirinya menjelaskan penyebab perubahan."
)

# Grafik berdasarkan musim dan cuaca
left, right = st.columns(2)

with left:
    st.subheader("Average Rentals by Season")
    st.write(
        "Grafik membandingkan rata-rata penyewaan harian antar musim "
        "berdasarkan filter yang sedang dipilih."
    )

    season_summary = (
        filtered_df.groupby("season_name", as_index=False)["cnt"]
        .mean()
    )

    season_summary["season_name"] = pd.Categorical(
        season_summary["season_name"],
        categories=seasons,
        ordered=True
    )

    season_summary = season_summary.sort_values("season_name")

    fig_season = px.bar(
        season_summary,
        x="season_name",
        y="cnt",
        title="Average Daily Rentals by Season",
        labels={
            "season_name": "Season",
            "cnt": "Average Daily Rentals"
        },
        text="cnt"
    )

    fig_season.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside",
        hovertemplate=(
            "Season=%{x}<br>"
            "Average Daily Rentals=%{y:,.2f}<extra></extra>"
        )
    )

    fig_season.update_layout(
        yaxis_tickformat=",",
        yaxis_title="Average Daily Rentals",
        xaxis_title="Season"
    )

    st.plotly_chart(fig_season, use_container_width=True)

    if not season_summary.empty:
        highest_season = season_summary.loc[
            season_summary["cnt"].idxmax()
        ]
        lowest_season = season_summary.loc[
            season_summary["cnt"].idxmin()
        ]

        st.caption(
            f"Insight berdasarkan filter saat ini: rata-rata penyewaan "
            f"tertinggi terdapat pada musim {highest_season['season_name']} "
            f"({highest_season['cnt']:,.2f} penyewaan per hari), sedangkan "
            f"terendah pada musim {lowest_season['season_name']} "
            f"({lowest_season['cnt']:,.2f})."
        )

with right:
    st.subheader("Average Rentals by Weather")
    st.write(
        "Grafik membandingkan rata-rata penyewaan harian menurut kategori "
        "cuaca yang tercatat dalam dataset."
    )

    weather_summary = (
        filtered_df.groupby("weather_name", as_index=False)["cnt"]
        .mean()
        .sort_values("cnt", ascending=False)
    )

    fig_weather = px.bar(
        weather_summary,
        x="weather_name",
        y="cnt",
        title="Average Daily Rentals by Weather",
        labels={
            "weather_name": "Weather Condition",
            "cnt": "Average Daily Rentals"
        },
        text="cnt"
    )

    fig_weather.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside",
        hovertemplate=(
            "Weather Condition=%{x}<br>"
            "Average Daily Rentals=%{y:,.2f}<extra></extra>"
        )
    )

    fig_weather.update_layout(
        yaxis_tickformat=",",
        yaxis_title="Average Daily Rentals",
        xaxis_title="Weather Condition",
        xaxis_tickangle=-15
    )

    st.plotly_chart(fig_weather, use_container_width=True)

    if not weather_summary.empty:
        highest_weather = weather_summary.iloc[0]
        lowest_weather = weather_summary.iloc[-1]

        st.caption(
            f"Insight berdasarkan filter saat ini: rata-rata penyewaan "
            f"tertinggi tercatat pada kondisi "
            f"{highest_weather['weather_name']} "
            f"({highest_weather['cnt']:,.2f} per hari), sedangkan terendah "
            f"pada kondisi {lowest_weather['weather_name']} "
            f"({lowest_weather['cnt']:,.2f} per hari). Perbedaan ini "
            f"menunjukkan keterkaitan, bukan bukti bahwa cuaca adalah "
            f"satu-satunya faktor yang memengaruhi permintaan."
        )

# Ringkasan bulanan
st.subheader("Monthly Rental Summary")
st.write(
    "Tabel berikut merangkum rata-rata penyewaan harian, total penyewaan, "
    "dan jumlah hari yang tercakup untuk setiap bulan berdasarkan filter aktif."
)

monthly = (
    filtered_df.groupby("month_num", as_index=False)
    .agg(
        Average_Rentals=("cnt", "mean"),
        Total_Rentals=("cnt", "sum"),
        Number_of_Days=("cnt", "count")
    )
)

monthly["Month"] = monthly["month_num"].apply(
    lambda m: pd.Timestamp(
        year=2000, month=m, day=1
    ).strftime("%B")
)

monthly = monthly[
    ["Month", "Average_Rentals", "Total_Rentals", "Number_of_Days"]
].rename(columns={
    "Average_Rentals": "Average Daily Rentals",
    "Total_Rentals": "Total Rentals",
    "Number_of_Days": "Number of Days"
})

st.dataframe(
    monthly.style.format({
        "Average Daily Rentals": "{:,.2f}",
        "Total Rentals": "{:,.0f}",
        "Number of Days": "{:,.0f}"
    }),
    use_container_width=True,
    hide_index=True
)

with st.expander("View Filtered Dataset"):
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

st.caption(
    "Data source: Bike Sharing Dataset (2011–2012). "
    "KPI, grafik, insight, dan tabel menyesuaikan filter yang dipilih. "
    "Interpretasi bersifat deskriptif dan tidak membuktikan hubungan sebab-akibat."
)
