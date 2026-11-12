# Unified reference style module for all data figures (locked 2026-11-09):
# thick black left/bottom axes with outward ticks, black-edged patches, and
# flat fills in dark navy / pale yellow / pale mint. All figure scripts take
# colors and axis styling from here so the 13 data figures stay visually
# consistent.
import matplotlib
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

NAVY = (0x26/255, 0x21/255, 0x5E/255)   # dark navy: main model / first series
YEL  = (0xE4/255, 0xE6/255, 0x6B/255)   # pale yellow: control / second series
MINT = (0xC2/255, 0xE6/255, 0xD1/255)   # pale mint: third series (rarely used)
INK  = (0.0, 0.0, 0.0)                  # pure black for axes and edges
GRAY = (0.55, 0.55, 0.55)               # gray for references and annotations


def style_ax(ax, lw=2.2):
    """Reference-style axes: closed black frame on all four sides, ticks and
    tick labels outside the frame."""
    for s in ('top', 'right', 'left', 'bottom'):
        ax.spines[s].set_visible(True)
        ax.spines[s].set_color(INK)
        ax.spines[s].set_linewidth(lw)
    ax.tick_params(direction='out', width=1.2, length=4, colors=INK)


def flush_end_labels(fig, tol_pt=3.0):
    """Flush-align the top and bottom y-axis tick labels: the lowest label is
    top-aligned and the highest label bottom-aligned, so the label stack sits
    fully outside the closed frame instead of straddling the axis line (which
    lets 0 float above the x-axis). Uses display coordinates, so reversed axes
    are handled correctly. Tolerant: an end tick is flush-aligned only if it
    sits within tol_pt of the frame edge; ticks floating inside the frame keep
    centered alignment so labels never hang in empty space. Call once per
    figure before savefig."""
    fig.canvas.draw()
    tol = tol_pt * fig.dpi / 72.0
    for ax in fig.axes:
        labs = ax.get_yticklabels()
        if len(labs) < 3:
            continue
        bb_lo = ax.spines['bottom'].get_window_extent()
        bb_hi = ax.spines['top'].get_window_extent()
        if bb_lo is None or bb_hi is None:
            continue
        c_lo = bb_lo.y0 + bb_lo.height / 2   # bottom-edge centerline (display coords)
        c_hi = bb_hi.y0 + bb_hi.height / 2   # top-edge centerline
        cents = [(l.get_window_extent().y0 + l.get_window_extent().y1) / 2
                 for l in labs]
        i_lo = min(range(len(labs)), key=lambda i: cents[i])
        i_hi = max(range(len(labs)), key=lambda i: cents[i])
        if abs(cents[i_lo] - c_lo) <= tol:
            labs[i_lo].set_verticalalignment('top')
        if abs(cents[i_hi] - c_hi) <= tol:
            labs[i_hi].set_verticalalignment('bottom')


def patch(facecolor, label, hatch=None):
    """Legend patch with black edge (reference style)."""
    return Patch(facecolor=facecolor, edgecolor=INK, linewidth=1.2,
                 hatch=hatch, label=label)


def line(color, label, ls='-', marker=None, ms=4.0, lw=1.8):
    """Line2D legend handle with markers and black edges."""
    kw = dict(color=color, label=label, ls=ls, lw=lw)
    if marker:
        kw.update(marker=marker, ms=ms, mfc=color, mec=INK, mew=0.8)
    return Line2D([0], [0], **kw)
