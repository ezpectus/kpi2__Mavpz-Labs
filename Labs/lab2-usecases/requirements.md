# EARS-вимоги (Lab 2)

| ID | EARS | Тестованість |
|----|------|-------------|
| REQ1 | WHEN user submits registration form with email and password, system SHALL create account and return auth token | Так: є форма, є відповідь |
| REQ2 | WHEN user selects Google login, system SHALL redirect to Google OAuth and create account on callback success | Так: редірект, callback |
| REQ3 | WHILE user is authenticated, system SHALL allow video upload with title, description and URL | Так: перевірка auth |
| REQ4 | WHEN guest opens video page, system SHALL display video player, views count and comments list | Так: сторінка відео |
| REQ5 | WHEN user clicks like button, system SHALL record like and prevent duplicate likes from same user | Так: один лайк |
| REQ6 | WHEN user subscribes to channel, system SHALL create subscription record and notify channel owner | Так: запис, нотифікація |
| REQ7 | WHILE guest enters search query, system SHALL return matching videos by title sorted by relevance | Так: пошуковий запит |
| REQ8 | WHEN user posts comment on video, system SHALL store comment with userId, videoId and timestamp | Так: коментар збережено |
| REQ9 | WHEN user deletes own comment, system SHALL mark comment as deleted (soft delete) | Так: soft delete |
| REQ10 | WHILE channel owner views subscriber list, system SHALL display list of users subscribed to their channel | Так: список |

## Непокрита вимога

- REQ11: WHEN video upload fails due to invalid format, system SHALL return error with supported formats list
  - Не покрито use case - це винятковий сценарій UC3 (Upload Video), не окремий UC. Пояснення: обробка помилок всередині UC3, не потребує окремого сценарію на діаграмі.

---

# User Stories

| ID | Story |
|----|-------|
| US1 | As a Guest, I want to search videos by title so that I can find content without registering |
| US2 | As a Guest, I want to watch videos so that I can view content |
| US3 | As a User, I want to register with email so that I can have an account |
| US4 | As a User, I want to login with Google so that I don't need to remember another password |
| US5 | As a User, I want to upload videos so that I can share my content |
| US6 | As a User, I want to comment on videos so that I can discuss content |
| US7 | As a User, I want to like videos so that I can show appreciation |
| US8 | As a User, I want to subscribe to channels so that I can follow creators |
| US9 | As a User, I want to delete my comments so that I can remove outdated content |

---

# Gherkin-сценарії

## Feature: Registration

```gherkin
Scenario: Register with email and password
  Given no user exists with email "test@example.com"
  When user submits registration form with email "test@example.com" and password "Pass123"
  Then system creates account
  And returns auth token
```

## Feature: Google Login

```gherkin
Scenario: Login via Google OAuth
  Given user is not authenticated
  When user clicks "Login with Google"
  Then system redirects to Google OAuth
  When Google returns valid callback with email "user@gmail.com"
  Then system creates or finds account
  And returns auth token
```

## Feature: Upload Video

```gherkin
Scenario: Authenticated user uploads video
  Given user is authenticated with id "uuid-123"
  When user uploads video with title "My Video" and url "https://cdn.videohub.com/v/123.mp4"
  Then system creates video record with authorId "uuid-123"
  And returns video id
```

## Feature: Like Video

```gherkin
Scenario: User likes a video
  Given user "uuid-123" is authenticated
  And video "uuid-456" exists
  When user clicks like on video "uuid-456"
  Then system creates like record with userId "uuid-123" and videoId "uuid-456"
  And prevents duplicate likes from same user

Scenario: User cannot like same video twice
  Given user "uuid-123" already liked video "uuid-456"
  When user clicks like on video "uuid-456"
  Then system does not create duplicate like
  And returns existing like status
```

## Feature: Subscribe

```gherkin
Scenario: User subscribes to channel
  Given user "uuid-123" is authenticated
  And user "uuid-789" has a channel
  When user "uuid-123" subscribes to channel "uuid-789"
  Then system creates subscription record
  With subscriberId "uuid-123" and channelId "uuid-789"
```

## Feature: Search

```gherkin
Scenario: Guest searches for videos
  Given no authentication required
  When guest enters search query "cats"
  Then system returns videos where title contains "cats"
  And results are sorted by relevance
```

---

# Матриця трасування

| Вимога | User Story | Use Case | Gherkin |
|--------|-----------|----------|---------|
| REQ1 | US3 | UC1 | Registration |
| REQ2 | US4 | UC2 | Google Login |
| REQ3 | US5 | UC3 | Upload Video |
| REQ4 | US2 | UC4 | - |
| REQ5 | US7 | UC6 | Like Video (2 scenarios) |
| REQ6 | US8 | UC7 | Subscribe |
| REQ7 | US1 | UC8 | Search |
| REQ8 | US6 | UC5 | - |
| REQ9 | US9 | UC5 | - |
| REQ10 | - | - | - |
| REQ11 | - | - | - (непокрита, див. пояснення вище) |

Покриття: REQ10 (subscriber list) - не має окремого UC, це частина UC7 (Subscribe) з точки зору channel owner. Можна додати UC9 якщо треба.
