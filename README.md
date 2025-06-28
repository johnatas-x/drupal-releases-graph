# Drupal Releases Lifecycle Graph

This Python script generates a visual timeline of the maintenance and security lifecycle for recent **Drupal versions (10.3 to 11.3)** using color-coded horizontal bars.

- ✅ **Green**: The version is actively maintained.
- 🟡 **Yellow**: Security fixes only.
- 🔴 **Red**: The version is no longer supported.
- 📍 A vertical dotted line indicates **today's date**.
- ⏳ Versions are sorted chronologically (oldest at the top).
- ⚠️ **Future dates are estimates** and will be updated when official release/support dates are confirmed by the Drupal team.

---

## 📸 Output

The chart displays:
- The version number on the left, with a background color matching the current support level.
- A time-based X-axis labeled in **French**, showing the month and year.
- Faded bars for phases **that are in the past**, to visually distinguish historical from current/future periods.
- A legend in the **top-right corner**.

---

## 🛠️ Requirements

Ensure Python and required libraries are installed.

### Step-by-step installation on Ubuntu <ins>example</ins>:

```bash
# Install Python.
sudo apt update
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3.12-venv

# Create and activate a virtual environment.
python3 -m venv .venv
source .venv/bin/activate

# Install required Python packages.
pip install matplotlib pandas

# Run the script.
python drupal_releases_graph.py

# Deactivate the virtual environment when done.
deactivate
```

---

## 🖼️ Output Behavior

By default, the script will **open a preview window** showing the generated chart.  
This allows you to tweak the layout and manually export it if needed.

To **automatically export the chart as a PNG without preview**, edit the file:

- **Comment out** the preview line:
  ```python
  plt.show()
  ```
- **Uncomment** the PNG export lines:
  ```python
  plt.savefig("drupal_versions_lifecycle.png", dpi=300)
  print("✅ File saved: drupal_versions_lifecycle.png")
  ```

These lines are located near the end of the script (`drupal_releases_graph.py`, around line 137).

---

## 📂 Output File

When the preview is disabled, the chart will be saved as:

```
drupal_versions_lifecycle.png
```

in the same directory as the script.

---

## 📌 Notes

- This chart can help teams anticipate version transitions and end-of-life deadlines.
- If you'd like to generate an SVG version or change language settings, feel free to adapt the script.

---
