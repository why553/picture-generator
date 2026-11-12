---
name: research-figure-style
description: Draw publication-quality research figures (matplotlib data figures and TikZ pipeline diagrams) under a locked house style. Use when creating or restyling any paper/report figure, including line plots, bar charts, profile plots, multi-panel subplots, and method pipeline diagrams, especially when visual consistency across many figures matters or when the user mentions 画图规范, 科研配色, refstyle, or 论文图.
---

# Research Figure Style

Locked house style for all paper figures. Data figures take colors and axis
styling from `scripts/refstyle.py`. Never hardcode palette values in figure
code; import them.

## Part 1: matplotlib data figures

### Workflow

1. Copy `scripts/refstyle.py` next to the figure script (or import it from a
   shared location) and use it for every axes:

```python
import refstyle as R
fig, ax = plt.subplots()
R.style_ax(ax)
ax.plot(x, y, color=R.NAVY)
```

2. Series colors: NAVY = main model / first series, YEL = control / second
   series, MINT = third series (rare). GRAY only for reference lines and
   annotations. Flat fills, black edges on every patch.
3. Panel labels `(a) ...`, `(b) ...`: same height across panels, centered
   horizontally under each panel (`ax.set_xlabel` position or explicit text at
   the panel bottom center). Never top-left corner labels.
4. Legends: place in an empty corner or fully outside below the figure
   (`bbox_to_anchor`); never overlap data. Multi-panel figures share ONE
   legend row instead of repeating per panel. Keep symbol-to-label spacing
   uniform.
5. Before `savefig`, call `R.flush_end_labels(fig)` so the top and bottom
   y-tick labels sit flush outside the closed frame and 0 does not float.
6. Save with `bbox_inches="tight"`.

### Hard rules

- Closed black frame on all four sides, ticks pointing outward.
- Grayscale safety: every series pair must be distinguishable by line style or
  shade alone, not color alone.
- No saturated colors. No corner labels. No legend on top of data.
- Font size floor: `\tiny` equivalent in LaTeX-embedded figures.

## Part 2: TikZ pipeline diagrams

For method pipeline / architecture diagrams, read
[references/tikz-pipeline.md](references/tikz-pipeline.md) and follow its
card layout, palette, and compile-check workflow.

## Verification checklist (mandatory)

After generating any figure:

1. Render to PNG and inspect at 200% zoom.
2. Confirm: closed frame, outward ticks, panel labels bottom-centered and
   same-height, legend in empty space, zero label overlaps, grayscale
   distinguishable (simulate or eyeball in gray).
3. Fix and re-render until clean. Never ship a figure that has not been
   visually inspected.
