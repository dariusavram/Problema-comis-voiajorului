# Algoritm Genetic pentru Problema Comis-Voiajorului (TSP)

## Descriere
Această aplicație implementează un **algoritm genetic** pentru rezolvarea **Problemei Comis-Voiajorului (TSP)**. Scopul este de a găsi cea mai scurtă rută între un set de orașe, pornind și revenind la un oraș-sediu, utilizând o matrice de distanțe predefinită.

## Funcționalități
- **Încărcarea unei matrice de distanțe** dintr-un fișier.
- **Generarea unei populații inițiale** de rute aleatorii.
- **Calculul fitness-ului** pentru fiecare rută pe baza distanței totale parcurse.
- **Selecție prin turnir** – alege cei mai buni candidați pentru reproducere.
- **Încrucișare și mutație** pentru generarea noilor soluții.
- **Evoluția generațiilor** pentru optimizarea traseului.
- **Identificarea și afișarea celei mai bune rute** după un număr specificat de generații.

## Structura Codului
- **`GeneticAlgorithm`** – clasa principală care implementează algoritmul genetic.
  - `load_distances(cale_fisier)` – încarcă matricea de distanțe dintr-un fișier text.
  - `genereaza_populatie_initiala()` – creează rute inițiale aleatorii.
  - `calculeaza_fitness(ruta)` – calculează lungimea totală a unei rute.
  - `turnir(generatie, k=2)` – selectează părinții pentru reproducere.
  - `incrucisare(parinte1, parinte2)` – creează doi copii din doi părinți.
  - `mutatie(individ, sansa_mutatie)` – aplică mutații asupra unei rute.
  - `evolueaza_generatie(sansa_mutatie)` – creează o nouă generație de rute.
  - `ruleaza_generatii(numar_generatii, sansa_mutatie)` – rulează simularea și afișează cea mai bună rută găsită.

## Configurare și Rulare
1. **Asigură-te că ai Python instalat** (versiunea 3.x).
2. **Instalează biblioteca Matplotlib** (opțional, pentru vizualizare):
   ```sh
   pip install matplotlib numpy
   ```
3. **Pregătește fișierul `distante.txt`** – conține matricea de distanțe dintre orașe.
4. **Rulează scriptul**:
   ```sh
   python3 main.py
   ```

## Parametri de Configurare
- **`orase`** – lista orașelor incluse în problemă.
- **`sediu`** – orașul de plecare și sosire.
- **`populatie`** – numărul de rute generate în fiecare generație.
- **`numar_generatii`** – câte iterații va rula algoritmul.
- **`sansa_mutatie`** – procentul de mutație aplicat rutelor noi.

## Exemplu de Output
```
Cea mai bună soluție după 3000 generații:
Rută: [Baia Mare, Cluj, Oradea, Timișoara, București, Constanța, Galați, Iași, Brașov, Craiova, Baia Mare] 
Fitness (distanță totală): XXXX km
```

