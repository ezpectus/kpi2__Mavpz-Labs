# Audit: Lab 2 - Use Cases

## Метод

Порівняв use-case-діаграму, EARS-вимоги та матрицю трасування з spec.md і ER-моделлю (Lab 1). Кожна розбіжність: який критерій у spec був неточним/відсутнім -> як уточнив -> коміти. Топ-3 за шаблоном завдання — №1–3; №4 знайдено при фінальному рев'ю і додано чесно окремо.

## Розбіжності spec ↔ артефакт

### 1. Немає зовнішнього актора (зовнішня система)

**Критерій spec:** «>= 2 типи акторів (людина + зовнішня система)» — був у spec з `3625304`; уточнено прив'язку Google OAuth до UC9 комітом `fdba085`.
**Знайдено:** v1 діаграми мала тільки Guest і User (обидва люди). Вимога REQ2 каже про Google OAuth — на діаграмі його не було.
**Виправив:** додав Google OAuth як зовнішнього актора, пов'язав з автентифікацією.
**Коміт-модель:** `5ee5cb1` — lab2: fix - add google oauth actor + generalization

### 2. Немає include/extend та узагальнення

**Критерій spec:** «діаграма з include/extend та узагальненням» — був у spec; про напрямок generalization явно нічого не стояло (цим скористалась знахідка №4) — уточнено `fdba085`.
**Знайдено:** v1 мала тільки прямі зв'язки актор -> UC. Немає include (обов'язковий під-сценарій), extend (опційний), узагальнення.
**Виправив:** UC9 Authenticate з include для UC2/3/5/6/7; extend UC8 -> UC4; generalization між Guest і User.
**Коміт-модель:** `d7dad19` — lab2: fix - add include extend relationships

### 3. Матриця трасування 1:1 замість M:N

**Критерій spec:** «матриця трасування багато-до-багатьох» + «>= 1 непокрита вимога з поясненням» — були в spec.
**Знайдено:** перша матриця мала зв'язки 1:1 (вимога -> UC -> Gherkin) і все покрито.
**Виправив:** REQ5 -> UC6 + 2 Gherkin-сценарії, REQ8/REQ9 -> UC5, REQ10 і REQ11 непокриті з поясненнями.
**Коміт-артефакт:** `c9cee4e` — lab2: add ears, user stories, gherkin, traceability

### 4. Узагальнення у зворотньому напрямку в .mmd + Register/Login на неправильному акторі (знайдено при фінальному рев'ю)

**Критерій spec:** відсутній — додано «узагальнення дитина -> батько (User --|> Guest), ідентично в .mmd і .drawio» і «UC асоційовані з актором, що їх реально виконує».
**Знайдено:** (a) у `usecase.mmd` стояло `Guest -.->|generalization| User` — читається «Guest є різновидом User», а в `usecase.drawio` стрілка йшла правильно User -> Guest: два артефакти однієї моделі суперечили. (b) UC1 Register і UC2 Login були асоційовані з User — а реєструється саме Guest (зареєстрований User не може реєструватись). User stories US3/US4 казали «As a User» про реєстрацію — та сама розбіжність у requirements.md.
**Виправив:** `User -.->|generalization| Guest` у .mmd; UC1/UC2 переприв'язані до Guest; US3/US4 -> «As a Guest»; PNG перерендерено; drawio синхронно.
**Коміт spec+модель:** `fdba085` — lab2: spec+model - guest owns register/login + generalization direction fix (один коміт змінює spec.md, usecase.mmd, usecase.drawio, requirements.md, renders/usecase.png)
