# Lab 3 - Sequence-діаграма: VideoHub

## Домен

VideoHub - платформа для завантаження та перегляду відео (YouTube-клон).

Реалізація: [github.com/ezpectus/VideoHub](https://github.com/ezpectus/VideoHub)

## Обраний сценарій

**UC3: Upload Video** (з Завдання 2) - ключовий сценарій:
- Користувач завантажує відео з title, description, url
- Система перевіряє автентифікацію (include UC9)
- Валідує ввід, створює запис Video в БД
- Повертає videoId або код помилки

Цей UC найкраще показує взаємодію: User -> Controller -> Service -> Database, з гілками (успіх/помилки).

## Учасники

- **User** (актор) - завантажує відео
- **VideoController** - приймає HTTP-запит, валідує ввід
- **AuthService** - перевіряє токен (реалізує UC9 Authenticate з Lab 2)
- **VideoService** - бізнес-логіка
- **Database** - зберігання (Video entity з ER-моделі Lab 1)

## Гілки сценарію

- `alt` токен невалідний / валідний -> 401 або продовження
- `alt` title порожній -> 400
- `alt` (authorId, url) вже існує -> 409
- успіх -> 201 Created (videoId)

## Зв'язок з попередніми лабами

- **Lab 1 (ER):** Database створює Video entity; authorId = userId з токена
- **Lab 2 (UC):** UC3 Upload Video деталізується; UC9 Authenticate -> validateToken

## Структура

- `task.md` - умова
- `spec.md` - намір, учасники, кроки, критерії
- `model/sequence.mmd` - Mermaid sequenceDiagram (source)
- `model/sequence.drawio` - та сама діаграма для редагування в diagrams.net
- `renders/sequence.png` - рендер
- `AUDIT.md` - розбіжності spec <-> артефакт + коміти-виправлення (4 findings)
- `DEFENSE.md` - точка входу для рев'ю
- `adr/adr-003-upload-dedup-rule.md` - дедуп (authorId, url) як бізнес-правило
- `ai/` - слід AI-ітерації: prompts.md (промпти) + audit.md (знахідки й виправлення)
