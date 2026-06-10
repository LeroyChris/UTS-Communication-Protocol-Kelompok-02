# UTS Communication Protocol - Kelompok 02

## Identitas Kelompok
Mata Kuliah: Communication Protocol  
Program Studi: Sains Data  
Kelas: Reguler  
Tema: API Request, Data Encoding, and Packet Capture

## Anggota dan Role
| Nama | NIM | Role |
|---|---|---|
| Zahir Ali Izzaturahman | 25110500021 | Role 1 - API Tester dan Postman Collection |
| Stephanus Teo | 25110500013 | Role 2 - Packet Capture dan Troubleshooting Evidence |
| Enrico Lazuardi | 2511050027 | Role 3 - Data Format Analysis dan Python Parsing |
| Leroy Christopher Gerson | 25110500025 | Role 4 - Report, PPT, GitHub Structure, dan Backup Presenter |

## Case yang Dipilih
Case A - REST API JSON  

## Ringkasan Project
Project ini menguji komunikasi API menggunakan request GET dan POST, menganalisis response JSON, melakukan packet capture menggunakan Wireshark, melakukan parsing data menggunakan Python, dan menyusun evidence dalam bentuk report, PPT, repository, serta reflection individu.

## Struktur Folder
- `/postman` berisi Postman Collection.
- `/capture` berisi file packet capture `.pcapng`.
- `/screenshots` berisi screenshot request-response, packet analysis, dan output Python.
- `/python` berisi script parsing data.
- `/output` berisi output CSV hasil parsing.
- `/report` berisi report PDF final.
- `/ppt` berisi file presentasi.
- `/reflection` berisi reflection individu masing-masing anggota.

## Endpoint yang Digunakan
Base URL:
http://127.0.0.1:8088

Endpoint utama:
- GET /api/products
- GET /api/users
- POST /api/profiles
- POST /api/orders
- GET /api/transactions

## Cara Menjalankan Script Python
```bash
pip install requests pandas
python python/parsing_script.py
```

Output akan tersimpan di:
output/parsed_result.csv

## Link Deliverables
- Report PDF: /report/UTS_CP_Reguler_Kelompok02_Report.pdf
- PPT: /ppt/UTS_CP_Reguler_Kelompok02_Presentation.pptx
- Postman Collection: /postman/UTS_CP_Reguler_Kelompok02_Postman_Collection.json
- Packet Capture: /capture/UTS_CP_Reguler_Kelompok02_Capture_Role2.pcapng