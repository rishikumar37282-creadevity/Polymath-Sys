# Project Memory: POLYMATH.SYS (AI Research & Engineering Portal)

## 1. Vision & Core Philosophy
**The Polymath Journey**
This project represents a premium, editorial-style academic web platform designed to map an elite 48-month curriculum across Deep Learning, Mathematics, and Quantum Computing. 

**Core Mission:** To combat "Optimal Strategy Paralysis" by providing a rigorous, self-directed, and meticulously structured ecosystem. It is an intersection of a technical curriculum, an archival vault, and an industry directory.

---

## 2. File Structure & Architecture
The project operates as a highly performant, static frontend system (HTML/CSS/JS) specifically designed to evoke a "System/Terminal" aesthetic.

### Core Files
- `index.html`: The central hub. Contains the core manifesto, curriculum grid, research blog directory, document vault, and ecosystem directory (AI companies, great minds).
- `styles.css`: The monolithic stylesheet. Serves as the global design system containing color variables, layouts, and responsive queries.
- `script.js`: Handles interactivity, such as accordion modules, sequential flow states, and tab-based navigation.
- `memory.md`: The living document for tracking project vision, structure, and ongoing changes.
- `architectures/`: Reference directory containing technical documentation and source markdown for system architectures.

### Curriculum Modules
- `polymath_master_roadmap.html`: Strategy Blueprint (Months 1–48). Structure spanning consistency, systems design, and mathematical linking.
- `phase1_learning_roadmap.html`: Phase I (Months 1–12). Foundations: Core Engineering, Multivariable Calculus, Data Structures.
- `phase2_deep_roadmap.html`: Phase II (Months 13–24). Deep AI: Cloud Infrastructure, PyTorch ecosystems, Sequence Modeling.
- `phase3_frontier_roadmap.html`: Phase III (Months 25–48). The Frontier: Quantum Mechanics, QML, Finance Integration.
- `circular.html`: The Full AI Circular. A dynamic, filterable syllabus providing tabular and chronological breakdowns of topics with interactive discpline filtering.

---

## 3. Design System & Aesthetics

**Style Philosophy:** Dark-mode only, brutalist layout logic but with highly polished micro-interactions.

### Color Palette (Obsidian & High Contrast)
- **Primary Background**: `#0b0b0b`
- **Card/Surface Background**: `#121212`
- **Borders**: `#232323` (Hover: `#4e4e4e`)
- **Primary Text**: `#ededed`
- **Secondary Text (Muted)**: `#888888`
- **Accent/Highlights**: `#ffffff` (Pure white)
- **Functional/Technical Tags**:
  - Math/Finance (Bronze/Orange highlight)
  - Core Engineering (Blue highlight)
  - Machine Learning (Green highlight)
  - Deep AI/Quantum (Purple highlight)
  - Red Flag/Must Know/Primary (Red highlight)

### Typography
- **Primary Font**: `Inter` (Sans-serif) for clean, high-legibility long-form reading.
- **Secondary Font**: Default `monospace` used structurally for metadata, dates, tags, and spine numbering to reinforce the engineering theme.

### UI Components & Layouts
- **Bento Book Grids**: Used on `index.html` to mimic a bookshelf directory (`.book-grid`, `.book-card`).
- **Asymmetrical Blog Grid**: Featured items vs. sidebar items (`.blog-grid`, `.bg-featured`).
- **Data Densities**: Used for Document Vault cards (`.dv-card`) to maximize visible information about downloads/archive objects.
- **Borderless Syllabus Tables**: Used heavily in `circular.html` (`.borderless-table`) with subtle row hover effects (`#151515`).
- **Callout Boxes**: Uses specific left-border highlights (`.cbox`, `.insight`) for rules and milestones.

---

## 4. Workflows & Methodologies
- **Retention Protocol ([M.01])**: Spaced Repetition (surfacing reviews at the edge of the forgetting curve).
- **Synthesis Protocol ([M.02])**: Interleaved Practice (scrambling Math, Physics, and Engineering to build associations).
- **Output Protocol ([M.03])**: Feynman Diagnostics (teaching highly advanced concepts back to AI layers to verify module completion).

---

## 5. Changelog & Project Evolution

*(Use this section to log major implementations, aesthetic overhauls, and significant structural changes going forward.)*

- **[2026-03]**: Initial platform analysis and creation of `memory.md`.
- **[2026-03-28] — Technical Architecture Integration**:
  - **Mermaid.js System**: Embedded Mermaid.js natively across all phase roadmaps. Replaced external link buttons with interactive SVG diagrams (RAG Pipeline, Transformer, QML circuits).
  - **Design Extension**: Appended `.arch-container` and `.mermaid` tokens to the global design system.
- **[2026-03-28] — Hero Showcase & 3D Immersion**:
  - **The Hero Stage**: Implemented a "Metallic Black" textured top section (`hero-stage`) with brushed-metal gradients and a minimal dot-grid pattern spanning the full viewport width.
  - **3D Isometric Stack**: Engineered a floating architectural file stack using pure CSS 3D transforms (`rotateX(60deg)`).
  - **Typewriter Engine**: Built a pure CSS mechanical typewriting/backspacing loop for brand-identity strings in an elegant `Playfair Display` serif.
  - **Rotating Signal Strip**: Integrated a JavaScript-driven rotating quote carousel featuring signals from Feynman, Einstein, Turing, and von Neumann with an editorial layout.
- **[2026-03-28] — Syllabus Intelligence**:
  - **Dynamic Filtering**: Converted the static syllabus (circular.html) into "The Full AI Circular" with an interactive pill-based filter system for cross-domain exploration (AI, ML, Quantum, etc.).
  - **Aesthetic Polish**: Added 3D depth physics to book cards and shimmering reveals to hero typography. Fixed structural regressions in roadmap panels.
