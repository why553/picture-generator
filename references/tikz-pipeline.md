# TikZ Pipeline Diagram Rules

For method pipeline / architecture figures compiled with pdflatex.

## Layout

- Card layout: every module is a rounded-rectangle box, arrows connect cards.
- Highlight the novel contribution module with a bold frame and a distinct
  background. Mark its scope with a brace labeled "Our Contribution".
- Compact layout: minimize whitespace, align cards horizontally and
  vertically. Horizontal chain for 3-6 stage pipelines; vertical chain for
  narrow single-column slots; U-shape for iterative loops (GAN, RL).

## Palette

Low-saturation pastel only, no saturated colors. Default scheme Blue-Gray
(general pipelines), alternatives: Warm Tones (highlighting novelty),
Green-Cyan (generation, biology), Purple-Blue (theory, math), Monochrome
(print-friendly).

## Typography and strokes

- sans-serif throughout (`\sffamily`).
- Stealth (latex-style) arrows, never bare lines.
- Shared legend row at figure bottom for repeated symbols, with fixed spacing
  between legend items. Never per-panel legend repetition.

## Workflow

1. Generate a standalone `.tex` (`standalone` document class).
2. Compile with pdflatex (first run may need `-enable-installer` on MiKTeX to
   fetch packages).
3. Convert PDF to PNG with pdftoppm or pypdfium2, then inspect the render:
   arrow crossings, label overlaps, legend spacing, text overflow.
4. Iterate until the render passes the Part 1 verification checklist.
