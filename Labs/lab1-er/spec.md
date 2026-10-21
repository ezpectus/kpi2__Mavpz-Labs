# Spec: Lab 1 - ER-модель VideoHub

## Намір

Змоделювати дані платформи для завантаження та перегляду відео як ER-модель: сутності, атрибути, зв'язки, кардинальності, первинні та зовнішні ключі. Домен обрано на основі реального проєкту VideoHub (YouTube-клон).

## Сутності та атрибути

### User
- id (PK, UUID)
- email (unique)
- username (unique)
- password (nullable, бо може бути Google OAuth)
- googleId (nullable, unique)
- avatar (nullable)
- banner (nullable)
- description (nullable)
- createdAt

### Video
- id (PK, UUID)
- title
- description (nullable)
- url
- thumbnail (nullable)
- views (int, default 0)
- createdAt
- authorId (FK -> User.id)

### Comment
- id (PK, UUID)
- text
- createdAt
- userId (FK -> User.id)
- videoId (FK -> Video.id)

### Like
- id (PK, UUID)
- userId (FK -> User.id)
- videoId (FK -> Video.id)
- createdAt (коли лайкнуто - власний атрибут, тому асоціативна сутність а не чистий зв'язок M:N)
- Unique: (userId, videoId) - один лайк на відео від користувача

### Subscription
- id (PK, UUID)
- subscriberId (FK -> User.id)
- channelId (FK -> User.id)
- createdAt
- Unique: (subscriberId, channelId) - одна підписка

## Зв'язки

1. User - Video: one-to-many (автор має багато відео, відео має одного автора)
2. User - Comment: one-to-many (користувач пише багато коментарів)
3. Video - Comment: one-to-many (відео має багато коментарів)
4. User - Video: many-to-many через Like (асоціативна сутність)
5. User - User: many-to-many через Subscription (self-referencing, асоціативна сутність)

## Критерії прийняття

- [x] Кардинальності коректні (1:N, M:N)
- [x] Правило асоціативної сутності: зв'язок стає сутністю ЛИШЕ якщо має власні атрибути. Чистий M:N без атрибутів - це нормальний зв'язок, а не помилка. Like і Subscription - сутності, бо мають createdAt (час дії - дані домену)
- [x] Первинні ключі визначені для всіх сутностей
- [x] Зовнішні ключі визначені
- [x] Модель нормалізована (3NF - немає транзитивних залежностей)
- [x] Унікальність ВИДНО в моделі: окремі атрибути позначені маркером `UK` (видно в рендері); складені пари Like (userId, videoId) і Subscription (subscriberId, channelId) задокументовані текстом у spec, бо Mermaid erDiagram не має composite-UK - це реальне обмеження нотації
- [x] Рендер PNG і drawio синхронні з source er.mmd
- [x] Відмінності від джерельної схеми зафіксовані нижче

## Відмінності від джерельної схеми (VideoHub, schema.prisma)

Звірено построково з Prisma-моделлю реального проєкту:

- `Like.createdAt` - у джерелі ВІДСУТНІЙ; додано свідомо: час лайку є даними домену (і обґрунтовує Like як сутність - див. adr-002).
- Решта атрибутів, PK, FK та @@unique збігаються.
