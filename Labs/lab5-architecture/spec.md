# Spec: Lab 5 - Component Diagram VideoHub

## Намiр

Описати архітектуру VideoHub як компонентну діаграму. Компоненти, provided/required-інтерфейси, залежності, межа системи, зовнішні інтеграції. Повна узгодженість з Lab 1-4.

## Компоненти системи

| Компонент | Відповідає (Lab 1-4) |
|-----------|---------------------|
| Frontend (Next.js) | UI для всіх UC (Lab 2) |
| API Gateway (Express) | VideoController (Lab 3) |
| Auth Service | AuthService (Lab 3), UC2/UC9 (Lab 2) |
| Video Service | VideoService (Lab 3), UC3 (Lab 2) |
| Comment Service | UC5 (Lab 2) |
| Notification Service | fork: notify subscribers (Lab 4) |
| Search Service | fork: index video (Lab 4), UC8 (Lab 2) |
| Data Access Layer | Database (Lab 3) |
| PostgreSQL | Video, User, Comment, Like, Subscription (Lab 1) |

## Зовнішні інтеграції

| Зовнішня система | Інтерфейс |
|------------------|-----------|
| Google OAuth | Auth (required by Auth Service) |
| Email/SMS Gateway | Notify (required by Notification Service) |

## Інтерфейси

### Provided (система надає)
- `IREST API` - REST endpoints (provided by API Gateway)
- `IAuth` - автентифікація (provided by Auth Service)
- `IVideoOps` - операції з відео (provided by Video Service)
- `ICommentOps` - операції з коментарями (provided by Comment Service)
- `ISearch` - пошук (provided by Search Service)

### Required (система потребує)
- `IGoogleOAuth` - Google OAuth (required by Auth Service)
- `IEmailGateway` - email/SMS (required by Notification Service)
- `IDataAccess` - доступ до БД (required by services, provided by Data Access Layer)

## Межа системи

Всередині: Frontend, API Gateway, Auth/Video/Comment/Notification/Search Services, Data Access, PostgreSQL
Зовні: Google OAuth, Email/SMS Gateway

## Критерії прийняття

- [x] Компоненти та інтерфейси коректні
- [x] Provided/required-інтерфейси визначені
- [x] Межа системи чітка
- [x] Зовнішні інтеграції показані
- [x] Узгодженість з ER (Lab 1)
- [x] Узгодженість з UC (Lab 2)
- [x] Узгодженість з Sequence (Lab 3)
- [x] Узгодженість з Activity (Lab 4)
