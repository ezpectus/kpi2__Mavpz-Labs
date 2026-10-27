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
- `IRestApi` - REST endpoints (provided by API Gateway)
- `IAuth` - автентифікація (provided by Auth Service)
- `IVideoOps` - операції з відео (provided by Video Service)
- `ICommentOps` - операції з коментарями (provided by Comment Service)
- `ISearch` - пошук (provided by Search Service)
- `ISearchIndex` - індексування відео (provided by Search Service)
- `INotify` - сповіщення (provided by Notification Service)
- `IDataAccess` - доступ до БД (provided by Data Access Layer)

### Required (система потребує)
- `IRestApi` - required by Frontend
- `IAuth`, `IVideoOps`, `ICommentOps`, `ISearch` - required by API Gateway
- `INotify`, `ISearchIndex`, `IDataAccess` - required by Video Service
- `IDataAccess` - required by Auth/Comment/Search Services
- `IGoogleOAuth` - Google OAuth (required by Auth Service, зовнішній)
- `IEmailGateway` - email/SMS (required by Notification Service, зовнішній — ADR-005)

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
- [x] Діаграма в UML component-нотації — канонічний source PlantUML `model/component.puml` («component»-стереотипи, provided lollipop / required socket, межа як first-class елемент `rectangle`); Mermaid `graph TD` не має component-нотації — лише мітки ребер (прецедент Lab 2 і Lab 4)
- [x] Матриця трасування: кожен компонент і кожна залежність має слід у Lab 1–4 (UC/REQ/lifeline/activity-крок) — доведено таблицею в AUDIT.md; жоден UC1–UC9 без компонента
- [x] Email/SMS Gateway — задокументоване доменне розширення (ADR-005): канал сповіщень для REQ6 і кроку Notify (Lab 4), поза REQ явно позначено
