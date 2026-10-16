# Read your original CSV file
with open("SongListFile.csv", "r", encoding="utf-8") as f:
    csv_content = f.read()

# 1. Escape any backslashes first (so they don't break string formatting)
safe_content = csv_content.replace("\\", "\\\\")

# 2. Safely escape any backticks hiding inside song titles/artists
safe_content = safe_content.replace("`", "\\`")

# 3. Escape dollar signs to prevent JavaScript template string interpolation (${...})
safe_content = safe_content.replace("${", "\\${")

# Wrap it into the JavaScript template string
js_code = f"const DEFAULT_CSV_DATA = `{safe_content}`;"

# Save to songs_bundle.js
with open("songs_bundle2.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Conversion complete! 'songs_bundle.js' is safely formatted with multi-line layout.")