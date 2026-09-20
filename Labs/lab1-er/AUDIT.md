# Audit: Lab 1 - ER-модель VideoHub

## Метод

Порівняв модель (er.mmd) з spec.md і з реальним проєктом VideoHub (Prisma schema).

## Знайдені проблеми

### 1. Like - прямий M:N замість асоціативної сутності

В v1 було: `User }|--|{ Video : "likes"` - пряме M:N без асоціативної сутності.
В spec пункт 4: "User - Video: many-to-many через Like (асоціативна сутність)".
В Prisma: Like - окрема модель з FK на User і Video + @@unique([userId, videoId]).

Виправив: розгорнув M:N через Like як асоціативну сутність (User ||--o{ Like, Video ||--o{ Like).
Commit: `lab1: fix - like as associative entity not direct M:N`

### 2. Subscription - прямий M:N замість асоціативної сутності

В v1 було: `User }|--|{ User : "subscribes to"` - пряме M:N self-referencing.
В spec пункт 5: "User - User: many-to-many через Subscription (self-referencing, асоціативна сутність)".
В Prisma: Subscription - окрема модель з двома FK на User + @@unique([subscriberId, channelId]).

Виправив: розгорнув M:N через Subscription (User ||--o{ Subscription "subscriber", User ||--o{ Subscription "channel").
Commit: `lab1: fix - subscription as associative entity + unique note`

### 3. Unique-обмеження не показані на діаграмі

В v1 не було позначено unique-обмеження. В spec: email unique, username unique, googleId unique, (userId, videoId) unique, (subscriberId, channelId) unique.
Mermaid erDiagram не підтримує unique-нотацію на діаграмі.

Виправив: додав comment-блок з unique-обмеженнями на діаграму.
Commit: `lab1: fix - subscription as associative entity + unique note` (той самий - unique туди ж)
