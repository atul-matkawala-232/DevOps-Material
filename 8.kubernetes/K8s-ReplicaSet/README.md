# ☸️ Kubernetes: Replication Controller & ReplicaSet

A beginner-friendly, **interactive** guide to Kubernetes RC and ReplicaSet — with live pod simulations, collapsible sections, tab panels, and a selector playground. No frameworks, no build step.

## 🚀 View it live (GitHub Pages)

1. Fork or upload this repo to GitHub
2. Go to **Settings → Pages**
3. Under *Source*, select **Deploy from a branch → main → / (root)**
4. Click **Save** — your guide will be live at:
   `https://<your-username>.github.io/<repo-name>/`

## 📁 Files

| File | Description |
|------|-------------|
| `index.html` | The complete interactive guide (single file, no dependencies) |
| `README.md` | This file |

## ✨ Features

- **8 collapsible sections** — click any heading to expand/collapse
- **Tab panels** inside sections (YAML / Explanation / Lifecycle)
- **Live pod simulation** — kill pods, scale replicas, watch the controller react
- **Selector playground** — change pod labels and see if they match the RS selector
- **YAML code blocks** with syntax highlighting
- **Side-by-side RC vs RS comparison**
- **kubectl cheat sheet** table
- Works entirely offline — pure HTML/CSS/JS, zero dependencies

## 🖥️ Run locally

Just open the file in any browser:

```bash
open index.html         # macOS
xdg-open index.html     # Linux
start index.html        # Windows
```

Or serve it with Python:

```bash
python3 -m http.server 8080
# then open http://localhost:8080
```
