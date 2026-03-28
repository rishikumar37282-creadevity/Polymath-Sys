# IMPLEMENTATION GUIDE: Astro Migration & Intelligence Layer

This document provides a step-by-step manual for migrating **Polymath.Sys** from its current static HTML structure to a scalable, automated **Astro** framework.

---

## Phase 1: The Astro Infrastructure
*Goal: Move from monolithic HTML to a component-driven architecture.*

### 1. Project Initialization
```bash
npx create-astro@latest ./ --template minimal --no-install
```
- **Directory Structure**:
  - `/src/layouts/`: Base layout with your current `<head>` and `styles.css`.
  - `/src/components/`: Navigation bar, Footer, and individual Cards.
  - `/src/pages/`: Main entry points.
  - `/src/content/`: Markdown-driven data (Roadmaps, Blogs).

### 2. Design System Migration
1. Copy the current `styles.css` to `src/styles/global.css`.
2. Import it in your `MainLayout.astro` to ensure 100% visual parity.
3. **Important**: Preserve the CSS variables for the color palette (`--bg`, `--card-bg`, etc.).

---

## Phase 2: Markdown & Content Collections
*Goal: Separate content from code to enable easy expansion.*

### 1. Schema Definition
Define your collections in `src/content/config.ts`:
```typescript
import { defineCollection, z } from 'astro:content';

const roadmap = defineCollection({
  schema: z.object({
    title: z.string(),
    phase: z.number(),
    lastUpdated: z.date(),
  })
});

export const collections = { 'roadmap': roadmap };
```

### 2. Roadmap Migration
Move all content from `phase1_learning_roadmap.html` into `src/content/roadmap/phase1.md`. Use Markdown for the syllabus tables and mermaid blocks for diagrams.

---

## Phase 3: The Automation & Intelligence Layer
*Goal: Implement zero-touch research and news extraction.*

### 1. The GitHub Action Scraper
1. Create `.github/workflows/daily-sync.yml`.
2. Set it to run on a `schedule` (cron) daily.
3. The workflow should:
   - Run a Python script (`scripts/research_scraper.py`).
   - Use the `arxiv` and `feedparser` libraries.
   - Generate a new `.md` file in `src/content/news/`.
   - `git commit` and `push` back to the repo.

### 2. Intelligence Module (Scraper Strategy)
- **Source ArXiv**: Filter by category `cs.LG`, `cs.AI`, `quant-ph`.
- **Source Industry**: Scrape OpenAI, DeepMind, and Anthropic blogs.
- **Source Jobs**: Scrape Greenhouse/Lever APIs for specific companies.

---

## Phase 4: Feature Extensions
*Goal: Advanced functional integrations.*

### 1. Repository Ranking System
- Create a script that uses the GitHub REST API to fetch stats for the repos listed in your current "Ecosystem" section.
- Calculate a "Momentum Score" based on star growth and recent commits.
- Display this as a "Hot/Trending" tag on the dashboard.

### 2. Career & Industry Board
- Use a `jobs.yaml` data file.
- Implement a simple filter in Astro to display roles based on "Research" vs "Engineering" vs "Alignment".

---

## Agent Skills & Rules
*Required mental models for implementation:*

1. **The Brutalist Skill**: When adding new elements, use only hard borders (`1px solid #232323`), mono-spaced fonts for metadata, and extreme padding (`4rem+`). Never use rounded corners greater than `4px`.
2. **The Performance Skill**: Always check the "Network" tab. A single page load should never exceed **200kb** (excluding images). Use Astro's `client:load` sparingly.
3. **The Accuracy Skill**: Technical content must be verified. Roadmaps should correctly link to the cited papers on ArXiv.

---

## Implementation Checklist
- [ ] Initialize Astro environment.
- [ ] Extract `Layout.astro` and `Navigation.astro`.
- [ ] Convert `phase1-3` HTML to Markdown.
- [ ] Set up `GitHub Actions` for automated scraping.
- [ ] Connect `generator.py` to the new Astro build process.
