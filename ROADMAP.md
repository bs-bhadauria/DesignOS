# DesignOS Roadmap

**Project Status:** Active Development
**Architecture Version:** v2.0 (Lean 2-Stage Context-Injected Pipeline)

---

# Vision
DesignOS is an AI-native document engineering platform designed to generate professional documents through an intelligent, highly-optimized 2-Stage pipeline:
1. **Stage 1 (Content Planner)**: Formulates copywriting and outlines the structure.
2. **Stage 2 (Design Engine)**: Performs freehand HTML/Tailwind styling, incorporating the **original user prompt and multimodal files** (photos, sketches, PDFs, screenshots) alongside the JSON outline (Shared Context Ingestion).

# Engineering Principles
- **Context Injection**: Stage 2 is never visually blind; it receives both JSON outline data and the raw user prompt/creative inputs (including images, documents, and screenshots).
- **Simplicity over Complexity**: Direct HTML generation instead of rigid multi-agent data structures.
- **Evolution through Prompts**: Scale by adding new templates (Resumes, Newsletters), not new agents.
- **Provider independence**: Easy integration with Open Source models.

---

# Current Status

## Completed
- Repository setup (Backend & Frontend)
- FastAPI & Next.js integration
- Gemini integration via Provider Factory
- **Architecture Refactor**: Transitioned from a complex 5-Agent DDOM system to a Lean 2-Stage Pipeline (`content_planner` -> `renderer`).
- Codebase cleanup (Archived legacy files).
- Created Pelican riding a bicycle HTML PoC.

## In Progress
- Refactoring `DocumentAgent` to inject the original user prompt directly into Stage 2 rendering context.
- Preparing for Presentation Mode UI.

---

# Upcoming Milestones

## Milestone 1: Interactive Presentations & Layouts (Current Focus)
- Implement presentation mode in frontend (slide-by-slide horizontal navigation).
- Enrich Stage 2 render prompts to produce dynamic animations and layouts based on injected user prompts and multimodal files.

## Milestone 2: Open-Source Model Support
- Add connectors for Open Source models (Llama 3, Qwen) via Ollama/Groq.
- Benchmark local model performance for Stage 1.

## Milestone 3: HTML/SVG Flow Diagrams & Animations
- Add CSS/SVG guidelines to renderer instructions to make flowcharts and data migrations animate natively.

## Milestone 4: Export & Distribution
- HTML to PDF / PPTX / Markdown export.