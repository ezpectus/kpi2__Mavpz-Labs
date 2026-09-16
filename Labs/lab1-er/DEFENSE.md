# DEFENSE - Lab 1: ER-модель VideoHub

## Чому Mermaid а не PlantUML

Вибрав Mermaid erDiagram бо рендериться в GitHub нативно. Препод відкриває репо і бачить діаграму без інструментів. PlantUML потужніший (підтримка inheritance, notations) але треба Java або плагін. Для лаби достатньо. Деталі: adr/adr-001-notation-choice.md

## Узгодженість з проєктом

Це перша лаба - попередніх моделей немає. Порівняв з реальним проєктом VideoHub (Prisma schema): 5 сутностей (User, Video, Comment, Like, Subscription), 5 зв'язків, FK і unique-обмеження співпадають з schema.prisma один в один.

## Що знайшов в аудиті і виправив

1. Like був прямим M:N (`User }|--|{ Video`) замість асоціативної сутності. Розгорнув через Like (User ||--o{ Like, Video ||--o{ Like). Commit: `fix - like as associative entity`

2. Subscription так само - прямий M:N self-ref. Розгорнув через Subscription з двома FK на User. Commit: `fix - subscription as associative entity`

3. Unique-обмеження не були показані. Mermaid erDiagram не підтримує unique нотацію, додав коментар на діаграму. Commit: `fix - add unique constraints note`
