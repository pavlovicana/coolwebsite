# 🐳 WordPress WooCommerce Docker Project

Ovo je **WordPress + WooCommerce** sajt spakovan za lokalni razvoj pomoću Docker-a.  
Sadrži sve što je potrebno da se identična kopija podigne na bilo kojoj mašini.

---

## 📦 Sadržaj projekta

- `docker-compose.yml` – definiše WordPress i MySQL kontejnere  
- `dump.sql` – export baze sa svim WooCommerce podacima (proizvodi, porudžbine, podešavanja)  
- `wp-content/` *(opciono)* – pluginovi (uključujući WooCommerce), teme, slike proizvoda  
- `sample-data/woocommerce-products.xml` – WooCommerce sample data XML fajl za uvoz proizvoda  

---

## 🚀 Kako pokrenuti lokalno

1️⃣ Kloniraj ovaj repozitorijum:

```bash
git clone https://github.com/<YOUR-USERNAME>/<YOUR-REPO>.git
cd <YOUR-REPO>

2️⃣ Pokreni kontejnere:

bash
Copy
Edit
docker-compose up -d
3️⃣ Importuj bazu:

bash
Copy
Edit
docker exec -i wordpresssite-db-1 mysql -u root -prootpassword wordpress < dump.sql
4️⃣ Otvori WordPress u browseru:

➡️ http://localhost:8000

🛠 Kako importovati WooCommerce sample data
Ukoliko želiš da ponovo importuješ WooCommerce sample data proizvode:

U WordPress admin panelu idi na:
WooCommerce > Products > Import

Izaberi XML fajl koji se nalazi u projektu:
sample-data/woocommerce-products.xml

Sledeći koraci u importu će omogućiti WordPress-u da preuzme slike proizvoda sa originalnih URL-ova.

