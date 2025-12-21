import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

def draw_big_clear_contradiction():
    # --- 1. DEFINE THE IDEAL POINTS FOR MAXIMAL CLARITY ---
    # We define 3 points per curve to ensure they shape correctly and pass
    # exactly where we want them to show the big gap.
    
    # Intersection Point (I)
    nx_int, ny_int = 8, 8

    # The comparison X-coordinate (to the left of intersection)
    comparison_x = 2

    # Point A (on Blue IC1 - High up)
    nx_a, ny_a = comparison_x, 28
    # Third point for Blue IC1 to define shape to the right
    nx_a_right, ny_a_right = 22, 4

    # Point B (on Red IC2 - Significantly lower than A)
    nx_b, ny_b = comparison_x, 16
    # Third point for Red IC2 (must cross above Blue on the right)
    nx_b_right, ny_b_right = 22, 6

    # --- 2. GENERATE SMOOTH CURVES (Interpolation) ---
    # Group points for spline generation
    # x must be sorted for interpolation
    x1_pts = np.array([nx_a, nx_int, nx_a_right])
    y1_pts = np.array([ny_a, ny_int, ny_a_right])
    
    x2_pts = np.array([nx_b, nx_int, nx_b_right])
    y2_pts = np.array([ny_b, ny_int, ny_b_right])

    # Create dense X range for smooth plotting
    x_dense = np.linspace(min(x1_pts), max(x1_pts), 500)

    # Generate Quadratic Spline (k=2) for smooth curves through the points
    spl1 = make_interp_spline(x1_pts, y1_pts, k=2)
    y1_dense = spl1(x_dense)
    
    spl2 = make_interp_spline(x2_pts, y2_pts, k=2)
    y2_dense = spl2(x_dense)

    # --- 3. PLOTTING ---
    # Make the figure BIG
    plt.figure(figsize=(14, 10))

    # Plot Curves with thick lines
    plt.plot(x_dense, y1_dense, color='#0055D4', linewidth=4, label='IC1 (Blue)')
    plt.plot(x_dense, y2_dense, color='#D40000', linewidth=4, label='IC2 (Red)')

    # Plot Key Points with LARGE markers
    # Intersection
    plt.scatter(nx_int, ny_int, color='black', zorder=10, s=250, edgecolor='white', linewidth=2)
    
    # Points A and B
    plt.scatter(nx_a, ny_a, color='#0055D4', zorder=10, s=200, edgecolor='black', linewidth=1)
    plt.scatter(nx_b, ny_b, color='#D40000', zorder=10, s=200, edgecolor='black', linewidth=1)

    # --- 4. ANNOTATIONS & CLARITY FEATURES ---
    
    # Big prominent vertical line showing the "Gap"
    plt.plot([comparison_x, comparison_x], [0, 30], color='gray', linestyle='--', linewidth=2, alpha=0.5)
    plt.text(comparison_x, 0.5, f'Fixed X = {comparison_x}', color='gray', 
             ha='center', fontsize=12, weight='bold')

    # Labels with large fonts
    offset_x = 0.8
    # A
    plt.text(nx_a + offset_x, ny_a, f'Point A\n({nx_a}, {ny_a})\n[More Y]', 
             color='#0055D4', fontsize=14, weight='bold', va='center')
    # B
    plt.text(nx_b + offset_x, ny_b, f'Point B\n({nx_b}, {ny_b})\n[Less Y]', 
             color='#D40000', fontsize=14, weight='bold', va='center')
    # Intersection
    plt.text(nx_int + offset_x, ny_int + 0.5, f'Intersection\n({nx_int}, {nx_int})', 
             color='black', fontsize=14, weight='bold')

    # Arrows showing connection to intersection
    arrow_style = dict(arrowstyle="->", lw=2.5, alpha=0.6)
    plt.annotate('', xy=(nx_int, ny_int), xytext=(nx_a+0.5, ny_a-1), arrowprops=dict(color='#0055D4', **arrow_style))
    plt.annotate('', xy=(nx_int, ny_int), xytext=(nx_b+0.5, ny_b+1), arrowprops=dict(color='#D40000', **arrow_style))


    # --- 5. THE EXPLANATION BOX ---
    box_text = (
        "THE CONTRADICTION:\n\n"
        "1. A is on Blue IC, I is on Blue IC  =>  A ~ I\n"
        "2. B is on Red IC, I is on Red IC    =>  B ~ I\n"
        "3. Transitivity implies: A must be ~ B\n\n"
        "REALITY CHECK (Look at the gap at X=2):\n"
        "A has MUCH more Y than B (28 vs 16).\n"
        "A rational person MUST prefer A over B (A > B).\n\n"
        "Conclusion: Intersecting ICs are logically impossible."
    )
    plt.text(12, 18, box_text, fontsize=13, 
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=1', linewidth=2))

    # --- 6. FINISHING TOUCHES ---
    plt.title('Proof: Why Indifference Curves Cannot Intersect', fontsize=20, pad=20)
    plt.xlabel('Quantity of Good X', fontsize=16, labelpad=10)
    plt.ylabel('Quantity of Good Y', fontsize=16, labelpad=10)
    
    # Set axes limits wide to let the diagram breathe
    plt.xlim(0, 25)
    plt.ylim(0, 35)
    
    # Bigger tick labels
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    plt.grid(True, alpha=0.15)
    plt.legend(fontsize=14, loc='upper right')
    
    plt.tight_layout()
    plt.savefig('big_better_contradiction.png')
    plt.show()

if __name__ == "__main__":
    draw_big_clear_contradiction()