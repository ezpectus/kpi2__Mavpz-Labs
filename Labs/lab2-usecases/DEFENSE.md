# DEFENSE: Lab 2 - Use Cases

Описав вимоги до VideoHub через EARS, user stories, Gherkin та use-case-діаграму. Два типи акторів (Guest/User + Google OAuth), include/extend, трасування M:N.

## Узгодженість з ER-моделлю (Lab 1)

Порівняв кожну сутність з ER-моделі з use cases:
- User -> User actor, UC1 Register, UC2 Login
- Video -> UC3 Upload, UC4 Watch
- Comment -> UC5 Comment
- Like -> UC6 Like
- Subscription -> UC7 Subscribe
- googleId в User -> Google OAuth actor

Все співпадає. Немає use case без сутності і навпаки.

## Аудит і виправлення

В першій версії діаграми не було зовнішнього актора. Додав Google OAuth (commit: `fix - add google oauth actor`). Потім помітив що нема include/extend - додав UC9 Authenticate з include для UC2/3/5/6/7 і extend UC8 -> UC4 (commit: `fix - add include extend`). Матриця трасування була 1:1 - переписав на M:N, додав непокриту REQ11 (commit: `add ears, user stories, gherkin`).

## Рішення по нотації

Mermaid graph замість PlantUML. PlantUML мав би стандартну нотацію але не рендериться в GitHub. Mermaid рендериться, хоча нотація не стандартна - компенсую текстом в spec. Деталі: adr/adr-002-usecase-notation.md
