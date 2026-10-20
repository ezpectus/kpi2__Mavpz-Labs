# Lab 5 - Architecture: VideoHub

## Домен

VideoHub - платформа для завантаження та перегляду відео (YouTube-клон).

Реалізація: [github.com/ezpectus/VideoHub](https://github.com/ezpectus/VideoHub)

## Архітектура

Система складається з:
- **Frontend** (Next.js) - UI, рендеринг сторінок
- **Backend API** (Express) - REST API, контролери
- **Auth Service** - JWT + Google OAuth
- **Video Service** - бізнес-логіка відео
- **Comment Service** - бізнес-логіка коментарів
- **Notification Service** - сповіщення підписникам
- **Search Service** - індексування і пошук
- **Database** (PostgreSQL) - зберігання даних
- **Google OAuth** (зовнішня інтеграція) - автентифікація
- **Email/SMS Gateway** (зовнішня інтеграція) - канал сповіщень (ADR-005)

## Зв'язок з попередніми лабами

- **Lab 1 (ER):** Database зберігає сутності User, Video, Comment, Like, Subscription
- **Lab 2 (UC):** Компоненти реалізують use cases (VideoService = UC3, AuthService = UC2/UC9)
- **Lab 3 (Sequence):** VideoController -> AuthService -> VideoService -> Database = компоненти на діаграмі
- **Lab 4 (Process):** fork (notify + index) = Notification Service + Search Service

## Структура

- `task.md` - умова
- `spec.md` - компоненти, інтерфейси, межа, критерії
- `model/` - source діаграми
- `renders/component.png` - рендер
- `AUDIT.md` - розбіжності spec <-> артефакт + коміти-виправлення
- `DEFENSE.md` - точка входу для рев'ю
- `adr/` - ADR-005 і далі
- `ai/` - слід AI-ітерації (промпти, аудит, workflow)
