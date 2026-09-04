# Spec: Lab 1 - ER-модель VideoHub (draft)

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

TODO: дописати критерії прийняття
