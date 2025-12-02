# ♻️ RecycleHub – Flask Based Waste Management App

RecycleHub adalah aplikasi berbasis **Flask + MySQL** untuk membantu pengelolaan sampah rumah tangga secara lebih bertanggung jawab sesuai **SDG 12 – Responsible Consumption & Production**.

---

## 🚀 Fitur Utama
- **Manajemen User** (registrasi, login, role admin/user)
- **Permintaan Pickup Sampah** (CRUD)
- **Manajemen Bank Sampah** (CRUD)
- Dashboard sederhana

---

## 🛠️ Teknologi yang Digunakan
- **Python Flask** (backend)
- **MySQL** (database)
- **HTML, CSS, JS** untuk UI dasar
- **MySQL Connector** untuk integrasi database
- **Git / GitHub** untuk version control

---

## 🗂️ Struktur Folder
```
RecycleHub/
│── app.py
│── /templates
│── /static
│── /config.py
│── /database
│     └── recyclehub.sql
│── README.md
```

---

## 🧩 Instalasi & Setup
### 1️⃣ Clone Repository
```
git clone https://github.com/USERNAME/RecycleHub.git
cd RecycleHub
```

### 2️⃣ Buat Virtual Environment
```
python -m venv venv
venv/Scripts/activate   # Windows

Nyalakan setiap ingin menjalankan project 
.\venv\Scripts\python app.py
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Import Database
- Buka **phpMyAdmin / MySQL Workbench**
- Buat database: `recyclehub_db`
- Import file: `database/recyclehub.sql`

---

## 🗃️ Struktur Database
### 📌 Tabel: `users`
```
id (PK)
name
email
password
role
created_at
```

### 📌 Tabel: `bank_sampah`
```
id (PK)
nama
alamat
kota
kontak
```

### 📌 Tabel: `pickup_request`
```
id (PK)
user_id (FK)
bank_id (FK)
jenis_sampah
berat
status
created_at
```

---

## ▶️ Menjalankan Aplikasi
```
python app.py
```
Buka di browser:  
http://127.0.0.1:5000/

---

## 🌱 Branch Workflow
Gunakan branch terpisah untuk setiap fitur:
```
git checkout -b feature/users
git checkout -b feature/pickup
git checkout -b feature/bank-sampah
```
Merge ke main setelah selesai.

---

## 📄 Lisensi
Project ini bersifat open-source dan dapat dikembangkan untuk kebutuhan penelitian, kompetisi, atau pembelajaran.

---

Jika ingin ditambahkan badge, screenshot, atau dokumentasi API, tinggal bilang saja!
