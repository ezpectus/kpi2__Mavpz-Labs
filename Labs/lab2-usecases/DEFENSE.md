# DEFENSE: Lab 2 - Use Cases

## 1. Намір і критерії

Описав вимоги до VideoHub: EARS-вимоги, user stories, Gherkin-сценарії, use-case-діаграма, матриця трасування M:N. Критерії в spec.md - >=2 типи акторів (людина + зовнішня система), include/extend і узагальнення на діаграмі, >=1 непокрита вимога з поясненням, узгодженість з ER-моделлю Lab 1.

## 2. Топ-3 розбіжності (знайшов і виправив)

1. **Не було зовнішнього актора** - проти критерію ">=2 типи акторів (людина + зовнішня система)". Вимога REQ2 каже про Google OAuth, а на діаграмі його не було. Додав Google OAuth як зовнішню систему + generalization Guest --|> User. -> commit `5ee5cb1` (lab2: fix - add google oauth actor + generalization)
2. **Не було include/extend** - проти критерію "діаграма з include/extend та узагальненням". Додав UC9 Authenticate (include для UC2/3/5/6/7 - всі UC що вимагають auth) і UC8 Search --|extend|> UC4 Watch. -> commit `d7dad19` (lab2: fix - add include extend relationships)
3. **Матриця трасування 1:1, все покрито** - проти критеріїв "матриця M:N" і ">=1 непокрита вимога з поясненням". Переписав матрицю на M:N, додав непокриту REQ11 з поясненням. -> commit `c9cee4e` (lab2: add ears, user stories, gherkin, traceability)

## 3. Ключове рішення

Mermaid graph замість PlantUML usecase. PlantUML має стандартну UML-нотацію (еліпси, stickman-актори) але не рендериться в GitHub без плагіна. Mermaid рендериться нативно, нотація не стандартна - компенсую текстом у spec.md і легендою на діаграмі. Деталі: adr/adr-002-usecase-notation.md

## 4. Перевірка узгодженості з попередньою моделлю (Lab 1)

Порівняв кожну сутність ER-моделі з use cases:

- User -> актор User, UC1 Register, UC2 Login
- Video -> UC3 Upload, UC4 Watch
- Comment -> UC5 Comment
- Like -> UC6 Like
- Subscription -> UC7 Subscribe
- googleId в User -> актор Google OAuth

Кожна сутність покрита хоча б одним UC, кожен UC спирається на сутність з Lab 1. Деталі в AUDIT.md.
