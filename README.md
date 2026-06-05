# Svilia Mirage

> **"Observe the observer."**

**Svilia Mirage**, siber tehdit aktörlerini pasif ve aktif aldatma teknikleriyle izleyen, davranışsal istihbarat toplayan ve tehdit altyapılarını detaylı profilleyen **açık kaynaklı** bir siber deception ve threat intelligence framework'idir.

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-00A3E0)
![React](https://img.shields.io/badge/React-18-61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)
![Tailwind](https://img.shields.io/badge/TailwindCSS-3.4-06B6D4)

---

## 🇹🇷 Türkçe Dokümantasyon

### 1. Mimari Genel Bakış ve Amaç

Svilia Mirage, tehdit aktörlerinin dijital izlerini, davranışsal parmak izlerini ve operasyonel taktiklerini **"gözlemciyi gözlemleme"** prensibiyle çözen modüler bir siber istihbarat çerçevesidir.

> ⚠️ **YASAL UYARI & ETİK KULLANIM**  
> Bu yazılım **sadece** yetkili sızma testleri, phishing farkındalık eğitimleri, honeypot tabanlı akademik araştırmalar ve kontrollü siber laboratuvar ortamları için tasarlanmıştır.  
> Credential harvesting, exploit çalıştırma veya kalıcılık gibi saldırgan özellikler **içermez**. Tüm yasal sorumluluk kullanıcıya aittir.

### 2. Sistem Bileşenleri ve Yetenekleri

#### A. Aktif Yem ve Metadata Telemetrisi
- Gerçek zamanlı **IP, ASN, ISP, GeoLocation** istihbaratı
- Detaylı **HTTP Headers** ve **User-Agent** analizi
- Gelişmiş tarayıcı parmak izi (screen resolution, GPU fingerprint, languages vb.)
- Referrer zinciri takibi (Dark Web, forum, Telegram vb.)

#### B. Davranışsal Analiz Motoru
- Fare hareketleri, hover, tıklama koordinatları ve heatmap
- Sayfa kaydırma derinliği analizi
- Oturum süresi ve sekme geçiş analitiği
- Farklı ağlardan (VPN/Tor) yeniden ziyaret tespiti

#### C. Otomatik Playwright Recon
- Ters yönlendirme takibi (301/302, JS meta-refresh)
- Headless tarayıcı ile nihai hedef DOM snapshot’ları
- Tehdit altyapısının otomatik arşivlenmesi

---

## 🌐 English Version

### Architectural Overview and Purpose

Svilia Mirage is a modular open-source cyber deception and behavioral intelligence framework that decodes adversaries' digital footprints and tactical methodologies through passive and active deception.

> ⚠️ **LEGAL DISCLAIMER**  
> This tool is intended solely for authorized penetration testing, phishing awareness training, academic honeypot research, and controlled lab environments. It contains **no offensive capabilities**.

### Key Capabilities

**Active Bait & Telemetry**
- Real-time IP, ASN, ISP, Geolocation
- Advanced browser & hardware fingerprinting
- Referrer path analysis

**Behavioral Analysis Engine**
- Mouse tracking, click heatmaps, scroll depth
- Session duration & activity patterns
- Cross-VPN revisit correlation

**Automated Reconnaissance**
- Playwright-powered reverse redirect analysis
- DOM snapshot archiving of malicious destinations

---

## 🗂️ Klasör Yapısı

```text
svilia-mirage/
├── backend/                  # FastAPI Backend
│   ├── app/
│   │   ├── api/              # Tracking, Sessions, Analytics, Exports
│   │   ├── core/             # Tracker, GeoIP, Fingerprint, Correlation
│   │   ├── models/
│   │   ├── services/         # Playwright, Report, Analytics
│   │   └── templates/bait/   # Honeypot sayfaları (login, giveaway, verify)
│   ├── requirements.txt
│   └── .env.example
├── frontend/                 # React + TypeScript + Vite
│   ├── src/
│   │   ├── pages/            # Dashboard, Sessions, Heatmap, GraphView
│   │   ├── components/       # LiveMonitor, ThreatGraph, EventFeed
│   │   └── services/         # API + WebSocket
│   └── package.json
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
└── README.md

🚀 Kurulum
1. Docker ile En Kolay Yöntem (Önerilen)
Bashgit clone https://github.com/svilia/svilia-mirage.git
cd svilia-mirage

# Tek komutla tüm sistemi ayağa kaldır
docker-compose up --build -d
Not: Docker Compose ile backend, frontend, Redis ve SQLite otomatik olarak kurulur.
2. Manuel Kurulum
Backend
Bashcd backend

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
playwright install --with-deps

cp .env.example .env
# .env dosyasını düzenleyin (özellikle SECRET_KEY)
Sunucuyu başlatın:
Bashuvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
Frontend
Bashcd ../frontend

npm install
cp .env.example .env          # Varsa
npm run dev
Frontend varsayılan olarak http://localhost:5173 adresinde çalışır.

📡 İlk Kullanım

Tarayıcıda http://localhost:5173 adresine gidin.
Dashboard’da mevcut yem sayfalarını (bait) görebilirsiniz.
Bir yem linki oluşturup test etmek için Sessions sekmesini kullanın.
Gerçek zamanlı olay akışını Live Monitor üzerinden izleyin.


🛠️ Docker Komutları
Bashdocker-compose up --build -d      # Başlat
docker-compose logs -f            # Logları canlı izle
docker-compose down               # Tüm container'ları durdur
docker-compose restart            # Yeniden başlat

📋 Gereksinimler

Docker & Docker Compose (tavsiye edilen)
Veya:
Python 3.10+
Node.js 18+
Redis (opsiyonel)
Playwright tarayıcı bağımlılıkları



🛣️ Yol Haritası

Phase 1 (Tamamlandı): Çekirdek telemetri + FastAPI
Phase 2 (Devam Ediyor): Cytoscape.js Threat Correlation Graph
Phase 3 (Planlandı): AI tabanlı anomali tespiti ve Threat Scoring
Phase 4 (Gelecek): Tauri ile desktop uygulaması


🤝 Katkıda Bulunma

Projeyi fork edin
Feature branch oluşturun (git checkout -b feature/amazing-feature)
Değişikliklerinizi commit edin
Pull Request açın


📬 İletişim ve Destek
E-posta: sviliadestek@gmail.com

Made with ❤️ for the defenders.
Svilia Mirage — Observe the observer.
