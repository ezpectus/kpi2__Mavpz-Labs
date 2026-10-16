# AI prompts: Lab 4 — процес (Activity), AI-шлях

## Контекст на вході

Ця лаба робилась з AI за рішенням після Lab 1–3: складніші завдання (процеси, архітектура) — через явний AI-цикл «драфт -> AI-аудит -> фікс-коміти». На вхід скинуто: `task.md` (activity АБО state machine; >=1 розгалуження; >=1 паралельна гілка; аудит повноти переходів/досяжності/умов; звірка з UC Lab 2 і Sequence Lab 3; топ-3 розбіжності; DEFENSE), `spec.md`, драфт `model/activity.mmd` (Mermaid flowchart v3), файли Lab 2 (`usecases.md` — main/alt flows UC3) і Lab 3 (`model/sequence.mmd` — гілки 401/400/409 з `findByAuthorAndUrl`), git-лог попередніх лаб і урок з рев'ю Lab 2 («діаграма не в UML-нотації»).

## P1 — чек-лист з умови

> Прочитай `task.md` Lab 4 і витягни кожну вимогу окремим пунктом чек-листа з місцем перевірки (spec / діаграма / аудит / defense). Не додавай вимог, яких немає в тексті умови. Окремо познач вимоги, що задають кількісний мінімум (>=1 розгалуження, >=1 паралельна гілка) і вимоги-звірки (UC, Sequence).

Відповідь AI: 9 пунктів — одна декларативна форма; start/end; дії+потоки; >=1 if/else; >=1 fork/join; swimlanes «за потреби»; повнота переходів+досяжність+коректність умов; звірка з UC і Sequence; топ-3 розбіжності + DEFENSE.

## P2 — прогнати чек по драфту

> Прогони чек-лист по `model/activity.mmd` v3 і `spec.md` як є. По кожному пункту — PASS/FAIL/РИЗИК з номером рядка. Окремим проходом звір гілки помилок з `Labs/lab3-sequence/model/sequence.mmd`: у sequence є 401/400/409 і явний крок `findByAuthorAndUrl`. Випиши кожну розбіжність з процитованим рядком.

Відповідь AI: FAIL — (а) у драфті тільки 401 і 400, гілки 409 з dedup-перевіркою немає взагалі — пряма розбіжність з Sequence (критерій «узгодженість з Lab 3»); (б) `{{fork}}`/`{{join}}` — шестикутники flowchart-синтаксису, не UML fork/join-бари; (в) swimlanes відсутні — ролі є в spec, але на діаграмі їх не видно; (г) Notify/Index не зустрічаються ні в UC3 flows, ні в sequence — незадокументоване розширення; (д) `title: ... v3` — версія в заголовку.

## P3 — критична оцінка нотації

> Lab 2 була відхилена за «діаграма говно кругле» — Mermaid graph замість UML use-case, виправлено переходом на PlantUML. Критично оціни: для Lab 4 умова дозволяє «Mermaid flowchart АБО PlantUML activity». Чи повторює flowchart ту саму помилку (наближення нотації замість нотації)? Порівняй по пунктах: swimlanes/partitions, fork/join як бари, decision-ромби, start/end, стрілки потоків. Висновок аргументуй нотацією, не зручністю GitHub-рендеру.

Відповідь AI: повторює. Flowchart не має partitions (ролі не намалювати), fork/join — звичайні вузли-шестикутники, не synchronization-бари; у PlantUML activity є `partition`, справжні `fork/fork again/end fork`, ромби `if/then/else`, `start/stop`. Рішення: канонічний source — PlantUML `activity.puml`; ADR-004 переглянуто (superseded для Mermaid — той самий сценарій що в Lab 2 з ADR-002).

## P4 — реалізація spec+model одним комітом

> Виправи ОДНИМ комітом spec.md і модель: (а) у spec додай критерії «діаграма в UML activity-нотації (канонічний source PlantUML): start/end, ромби-рішення, fork/join-бари, swimlanes» і «гілки помилок ідентичні Sequence Lab 3 (401/400/409, dedup-крок явний)»; кроки — додай dedup-перевірку між валідацією і створенням; ролі — зафіксуй дві lanes User/System. (б) Модель перепиши на `activity.puml`: partition User (open form, fill, submit) і partition VideoHub System (validateToken -> 401 end; validateInput -> 400 end; findByAuthorAndUrl -> 409 end; createVideo -> fork [Notify | Index] -> join -> 201 -> end). (в) `activity.mmd` видалити — один канонічний source. Коміт «spec+model ...» як у Lab 3.

Результат: коміт spec+model — PlantUML activity + гілка 409 + swimlanes + ADR-004 оновлено.

## P5 — рендери і синхронізація

> Перерендери `renders/activity.png` з `activity.puml` (через PlantUML server з User-Agent, як у Lab 2). Перепиши `activity.drawio` семантично синхронним: ті самі дії у тих самих lanes, ромби, fork/join-бари. Самоперевірка: жоден потік не йде в End поверх join; кожен decision має рівно два підписані виходи; 401/400/409 текстом збігаються з sequence.mmd.

Результат: PNG перегенеровано (видно lanes, три ромби, fork/join-бари), drawio синхронний.

## P6 — AUDIT у форматі рев'ю

> Напиши `AUDIT.md` за форматом Lab 3: кожна розбіжність = який критерій spec був відсутнім/неточним -> знайдено (з цитатою драфту) -> виправив -> коміт. Очікувані файндінги: немає 409/dedup (розбіжність з Lab 3), flowchart замість activity-нотації, swimlanes відсутні, Notify/Index незадокументовані -> ADR-004. «Цей коміт» там, де коміту ще немає — не вигадуй хеші.

## P7 — DEFENSE і звірка з попередніми моделями

> Напиши `DEFENSE.md` за шаблоном викладача: намір/критерії, топ-3 розбіжності + коміти, ключове рішення (ADR), перевірка узгодженості з UC і Sequence. У звірці: (а) гілки 401/400/409 і дедуп-крок ідентичні Lab 3 — sequence показує ХТО викликає, activity показує ПОТІК тієї ж логіки; (б) fork/join — асинхронні кроки, яких sequence не моделює (синхронний ракурс) — доменне розширення, ADR-004; (в) lane User відповідає актору UC3.

## P8 — фінальний прогон

> Прогони чек-лист P1 по фінальним файлам. По кожному пункту PASS/FAIL з доказом (файл:рядок). Якщо хоч один FAIL — виведи тільки його і стоп.

## P9 — workflow doc

> Опиши реальний процес у `ai/lab4_workflow.md` за шаблоном `lab3_workflow.md`: spec -> драфт (AI) -> AI-аудит -> фікс-коміти -> рендер -> AUDIT/DEFENSE -> пост-рев'ю готовність. Чесно вкажи, які файндінги знайшов AI-чек, а які б вручну не помітив.
