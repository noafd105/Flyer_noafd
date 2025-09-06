# FlyerNoAfD

[toc]

## Inhalt

Das Projekt beinhaltet eine Startseite, die bei Verbindung mit dem WLAN mithilfe der `main.py` eine Weiterleitung auf eine Registrierungsseite durchführt.
Diese Seite ist einer AfD-Website nachempfunden. Durch das Absenden des Formulars werden die eingegebenen Daten in der Datei `/daten/daten.txt` auf dem Raspberry Pi Pico W gespeichert. Dies ist datenschutzrechtlich bedenklich.

Die unter „Datenschutzeinstellungen“ aufgeführten Einstellungen sollten rechtlich überprüft werden, da die Korrektheit und Rechtsgültigkeit hier nicht sichergestellt sind.

Unter `thetruth.html` sind einige Zitate von AfD-Politikern mit Anmerkungen und den Namen der Politiker aufgeführt. Außerdem sind hier zwei KI generierte „Sharepics“ enthalten.

## Zweck

Die Idee hinter dem Projekt ist es, AfD-Wähler mit den Aussagen der Politiker per digitalem Flugblatt zu konfrontieren und so einen Umdenkprozess einzuleiten.

## Benötigte Materialien

- Raspberry Pi Pico W
- Eine Powerbank (zur Spannungsversorgung)

## Durchzuführende Schritte

1. **MicroPython installieren**
   Auf dem Raspberry Pi Pico W muss [MicroPython](https://micropython.org/download/RPI_PICO_W/) installiert werden.

2. **Projekt und Bibliotheken laden**
   - Das Projekt muss auf den Raspberry Pi Pico W geladen werden.
   - Zusätzlich wird die Bibliothek [phew v0.0.3](https://github.com/pimoroni/phew/releases/tag/v0.0.3) benötigt.

3. **IDE einrichten**
   Als Entwicklungsumgebung eignet sich [Thonny](https://thonny.org/).

---
