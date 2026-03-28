# AGENT RECONSTRUCTION: PROMPT SEQUENCE

Use the following prompts in order to migrate and scale **Polymath.Sys** from a fresh conversation. **Do not skip steps.**

---

### Prompt 1: Initial Context & DNA Loading
> "I am working on the **Polymath.Sys** AI Research portal. Before taking any action, please read the following files to understand the project architecture, design DNA, and scalability roadmap:
> 1. Read `AI Research Eng/memory.md` for project history.
> 2. Read `docs/architecture/MASTER_SYSTEM_BLUEPRINT.md` for the technical foundation.
> 3. Read `docs/architecture/instruction.md` for the migration manual.
> Your goal is to migrate the project to **Astro** while maintaining 100% visual and functional parity with the current Brutalist-Premium design."

---

### Prompt 2: Design Token & Layout Analysis
> "Analyze `styles.css` and `index.html`. Identify the core design tokens (CSS variables) and the structure of the shared elements (Header, Cross-Page Nav, Footer). 
> Then, create a `src/layouts/MainLayout.astro` file that incorporates these elements, ensuring that the `styles.css` is imported as a global style."

---

### Prompt 3: Phase 1 & 2 Roadmap Migration
> "Migrate the roadmaps from `AI Research Eng/phase1_learning_roadmap.html` (and Phase 2/3) into **Astro Content Collections**. 
> - Create a schema in `src/content/config.ts`.
> - Move the content into `src/content/roadmap/phase1.md`.
> - Ensure the `[RoadmapTemplate].astro` renders the Markdown into the exact same high-contrast tables and panels as the original HTML."

---

### Prompt 4: The Intelligence Layer (Automation)
> "Implement the **Automated News & Research Pipeline**.
> 1. Create a Python script in `scripts/research_scraper.py` that fetches papers from ArXiv API and formats them into `.md` files.
> 2. Create the GitHub Action in `.github/workflows/daily-sync.yml` to trigger this script and auto-commit the updates to the `src/content/news/` collection.
> 3. Ensure this logic is 'Agent-Safe' and won't overwrite existing manual blog posts."

---

### Prompt 5: Feature Expansion (Jobs & Repos)
> "Implement the **Repository Ranking** and **Industry Career Board**.
> - Integrate a build-time script that fetches GitHub star data for the repos in the 'Ecosystem' section.
> - Create a YAML data file for job roles at top AI companies.
> - Ensure these sections use the same 'Bento' grid cards defined in the original `styles.css`."

---

### Prompt 6: Final Verification & QA
> "Verify the entire deployment:
> 1. Check that all cross-navigation links in the `.phase-header-nav` are functional.
> 2. Test the Mermaid.js diagrams across all roadmap phases.
> 3. Run the `generator.py` script to ensure the local PDF generation still works for the new Astro-based structure.
> 4. Ensure no regression in the 3D CSS transforms and dot-grid backgrounds."
