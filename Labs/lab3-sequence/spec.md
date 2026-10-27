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
2. VideoController викликає AuthService.validateToken(token) — один раз, на початку; AuthService повертає userId or null
3. break: токен невалідний -> контролер відповідає 401, сценарій переривається
4. validate input (title, format) — самоперевірка контролера; break: title empty or invalid format -> 400, кінець (REQ11: invalid format — той же 400-шлях)
5. uploadVideo -> findByAuthorAndUrl(authorId = userId, url) — явний крок перевірки бізнес-правила дедупу (ADR-003: правило рівня застосунку — перевіряє сервіс, а не UNIQUE-обмеження БД); Database повертає video or not found
6. break: duplicate found -> conflict, користувачу 409, кінець
7. createVideo(authorId = userId, ...) -> Database повертає videoId -> VideoController відповідає 201 Created (videoId)

Гілки помилок змодельовані break-фрагментами (термінальний вихід зі сценарію), не вкладеною пірамідою alt — потік лишається лінійним і читабельним; семантика та сама: помилка перериває решту сценарію.

## Бізнес-правило для 409

В ER-моделі (Lab 1) UNIQUE задано тільки для Like(userId,videoId), Subscription(subscriberId,channelId) та User(email,username,googleId). Для Video.url унікального обмеження немає. Дедуплікація «той самий автор не завантажує один url двічі» — правило рівня застосунку; фіксується цим spec, до ER-моделі не додається.

## Критерії прийняття

- [x] Діаграма деталізує UC3 з Lab 2 (учасники, кроки, include UC9)
- [x] Учасники узгоджені з ER-моделлю (Video entity, authorId = userId)
- [x] Реалістичні назви викликів (validateToken, uploadVideo, createVideo)
- [x] Альтернативні гілки; гілки помилок ТЕРМІНАЛЬНІ — break-фрагменти (break = вихід зі сценарію; opt не обриває — не використовується)
- [x] Кроки бізнес-правил — явні повідомлення: дедуп-перевірка findByAuthorAndUrl перед createVideo, а не неявний конфлікт БД
- [x] Return-повідомлення для викликів
- [x] Гілки помилок: 401, 400, 409 + успіх 201
- [x] Компоненти — окремі lifelines (не один "Server"); validateToken один виклик перед розгалуженням
