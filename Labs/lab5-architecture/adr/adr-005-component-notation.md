# ADR-005: Mermaid graph для component diagram

## Статус

Accepted

## Контекст

Для Lab 5 треба component diagram з інтерфейсами, залежностями, межею системи. Варіанти:

1. **Mermaid graph** - GitHub рендерить, subgraph для межі системи, мітки на ребрах для інтерфейсів
2. **PlantUML component** - стандартна UML component нотація (lollipop interfaces), але не рендериться в GitHub
3. **draw.io** - візуальний редактор, не текстовий артефакт

## Рішення

Обрав Mermaid graph. Причини:
- subgraph створює чітку межу системи
- Мітки на ребрах (`-->|IAuth|`) показують інтерфейси
- Пунктирні ребра (`-.->`) відрізняють зовнішні залежності
- Рендериться в GitHub нативно

## Наслідки

- Плюс: рендериться в GitHub, subgraph для межі, мітки для інтерфейсів
- Мінус: не стандартна UML component нотація (нема lollipop interfaces, assembly connectors)
- Компенсую: текстовий опис інтерфейсів в spec.md (provided/required списки)
- Як і в Lab 2 (use case), Mermaid - компроміс між стандартом і доступністю
