# Audit: Lab 2 - Use Cases

## Метод

Порівняв use-case-діаграму, EARS-вимоги та матрицю трасування з spec.md і ER-моделлю (Lab 1).

## Розбіжності spec ↔ артефакт

### 1. Немає зовнішнього актора (зовнішня система)

**Знайдено:** v1 діаграми мала тільки Guest і User (обидва - люди). Spec вимагає >= 2 типи акторів (людина + зовнішня система/сервіс).

**Виправив:** додав Google OAuth як зовнішнього актора, пов'язав з UC2 (Login). Коміт: `fix - add google oauth actor + generalization`

### 2. Немає include/extend та узагальнення

**Знайдено:** v1 діаграми мала тільки прямі зв'язки актор -> use case. Немає include (обов'язковий під-сценарій), extend (опціональний), узагальнення (Guest extends User). Spec вимагає include/extend та узагальнення.

**Виправив:** додав UC9 (Authenticate) з include для UC2, UC3, UC5, UC6, UC7. Додав extend UC8 -> UC4 (Search extends Watch). Додав generalization Guest -.-> User. Коміт: `fix - add include extend relationships`

### 3. Матриця трасування 1:1 замість M:N

**Знайдено:** перша версія матриці мала зв'язки 1:1 (одна вимога -> один UC -> один Gherkin). Spec вимагає багато-до-багатьох. Наприклад REQ5 (like) має 2 Gherkin-сценарії, REQ8 і REQ9 обидва мапляться на UC5 (Comment).

**Виправив:** переписав матрицю - REQ5 -> UC6 + 2 Gherkin scenarios, REQ8/REQ9 -> UC5, REQ10 -> не покрито (пояснення). Додав REQ11 як непокриту вимогу з поясненням. Коміт: `add ears, user stories, gherkin, traceability`
