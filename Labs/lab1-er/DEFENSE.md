# DEFENSE: Lab 1 - ER-модель VideoHub

## 1. Намір і критерії

Змоделював дані відеоплатформи VideoHub як ER-модель: 5 сутностей, зв'язки 1:N і M:N, первинні/зовнішні ключі, unique-обмеження. Критерії прийняття зафіксовані в spec.md - коректні кардинальності, M:N тільки через асоціативні сутності, 3NF, рендер відповідає spec.

Домен обрав бо VideoHub - мій реальний проєкт (YouTube-клон): в ньому одразу є всі типи зв'язків для демонстрації (1:N, M:N через асоціативну сутність, self-referencing). Нормалізація - 3NF: всі атрибути атомарні, PK одиночні, неключові атрибути залежать тільки від PK - немає транзитивних залежностей (напр. в Video тримаємо authorId FK, а не дублюємо ім'я автора).

## 2. Топ-3 розбіжності (знайшов і виправив)

1. **Like як прямий M:N** - `User }|--|{ Video` без асоціативної сутності, проти критерію spec "M:N через Like (асоціативна сутність)". Розгорнув через Like: `User ||--o{ Like`, `Video ||--o{ Like`. -> commit `6a26223` (lab1: fix - like as associative entity)
2. **Subscription як прямий M:N self-ref** - та сама помилка: `User }|--|{ User` напряму, проти критерію "M:N через Subscription". Розгорнув через Subscription з двома FK на User (subscriberId, channelId). -> commit `c319a9d` (lab1: fix - subscription as associative entity + unique note)
3. **Unique-обмеження не показані** - проти критеріїв spec про unique на (userId, videoId), (subscriberId, channelId) і email/username/googleId. Mermaid erDiagram не має unique-нотації - додав ноту на діаграму і уточнив у spec. -> commit `c319a9d`

## 3. Ключове рішення

Mermaid erDiagram замість PlantUML і dbdiagram.io. PlantUML потужніший (unique-нотація, більше деталей) але треба Java, рендер не в GitHub. dbdiagram.io - не текстовий артефакт, не покладеш в репо. Mermaid рендериться прямо в репо - препод відкриває файл і бачить діаграму. Деталі: adr/adr-001-notation-choice.md

## 4. Перевірка узгодженості з попередньою моделлю

Перша лаба - попередніх моделей у ланцюгу немає. Як референс порівняв з Prisma schema реального проєкту VideoHub: 5 моделей = 5 сутностей, всі атрибути, FK і @@unique співпадають один в один. Деталі порівняння в AUDIT.md.
