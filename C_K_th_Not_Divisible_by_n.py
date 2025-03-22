# Adjusting figure size and coordinates to ensure proper layout
fig, ax = plt.subplots(figsize=(12, 22))
ax.set_xlim(0, 10)
ax.set_ylim(-4, 18)
ax.axis('off')

# Create a function to draw a box with text
def draw_box(ax, xy, text, box_color='lightgrey', text_color='black'):
    box = patches.FancyBboxPatch(xy, 10, 1, boxstyle="round,pad=0.3", ec="black", fc=box_color)
    ax.add_patch(box)
    ax.text(xy[0] + 5, xy[1] + 0.5, text, ha='center', va='center', color=text_color, fontsize=10, wrap=True)

# List of process steps with coordinates and descriptions
steps = [
    (8, 17, "Start"),
    (8, 15, "Initial Filtering\nCriteria: Exclude datasets without description files or with empty folders\nOutput: 9049 IDs, 9624 files"),
    (8, 13, "Unzipping Files\nOutput: 9049 IDs, 9659 files"),
    (8, 11, "Structured Data Filtering\nCriteria: Retain structured data formats (e.g., Excel, CSV, TSV, MTX)\nOutput: 1920 IDs, 2135 files"),
    (8, 9, "File Format Conversion\nConvert all eligible files to CSV format\nOutput: 1906 IDs, 6546 CSV files"),
    (8, 7, "Final Readability Check\nEnsure all CSV files are readable and not corrupted\nOutput: 1906 IDs, 6500 readable CSV files"),
    (8, 5, "Column Analysis\nCategorize files based on the presence of unnamed columns:\n- Less than 50% Unnamed Columns\n- More than 50% Unnamed Columns\n- All Unnamed Columns\nData Refinement:\n- Retain files with more than 50% unnamed columns\n- Drop unnamed columns or use the second row as headers for files with less than 50% unnamed columns\nOutput: 1881 IDs"),
    (8, 3, "Dataset Structuring\nCreate a consolidated CSV file:\n- Column 1: Dataset IDs\n- Column 2: Descriptions\nOutput: Structured dataset for further analysis"),
    (8, 1, "Description Embedding Generation\nModel: Sentence BERT (all-MiniLM-L6-v2)\nGenerate 384-dimensional embeddings for each description\nOutput: Embeddings stored with corresponding dataset IDs"),
    (8, -1, "Cosine Similarity Matrix Construction\nMeasure similarity between descriptions using cosine similarity\nCreate a cosine similarity matrix and binary representation\nOutput: Similarity matrix for analysis"),
    (8, -3, "End"),
]

# Draw each step
for step in steps:
    draw_box(ax, (step[0] - 5, step[1]), step[2])

# Draw arrows between the steps
for i in range(len(steps) - 1):
    ax.annotate("", xy=(steps[i + 1][0], steps[i + 1][1] + 1), xytext=(steps[i][0], steps[i][1] - 0.3),
                arrowprops=dict(arrowstyle="->", color='black'))

# Save the image
plt.savefig('/mnt/data/flowchart_final_v2.png')

plt.show()
