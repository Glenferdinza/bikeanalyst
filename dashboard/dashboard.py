import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Header: Proyek Analisis Data: Bike Sharing Dataset
st.header("Analisis Data: Bike Sharing Dataset")

# Header: Menentukan Pertanyaan Bisnis
st.header("Pertanyaan Bisnis")

st.write("""
1. Bagaimana pengaruh faktor lingkungan dan cuaca (seperti suhu, kelembapan, dan kondisi cuaca) terhadap jumlah penyewaan sepeda harian atau jam-jam tertentu?  
2. Apakah terdapat pola anomali dalam jumlah penyewaan sepeda yang dapat dikaitkan dengan kejadian besar atau kondisi khusus, seperti bencana atau hari libur nasional?  
""")

# Load data
def load_data():
    day_df = pd.read_csv("https://raw.githubusercontent.com/Glenferdinza/Semua-jenis-File/refs/heads/main/day.csv")
    hour_df = pd.read_csv("https://raw.githubusercontent.com/Glenferdinza/Semua-jenis-File/refs/heads/main/hour.csv")
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    return day_df, hour_df

day_df, hour_df = load_data()

day_df.head()
hour_df.head()
# Missing values

day_df.isnull().sum()

hour_df.isnull().sum()

# Cek kategori cuaca
day_df['weathersit'].unique()

# Statistik deskriptif
day_df.describe()

hour_df.describe()

# Korelasi variabel numerik di Data Day
correlation = day_df[['temp', 'hum', 'cnt']].corr()
print(correlation)

# Deteksi anomali dengan Z-Score di Data Hour
mean_cnt = np.mean(hour_df['cnt'])
std_cnt = np.std(hour_df['cnt'])
hour_df['z_score'] = (hour_df['cnt'] - mean_cnt) / std_cnt

hour_df[['cnt', 'z_score']].head()

# Fitur Interaktif: Filter berdasarkan tanggal
st.sidebar.header("Filter Data")
selected_date = st.sidebar.date_input("Pilih Tanggal", value=pd.to_datetime("2012-01-01"))
filtered_hour_df = hour_df[hour_df['dteday'] == pd.to_datetime(selected_date)]

st.header("Jawaban untuk Pertanyaan Bisnis 1")
# Visualisasi hubungan suhu dengan jumlah penyewaan sepeda
st.subheader("Hubungan Suhu dengan Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=day_df, color='blue', ax=ax)
ax.set_title('Hubungan Suhu dengan Jumlah Penyewaan Sepeda')
ax.set_xlabel('Suhu (Celsius)')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)
with st.expander("Insight dari Scatter plot diatas mengenai Hubungan Suhu dan Penyewaan Sepeda"):
    st.write("Melalui scatter plot dapat disimpulkan terdapat adanya tren positif, yang mana semakin tinggi suhu, jumlah penyewaan sepeda cenderung meningkat.")

# Visualisasi hubungan kelembapan dengan jumlah penyewaan sepeda
st.subheader("Hubungan Kelembapan dengan Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='hum', y='cnt', data=day_df, color='green', ax=ax)
ax.set_title('Hubungan Kelembapan dengan Jumlah Penyewaan Sepeda')
ax.set_xlabel('Kelembapan (%)')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)
with st.expander("Insight dari Scatter plot diatas mengenai Hubungan Kelembapan dan Penyewaan Sepeda"):
    st.write("Melalui scatter plot ini memperlihatkan adanya tren negatif, yang menunjukkan bahwa kelembapan tinggi cenderung menurunkan minat untuk menyewa sepeda.")

st.header("Jawaban untuk Pertanyaan Bisnis 2")
# Visualisasi pola jumlah penyewaan sepeda per jam
st.subheader("Pola Jumlah Penyewaan Sepeda per Jam")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=filtered_hour_df, color='orange', ax=ax)
ax.set_title('Pola Jumlah Penyewaan Sepeda per Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)
with st.expander("Insight dari Plot pada Pola Penyewaan per Jam diatas"):
    st.write("Plot menunjukkan pola waktu puncak di pagi dan sore hari, menunjukkan penggunaan sepeda yang signifikan untuk perjalanan kerja atau sekolah.")

# Visualisasi deteksi anomali (Z-Score) per jam
st.subheader("Deteksi Anomali Jumlah Penyewaan Sepeda per Jam")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hr', y='z_score', data=filtered_hour_df, color='red', ax=ax)
ax.set_title('Deteksi Anomali Jumlah Penyewaan Sepeda per Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Z-Score')
ax.axhline(y=3, color='black', linestyle='--', label='Threshold (3)')
ax.axhline(y=-3, color='black', linestyle='--')
ax.legend()
st.pyplot(fig)
with st.expander("Insight dari Plot Deteksi Anomali per Jam diatas ini"):
    st.write("Plot Z-Score menunjukkan adanya jam-jam tertentu dengan anomali ekstrem, yang mungkin disebabkan oleh event mendadak atau perubahan cuaca.")

# Header: Conclusion
st.header("Conclusion")

# Insight Conclusion
st.write("Dari analisis yang telah dilakukan, dapat disimpulkan bahwa:")
st.write("1. Pengaruh faktor lingkungan dan cuaca (seperti suhu, kelembapan, dan kondisi cuaca) terhadap jumlah penyewaan sepeda harian atau jam-jam tertentu adalah signifikan.")
st.write("2. Terdapat pola anomali dalam jumlah penyewaan sepeda yang dapat dikaitkan dengan kejadian besar atau kondisi khusus, seperti bencana atau hari libur nasional, namun tetap memerlukan investigasi lebih lanjut lagi mengenai penyebab-Nya.")

