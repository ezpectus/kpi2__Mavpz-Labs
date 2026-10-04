# Spec: Lab 3 - Sequence Diagram VideoHub

## Намiр

Описати динаміку сценарію UC3 (Upload Video) з Завдання 2 як sequence-діаграму: актор, компоненти, БД, виклики з напрямком, return-повідомлення, альтернативні гілки помилок (401, 400, 409).

## Обраний UC

UC3: Upload Video (з Lab 2)
- Ініціює: User (залогінений)
- Результат: створений запис Video, повернуто videoId
- Include: UC9 Authenticate -> у цій моделі це AuthService.validateToken

## Учасники

| Учасник | Тип | Відповідає в попередніх моделях |
|---------|-----|----------------------------------|
| User | Actor | User entity (Lab 1), actor User (Lab 2) |
| VideoController | Component | - (API-шар; не сутність) |
| AuthService | Component | UC9 Authenticate (Lab 2); перевіряє User.id |
| VideoService | Component | - (бізнес-логіка UC3) |
| Database | Object | Video entity (Lab 1) |

## Кроки сценарію

1. User надсилає POST /api/videos з title, description, url, auth token
2. VideoController викликає AuthService.validateToken(token) — один раз, на початку
3. alt: токен невалідний -> AuthService повертає null, контролер відповідає 401
4. alt: токен валідний -> повертає userId (дійде до Video.authorId з ER)
5. alt: title порожній -> 400 Bad Request (валідація контролера, до сервісу не доходить)
6. uploadVideo -> createVideo(authorId = userId, title, description, url)
7. alt: (authorId, url) вже існує -> Database повертає conflict, користувачу 409
8. else: Database повертає videoId -> VideoController відповідає 201 Created (videoId)

## Бізнес-правило для 409

В ER-моделі (Lab 1) UNIQUE задано тільки для Like(userId,videoId), Subscription(subscriberId,channelId) та User(email,username,googleId). Для Video.url унікального обмеження немає. Дедуплікація «той самий автор не завантажує один url двічі» — правило рівня застосунку; фіксується цим spec, до ER-моделі не додається.

## Критерії прийняття

- [x] Діаграма деталізує UC3 з Lab 2 (учасники, кроки, include UC9)
- [x] Учасники узгоджені з ER-моделлю (Video entity, authorId = userId)
- [x] Реалістичні назви викликів (validateToken, uploadVideo, createVideo)
- [x] Альтернативні гілки (alt/else); гілки помилок завершують сценарій, а не продовжують його
- [x] Return-повідомлення для викликів
- [x] Гілки помилок: 401, 400, 409 + успіх 201
