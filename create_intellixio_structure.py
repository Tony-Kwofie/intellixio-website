import os

# Root project folder
root = "intellixio-website"

# Folder structure
folders = [
    root,
    os.path.join(root, "products"),
    os.path.join(root, "assets"),
    os.path.join(root, "assets", "css"),
    os.path.join(root, "assets", "js"),
    os.path.join(root, "assets", "images"),
    os.path.join(root, "assets", "icons"),
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Files to create
files = [
    os.path.join(root, "index.html"),
    os.path.join(root, "products.html"),
    os.path.join(root, "industries.html"),
    os.path.join(root, "about.html"),
    os.path.join(root, "careers.html"),
    os.path.join(root, "contact.html"),
    os.path.join(root, "privacy-policy.html"),
    os.path.join(root, "terms-of-service.html"),
    os.path.join(root, "products", "intellixio-ops.html"),
    os.path.join(root, "assets", "css", "style.css"),
    os.path.join(root, "assets", "css", "components.css"),
    os.path.join(root, "assets", "css", "animations.css"),
    os.path.join(root, "assets", "css", "responsive.css"),
    os.path.join(root, "assets", "js", "main.js"),
    os.path.join(root, "assets", "js", "animations.js"),
    os.path.join(root, "assets", "images", "logo2.jpg"),
    os.path.join(root, "assets", "images", "founder.jpg"),
    os.path.join(root, "assets", "images", "ai-cityscape.jpg"),
    os.path.join(root, "assets", "images", "ops-logo.png"),
    os.path.join(root, "sitemap.xml"),
]

# Create empty files
for file in files:
    if not os.path.exists(file):
        with open(file, "w", encoding="utf-8") as f:
            pass

print("✅ Intellixio website structure created successfully!")
print(f"📁 Location: {os.path.abspath(root)}")
