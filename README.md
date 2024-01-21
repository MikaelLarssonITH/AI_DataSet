# Prediktivt Underhåll Genom Maskininlärning

Denna GitHub-repository innehåller Python-kod och tillhörande filer för ett maskininlärningsprojekt som syftar till att förutsäga underhållsbehov i industriell utrustning baserat på data om energiförbrukning och vridmoment. Projektet använder en Random Forest-klassificerare för att göra förutsägelser.

## Projektöversikt

Detta projekt innefattar analys av industriell driftdata för att förutsäga underhållskrav. Genom att identifiera mönster i energiförbrukning och vridmomentsmätningar, syftar modellen till att flagga potentiella underhållsbehov, vilket minskar driftstopp och förbättrar effektiviteten i industriella operationer.

## Komma Igång

Dessa instruktioner hjälper dig att få en kopia av projektet igång på din lokala maskin för utveckling och testning.

### Förutsättningar

Innan du kör projektet, se till att du har Python installerat på ditt system. Om inte, ladda ner och installera Python från [python.org](https://www.python.org/downloads/).

### Installation

1. **Klona Repositoryt**

   ```bash
   git clone https://github.com/dittanvandarnamn/predictive-maintenance.git
   cd predictive-maintenance

### Ställ In en Virtuell Miljö (Valfritt men rekommenderat)

2.1 **För Windows:**

  ```bash
  python -m venv venv
  .\venv\Scripts\activate
```

2.2 **För macOS och Linux:**

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

3. **Installera Nödvändiga Paket**

Installera alla nödvändiga paket med pip:
  ```bash
  pip install pandas numpy scikit-learn
  ```

## Köra Koden
För att köra den prediktiva modellen, navigera till projektets katalog och kör Python-skriptet:
```bash
python predictive_maintenance.py
```

## Data
Datan som används i detta projekt finns i filen Drive_data_Jan-Feb.csv. Denna fil inkluderar mätningar av energiförbrukning (kWh) och vridmoment (Nm) tillsammans med tidsstämplar och underhållsflaggor.
