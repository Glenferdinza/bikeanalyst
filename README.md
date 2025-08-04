# Proyek Analisis Data: Bike Sharing Dataset

## Live Demo
Link: https://bikeanalyst-v1.streamlit.app/

## Petunjuk Penggunaan

 Clone Repository
   ```bash
   git clone https://github.com/Glenferdinza/Semua-jenis-File.git
   cd Semua-jenis-File


## Pengaturan Lingkungan - Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
pip install streamlit pandas numpy seaborn matplotlib

## cek versi python
python --version

## Setup Environment apabila menggunakan venv
```bash
python -m venv main-ds
# Jika menggunakan windows:
main-ds\Scripts\activate
# Jika menggunakan macOS/linux:
source main-ds/bin/activate
pip install -r requirements.txt
python --version
```

## Menjalankan Aplikasi Streamlit
Gunakan perintah berikut untuk menjalankan aplikasi Streamlit:
```bash
streamlit run dashboard.py
```

## Jika menggunakan IDE berupa VS Code:
- Buka VS Code.
- Buka folder proyek yang sudah di ekstrak menjadi Folder bernama Tugas proyek akhir Dicoding_glenferdinza_efian
- Jika sudah buka file bernama dashboard
- Setelah membuka file bernama dashboard, pilih file bernama dashboard.py
- Setelah membuka file bernama dashboard.py, buka terminal dan jalankan perintah berikut:
```bash
streamlit run dashboard.py
```


## File Notebook
Proyek ini juga dilengkapi dengan sebuah file notebook bernama Proyek_Analisis_Data_Bike-sharing-dataset_Glenferdinza_Efian.ipynb. File berisikan:
- Visualisasi data untuk menyampaikan temuan-temuan penting.

### Cara Menggunakan File Notebook
- Pastikan sudah menginstal Jupyter Notebook atau JupyterLab.
- Aktifkan environment-Nya :
   ```bash
   conda activate main-ds
   ```
   atau
   ```bash
   pipenv shell
   ```
- Jalankan Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
- Buka file Proyek_Analisis_Data_Bike-sharing-dataset_Glenferdinza_Efian.ipynb di browser.

## Nah sekarang apabila mau membuka file berjenis pylancenya( Jupiter ) maka:
- Buka VS Code.
- Buka folder proyek yang sudah di ekstrak menjadi Folder bernama Tugas proyek akhir Dicoding_glenferdinza_efian
- Jika sudah buka file bernama Data
- Setelah membuka file bernama Data, pilih file bernama Proyek_Analisis_Data_Bike-sharing-dataset_Glenferdinza_Efian.ipynb
- Dan dapat dilihat  secara langsung outputnya

### Isi Utama Notebook
- Pembersihan Data: Langkah-langkah untuk membersihkan dan mempersiapkan data.
- Visualisasi Data: Grafik dan visualisasi interaktif untuk mendukung analisis.
- Modeling: Penerapan model prediksi untuk memperkirakan jumlah penyewaan sepeda.

