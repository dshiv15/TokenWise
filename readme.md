# 🚀 TokenWise: Real-Time Wallet Intelligence on Solana

**TokenWise** is a real-time wallet intelligence tool built to monitor and analyze wallet behavior for a specific Solana token. It fetches top wallet holders, tracks token transactions, and visualizes insights through a custom **neon-themed Streamlit dashboard**.

---

## 📌 Project Overview

### 🔧 Backend
- Developed with **Node.js** and **TypeScript**.
- Uses `@solana/web3.js` for blockchain interaction.
- Simulates top holders and transaction data for reliability in demos.
- Stores data in a local **SQLite** database.

### 💡 Frontend
- Built with **Streamlit**.
- Neon-themed interface (purple/green) with tabbed navigation.
- Features:
  - Buy/Sell metrics & net direction
  - Protocol distribution (Jupiter, Raydium, Orca)
  - Active wallet tracking
  - Time-range filtering (1–30 days)
  - Export options: CSV & JSON

### 🎯 Purpose
TokenWise offers **actionable insights** into token-level wallet activity. It’s designed for **technical evaluations**, showcasing blockchain integration, real-time analytics, and UI creativity.

---

## 📁 File Structure

```
TokenWise/
├── backend/
│   ├── src/
│   │   ├── index.ts            # Main backend logic
│   │   ├── solana.ts           # Simulated Solana data fetching
│   │   ├── database.ts         # SQLite operations
│   │   ├── types.ts            # TypeScript interfaces
│   ├── package.json            # Node.js dependencies
│   ├── tsconfig.json           # TypeScript configuration
│   ├── tokenwise.db            # SQLite database (generated at runtime)
├── dashboard/
│   ├── app.py                  # Streamlit dashboard logic
│   ├── requirements.txt        # Python dependencies
├── data/
│   ├── transactions.json       # Sample JSON export
│   ├── transactions.csv        # Sample CSV export
├── presentation/
│   ├── TokenWise_Presentation.pptx  # Project pitch deck
├── README.md                   # Project documentation (this file)
```

---

## ✅ Prerequisites

Ensure the following are installed:

- [Node.js](https://nodejs.org/) (v18+)
- [Python](https://www.python.org/) (v3.8+)
- SQLite (pre-installed with Python)
- Internet connection (for dependency installation)

---

## ⚙️ Setup Instructions

### 1. Backend Setup

```bash
cd backend
npm install
npm start
```

- Simulates wallet transactions every 5 seconds
- Stores data in `backend/tokenwise.db`

### 2. Dashboard Setup

```bash
cd dashboard
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Dashboard Features

### Key Modules:

- **Market Metrics**: Track total buys, sells & net direction (buy-heavy/sell-heavy).
- **Protocol Usage**: See usage distribution across Jupiter, Raydium, and Orca.
- **Active Wallets**: Identify most active addresses.
- **Time Filtering**: Select transactions from the past 1 to 30 days.
- **Data Export**:
  - `transactions.json`: JSON format
  - `transactions.csv`: Spreadsheet-friendly CSV

---

## 📂 Sample Output

### `data/transactions.json`

```json
[
  {
    "signature": "4sd...7K",
    "timestamp": "2025-07-08T10:20:00Z",
    "wallet": "3Gf...Yo",
    "amount": 1234.56,
    "isBuy": true,
    "protocol": "Jupiter"
  },
]
```

### `data/transactions.csv`

```
signature,timestamp,wallet,amount,isBuy,protocol
4sd...7K,2025-07-08T10:20:00Z,3Gf...Yo,1234.56,TRUE,Jupiter
...
```

---

## 🧠 Use Case

TokenWise is ideal for:
- Token teams looking for **holder insights**
- Researchers & analysts studying **Solana wallet behavior**
- Demonstrating skills in **blockchain, data visualization, and full-stack dev**

---

## 👨‍💻 Author

**Shiv Dixit**

---

## 📄 License

This project is licensed for evaluation and demo purposes. Reach out for extended usage rights.

---

Feel free to ⭐ the repo if you find it useful!
