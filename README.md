# OTE-Data-Logger
Software that reads Modbus data, analyzes the data, stores it in a database and controls embedded systems of photovoltaic power plants.

📡 OTE Data Logger – README
Tento projekt slouží k monitorování, ukládání a exportu elektrických veličin ze zařízení komunikujících přes Modbus, s možností reakce na cenu elektřiny dle OTE (Operátor trhu s elektřinou) a následné odesílání exportovaných dat e-mailem.

📂 Obsah projektu
•	modbusman.py – hlavní skript pro čtení dat z Modbus zařízení a ovládání relé dle cen elektřiny z OTE.
•	vytvorxmlzdb.py – generuje XML export dat z databáze pro aktuální den.
•	odesliemail.py – odešle vygenerovaný XML soubor e-mailem na definovaného příjemce.
________________________________________
🔧 modbusman.py – hlavní řídicí skript
Funkce:
•	Čtení elektrických parametrů (frekvence, napětí, proudy, výkony, import/export energie) ze zařízení přes Modbus.
•	Ukládání hodnot do SQLite databáze
•	Automatické ovládání relé na základě:
o	výpadku napájení (nadfrekvence, podfrekvence, podpětí, přepětí).
o	aktuálních cen energie dle XLSX souborů OTE.
•	Automatická detekce výpadků a odeslání upozornění e-mailem (spuštěním skriptu pro odeslání notifikace e-mailem).
•	Reakce na nízké ceny energie (např. < 10 EUR/MWh) a zapnutí zařízení přes USB relé.
Závislosti:
•	pymodbus
•	openpyxl
•	usbrelay_py
•	sqlite3
•	subprocess, datetime, time, struct
________________________________________
🧾 vytvorxmlzdb.py – generátor XML exportu
Funkce:
•	Vytvoří XML soubor obsahující všechny záznamy z databáze  aktuálního dne.
•	Výstupní soubor se ukládá do ~/OTE/XMLfiles/ s názvem ve formátu export_YYYY-MM-DD_HH:MM.xml.
Použití:
Spustit samostatně nebo v cronu k naplánovanému exportu.
Příklad Crontabu:
59 23 * * * python3 ~/OTE/vytvorxmlzdb.py
59 23 * * * python3 ~/OTE/odesliemail.py
0 */1 * * * /usr/bin/bash ~/OTE/dwnfileote.sh >> ~/cronLogDwnfileote.txt 2>&1
________________________________________
📧 odesliemail.py – odeslání e-mailem
Funkce:
•	Odesílá e-mailem vygenerovaný XML soubor na definovanou adresu.
•	E-mail obsahuje přílohu a základní text.
Parametry:
•	Odesílatel: root820429@gmail.com
•	Příjemce: 
•	SMTP server: Gmail (smtp.gmail.com:465)
________________________________________
✅ Doporučená konfigurace a použití
•	Perioda spouštění hlavního skriptu: běží v nekonečné smyčce, každých 5 sekund.
•	Perioda exportu XML: jednou denně (např. pomocí cron).
•	Odesílání e-mailu: ihned po vytvoření exportu, také vhodné plánovat pomocí cron.
________________________________________
📌 Předpoklady
•	Linuxový systém s přístupem k USB zaříení (Modbus převodník, USB relé).
•	Cesty v kódu jsou absolutní a přizpůsobeny konkrétnímu uživateli. Před použitím upravte podle svého systému.
•	Databáze se vytvoří při prvním spuštění programu. V případě změny kódu, který má vliv na databázi a pokud je to žádoucí, změňte název databáze na nový.
