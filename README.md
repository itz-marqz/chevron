# 🛡️ Chevronukrainianstore — Custom E-Commerce & Telegram Automated Store

A robust, lightweight e-commerce web application tailored for custom embroidered patches and tactical chevrons. Built with a custom Python/Flask backend, dynamic frontend pricing logic, automated Telegram bot integration, and an automated Excel-to-JSON catalog pipeline.

---

## 🚀 Key Features

* **Dynamic Bulk Pricing Grid:** The server independently calculates and re-verifies total costs based on wholesale tiers (from 1 to 500+ items), preventing client-side price manipulation via DevTools.
* **Direct Telegram Bot Integration:** 
  * Instant order notifications sent directly to a manager's Telegram supergroup with formatted HTML messages.
  * Secure handling of custom design requests supporting image uploads (PNG, JPEG, WEBP, PDF up to 10MB) with automatic server-side cleanup.
  * Smart splitting for long descriptions exceeding Telegram's 1024-character caption limit.
* **Automated Catalog Pipeline (`convert.py`):** A custom Python script powered by `pandas` and `openpyxl` that converts raw Excel inventory files (`products.xlsx`) into structured JSON, complete with strict data validation, row-by-row error logging, and duplicate checks.
* **Secure File Handling:** Implements robust file validation, UUID-based renaming to prevent path traversal attacks, and safe resource cleanup (`finally` blocks).

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask, Gunicorn, Requests, Python-dotenv, Pandas, Openpyxl
* **Frontend:** HTML5, CSS3, Vanilla JavaScript, Responsive Design
* **Integrations:** Telegram Bot API

---

## 🧩 Challenges & Solutions (Engineering Highlights)

During the development of this project, several architectural and integration hurdles were successfully overcome:

1. **Telegram API Group Upgrade Error (`group_chat_id` vs `supergroup`):**
   * *Problem:* Transitioning the target chat triggered a `Bad Request: group chat was upgraded to a supergroup chat` error.
   * *Solution:* Traced update history via the Telegram Bot API (`getUpdates` endpoint) to capture the exact chat ID with the required `-100` prefix, ensuring seamless message delivery.
2. **Client-Side vs. Server-Side Price Trust:**
   * *Problem:* Relying on frontend totals leaves the checkout vulnerable to tampering.
   * *Solution:* Implemented an authoritative backend pricing function (`unit_price`) that recalculates order costs independently, adding a warning flag to manager notifications if client totals mismatch.
3. **Large File Management & Telegram Limits:**
   * *Problem:* Telegram restricts photo captions to 1024 characters and rejects oversized or improperly formatted files.
   * *Solution:* Built a two-tier fallback system: if an image fails `sendPhoto` or exceeds limits, it gracefully downgrades to `sendDocument`, sending long text blocks as separate messages.

---

## ⚙️ Getting Started Locally

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/chevron-shop.git](https://github.com/YOUR_USERNAME/chevron-shop.git)
cd chevron-shop
