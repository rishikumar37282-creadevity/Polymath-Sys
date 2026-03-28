<div align="center">

# ◼ POLYMATH.SYS

### *The 48-Month AI Research & Engineering Curriculum*

[![Built With](https://img.shields.io/badge/Built%20With-HTML%20%7C%20CSS%20%7C%20JS-0b0b0b?style=for-the-badge&labelColor=1e1e1e)](.)
[![Design](https://img.shields.io/badge/Design-Editorial%20Dark-0b0b0b?style=for-the-badge&labelColor=1e1e1e)](.)
[![Status](https://img.shields.io/badge/Status-Active%20Development-4ade80?style=for-the-badge&labelColor=1e1e1e)](.)
[![License](https://img.shields.io/badge/License-Academic%20%26%20Research-60a5fa?style=for-the-badge&labelColor=1e1e1e)](.)

<br>

*A premium, minimalist web platform that structures an elite curriculum spanning*  
*Classical Deep Learning · Mathematics · Quantum Computing · Quantitative Finance*

<br>

---

</div>

<br>

## 🧠 The Problem This Solves

> **Optimal Strategy Paralysis** — the specific trap that ambitious, high-intelligence people fall into.  
> When the number of possible paths is large and the cost of choosing wrong feels high, your brain delays commitment. Planning becomes the activity instead of the means to an activity.

**POLYMATH.SYS** is the cure. It replaces infinite optionality with a structured, phased, 48-month execution system that maps every single module across AI, Mathematics, and Quantum Mechanics into one coherent roadmap.

<br>

## ✦ Key Features

| Feature | Description |
|:---|:---|
| 📖 **Editorial Book Layout** | Each curriculum phase is displayed as a textbook chapter with a spine, table of contents, and explicit module listings |
| 🧭 **Full Circular Syllabus** | A borderless, structured table view of the entire 48-month curriculum |
| 📝 **Research Blog** | Asymmetrical magazine-style layout with featured articles and sidebar |
| 🗄️ **Archival Vault** | Dense file-directory grid for papers, cheatsheets, and code notebooks |
| 🏢 **Deep Tech Directory** | Portfolio-style grid of 9 major AI companies with sector tags |
| 🧬 **Great Minds Index** | Avatar-card grid profiling 10 pioneers of AI and Deep Learning |
| 📚 **Resource Library** | Split-panel layout — GitHub repos (with star ratings) + Research papers (PapersWithCode links) |
| 📐 **System Methodology** | Structured appendix documenting Spaced Repetition, Interleaving, and Feynman Diagnostics |
| 🎯 **OSP Article** | Full standalone article on Optimal Strategy Paralysis with tabbed interactive content |

<br>

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                        POLYMATH.SYS                              │
│                                                                  │
│  ┌─────────────┐    ┌──────────────────────────────────────┐    │
│  │  MANIFESTO   │    │         HERO / ABOUT                 │    │
│  │  (OSP Intro) │    │     "The Full Circular"              │    │
│  │  + CTA       │    │     + View Circular Button           │    │
│  └──────┬───────┘    └──────────────┬───────────────────────┘    │
│         │                           │                            │
│  ┌──────▼───────────────────────────▼───────────────────────┐    │
│  │              CURRICULUM STRUCTURE                         │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │    │
│  │  │ POLYMATH  │ │ PHASE I  │ │ PHASE II │ │ PHASE III│   │    │
│  │  │ BLUEPRINT │ │ FOUND.   │ │ DEEP AI  │ │ FRONTIER │   │    │
│  │  │ [Spine]   │ │ [Spine]  │ │ [Spine]  │ │ [Spine]  │   │    │
│  │  │ [TOC]     │ │ [TOC]    │ │ [TOC]    │ │ [TOC]    │   │    │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘   │    │
│  └──────────────────────────────────────────────────────────┘    │
│                           │                                      │
│  ┌────────────────────────▼─────────────────────────────────┐    │
│  │ BLOG (Asymmetric) │ VAULT (Dense Grid)                   │    │
│  ├────────────────────┼─────────────────────────────────────┤    │
│  │ METHODOLOGY        │ RESOURCES (Git + Papers Split)      │    │
│  ├────────────────────┼─────────────────────────────────────┤    │
│  │ COMPANIES (Portfolio)  │ GREAT MINDS (Avatar Grid)       │    │
│  └──────────────────────────────────────────────────────────┘    │
│                           │                                      │
│  ┌────────────────────────▼─────────────────────────────────┐    │
│  │                    SYSTEM FOOTER                          │    │
│  │   Brand  │  Curriculum  │  Sections  │  Ecosystem        │    │
│  └──────────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────────┘
```

<br>

## 📁 Project Structure

```
Eng/
│
├── AI Research Eng/                    # Main Portal
│   ├── index.html                      # Landing page (all sections)
│   ├── styles.css                      # Global design system (~750 lines)
│   ├── script.js                       # Tab/accordion interactivity
│   ├── circular.html                   # Full circular syllabus view
│   ├── polymath_master_roadmap.html    # Master strategy (Months 1-48)
│   ├── phase1_learning_roadmap.html    # Phase I: Foundations (Months 1-12)
│   ├── phase2_deep_roadmap.html        # Phase II: Deep AI (Months 13-24)
│   └── phase3_frontier_roadmap.html    # Phase III: The Frontier (Months 25-48)
│
├── Polymath Identity Article/          # Standalone Article
│   ├── index.html                      # OSP article (dark editorial styling)
│   └── optimal_strategy_paralysis.html # Original source content
│
└── README.md                           # This file
```

<br>

## 🎨 Design System

The platform uses a **Brutalist Editorial** aesthetic — high-contrast dark mode with strict geometric constraints.

| Token | Value | Usage |
|:---|:---|:---|
| `--bg` | `#0b0b0b` | Page background |
| `--card-bg` | `#0e0e0e` | Card surfaces |
| `--card-border` | `#1e1e1e` | Hairline borders |
| `--text-primary` | `#ffffff` | Headlines |
| `--text-secondary` | `#888888` | Body copy |
| `--accent` | `#e3b341` | GitHub stars, warnings |
| Font | `Inter` | All typography |
| Border Radius | `8px` | Cards, `6px` for small elements |

### Layout Taxonomy

Every section uses a **unique grid architecture** to prevent visual monotony:

| Section | Layout Type | Grid Definition |
|:---|:---|:---|
| Curriculum | Book Index | `280px / 1fr` (spine + pages) |
| Blog | Asymmetric Magazine | `2fr / 1.2fr` |
| Document Vault | Dense Matrix | `repeat(auto-fill, minmax(220px, 1fr))` |
| Methodology | Appendix List | `80px / 240px / 1fr` |
| Resources | Split Panel | `1fr / 1fr` |
| Companies | VC Portfolio | `repeat(auto-fill, minmax(280px, 1fr))` |
| Great Minds | Avatar Grid | `repeat(auto-fill, minmax(200px, 1fr))` |
| Footer | 4-Column Directory | `1.8fr / 1fr / 1fr / 1fr` |

<br>

## 📚 The Curriculum (48 Months)

<table>
<tr>
<td width="25%" align="center">

### ◼ Master Blueprint
**Months 1–48**

The overarching strategic arc connecting all phases

</td>
<td width="25%" align="center">

### 📐 Phase I
**Months 1–12**

`Linear Algebra`  
`Calculus`  
`Data Structures`  
`Classical ML`

</td>
<td width="25%" align="center">

### 🔬 Phase II
**Months 13–24**

`PyTorch`  
`Transformers`  
`Cloud (AWS/GCP)`  
`MLOps & CI/CD`

</td>
<td width="25%" align="center">

### 🌌 Phase III
**Months 25–48**

`Quantum Theory`  
`QML`  
`Quant Finance`  
`Publications`

</td>
</tr>
</table>

<br>

## 🔗 Ecosystem Links

### Top GitHub Repositories
| Repository | Stars | Description |
|:---|:---|:---|
| [huggingface/transformers](https://github.com/huggingface/transformers) | ★ 138k | State-of-the-art NLP for PyTorch, TF, JAX |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | ★ 86k | Tensors and dynamic neural networks |
| [ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) | ★ 73k | LLM inference in C/C++ |
| [ollama/ollama](https://github.com/ollama/ollama) | ★ 105k | Run LLMs locally |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | ★ 98k | Composable LLM application chains |

### Landmark Research Papers
| Year | Paper | Link |
|:---|:---|:---|
| 2017 | Attention Is All You Need | [PapersWithCode](https://paperswithcode.com/paper/attention-is-all-you-need) |
| 2020 | Denoising Diffusion Probabilistic Models | [PapersWithCode](https://paperswithcode.com/paper/denoising-diffusion-probabilistic-models) |
| 2021 | LoRA: Low-Rank Adaptation | [PapersWithCode](https://paperswithcode.com/paper/lora-low-rank-adaptation-of-large-language) |
| 2023 | Direct Preference Optimization (DPO) | [PapersWithCode](https://paperswithcode.com/paper/direct-preference-optimization-your-language) |
| 2024 | The Llama 3 Herd of Models | [PapersWithCode](https://paperswithcode.com/paper/the-llama-3-herd-of-models) |

<br>

## 🧬 Great Minds Featured

<table>
<tr>
<td align="center" width="20%"><strong>Geoffrey Hinton</strong><br><sub>Godfather of DL · Turing Award</sub></td>
<td align="center" width="20%"><strong>Yann LeCun</strong><br><sub>Chief AI Scientist, Meta</sub></td>
<td align="center" width="20%"><strong>Yoshua Bengio</strong><br><sub>Pioneer of DL · Turing Award</sub></td>
<td align="center" width="20%"><strong>Ilya Sutskever</strong><br><sub>Co-founder SSI</sub></td>
<td align="center" width="20%"><strong>Andrej Karpathy</strong><br><sub>Former Dir. AI, Tesla</sub></td>
</tr>
<tr>
<td align="center"><strong>Demis Hassabis</strong><br><sub>CEO, Google DeepMind</sub></td>
<td align="center"><strong>Ashish Vaswani</strong><br><sub>Transformer Co-inventor</sub></td>
<td align="center"><strong>Fei-Fei Li</strong><br><sub>Stanford HAI · ImageNet</sub></td>
<td align="center"><strong>Ian Goodfellow</strong><br><sub>Inventor of GANs</sub></td>
<td align="center"><strong>Dario Amodei</strong><br><sub>CEO, Anthropic</sub></td>
</tr>
</table>

<br>

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/AyushSahoo19/AI-Eng.git

# Navigate to the project
cd AI-Eng

# Open in browser (no build step needed — pure static HTML)
start "AI Research Eng/index.html"
```

> **No dependencies. No build tools. No framework.** Pure HTML, CSS, and JavaScript — opens instantly in any browser.

<br>

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|:---|:---|:---|
| **Structure** | HTML5 | Semantic markup |
| **Styling** | Vanilla CSS | Custom design system with CSS variables |
| **Typography** | [Inter](https://fonts.google.com/specimen/Inter) | Premium sans-serif via Google Fonts |
| **Interactivity** | Vanilla JS | Tab switching, accordions, checkboxes |
| **Hosting** | Static | Deployable to GitHub Pages, Netlify, Vercel |

<br>

## 📄 System Methodology

The platform implements three evidence-based learning protocols:

> **`[M.01]` Spaced Repetition** — Mathematically timed reviews at the edge of the forgetting curve  
> **`[M.02]` Interleaved Practice** — Scrambled cross-domain study to force structural pattern recognition  
> **`[M.03]` Feynman Diagnostics** — Teaching concepts back to the AI system as the primary assessment method

<br>

---

<div align="center">

**◼ POLYMATH.SYS** · *Built for the ambitious few who refuse to choose between depth and breadth.*

<sub>© 2026 Polymath.Sys — Strictly Academic & Research Scope · VERSION 3.0</sub>

</div>
