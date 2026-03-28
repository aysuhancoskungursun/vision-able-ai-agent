# Vision-Able — AI-Powered Accessible Navigation

> **Team Impact** | Microsoft AI for Good Hackathon 2026

Vision-Able is a mobile-first web application that uses AI vision to detect accessibility hazards (blocked sidewalks, traffic signals, stairs without ramps) and provides real-time voice alerts and alternative route suggestions for visually impaired, wheelchair, and mobility-impaired users.

---

## Quick Start (Local)

No build step required — it's a single HTML file.

```bash
cd vision-able-web
python3 -m http.server 8080
# Open http://localhost:8080
```

---

## Project Structure

```
vision-able-web/
├── index.html                 # Entire app (HTML + CSS + JS)
├── staticwebapp.config.json   # Azure Static Web Apps config
├── README.md
└── assets/
    ├── sidewalk_obstacle.jpg  # Scenario 1 photo
    ├── traffic_light.jpg      # Scenario 2 photo
    └── stairs_no_ramp.jpg     # Scenario 3 photo
```

---

## Deploy to Azure Static Web Apps

### Option A — Azure Portal (quickest)

1. Go to [Azure Portal](https://portal.azure.com) → Create a resource → **Static Web App**
2. Connect your GitHub repo (`vision-able-ai-agent`)
3. Set **App location** to `/` (root)
4. Set **Output location** to empty (leave blank)
5. Click **Review + Create** → Azure auto-deploys on every push

### Option B — Azure CLI

```bash
# Login
az login

# Create resource group (if needed)
az group create --name rg-vision-able --location westeurope

# Create static web app
az staticwebapp create \
  --name vision-able-app \
  --resource-group rg-vision-able \
  --source https://github.com/YOUR_USERNAME/vision-able-ai-agent \
  --branch main \
  --app-location "/" \
  --output-location "" \
  --login-with-github
```

### Option C — VS Code

1. Install **Azure Static Web Apps** extension
2. Right-click `vision-able-web` folder → **Deploy to Static Web App**
3. Follow the wizard

---

## How It Works

The app has **4 tabs**:

| Tab | Description |
|-----|-------------|
| 🚧 Sidewalk | Pre-loaded Istanbul sidewalk obstacle scenario |
| 🚦 Traffic | Red pedestrian traffic light scenario |
| 🪜 Stairs | Staircase with no wheelchair ramp scenario |
| 🔴 Go Live | Open camera or upload photo for real-time analysis |

### Mock Mode (default)

All 3 scenario tabs use pre-defined responses — no API key needed. Perfect for demos.

### Live AI Mode

Toggle the switch in the **Go Live** tab to enable real-time AI analysis.

---

## Connecting Your AI API

### Where to enter API keys

1. Open the app → click the **Go Live** tab
2. Toggle **"Mock Mode"** → it switches to **"Live AI Mode"**
3. Three fields appear:

| Field | What to enter |
|-------|---------------|
| **Azure OpenAI Endpoint** | `https://YOUR-RESOURCE.openai.azure.com` |
| **API Key** | Your Azure OpenAI API key |
| **Deployment Name** | Your model deployment name (e.g., `gpt-4o`) |

### Using Copilot Studio instead

If you're using **Microsoft Copilot Studio** as the backend agent:

1. Create your agent in Copilot Studio with vision capabilities
2. Get the **Direct Line token** and **endpoint URL**
3. In `index.html`, find the `callAzureVision()` function (~line 490)
4. Replace the API call with your Copilot Studio endpoint:

```javascript
// Change this:
const url = `${endpoint}/openai/deployments/${deployment}/chat/completions?api-version=2024-12-01-preview`;

// To your Copilot Studio endpoint:
const url = `https://YOUR-COPILOT-ENDPOINT/api/messages`;
```

5. Adjust the request payload to match Copilot Studio's format

---

## Features

- **Mobile-first** — designed as a phone app, works on any device
- **3 pre-built scenarios** — ready for jury demo, no setup needed
- **Live camera** — opens device camera, capture & analyze in real-time
- **Photo upload** — fallback for devices without camera access
- **Persona switching** — Visual / Wheelchair / Mobility — changes agent responses
- **Streaming agent messages** — Vision Agent → Alert Agent → Navigation Agent
- **Voice output** with typewriter effect
- **Alternative route suggestions** with accessibility scores
- **Mock ↔ Live API** — single toggle switch, no code changes needed
- **Zero dependencies** — pure HTML/CSS/JS, no build step

---

## Demo Flow (3-5 minutes)

1. App opens → splash screen → dark premium UI
2. Select persona: **"Visually Impaired"**
3. **Tab 1** → See the blocked sidewalk → tap **Analyze** → watch agents stream results
4. **Tab 2** → Red traffic light → agent says "STOP, do not cross"
5. **Tab 3** → Stairs with no ramp → agent finds elevator alternative
6. **Tab 4 (Go Live)** → Open camera → capture a real photo → get AI analysis
7. Jury is impressed ✨

---

## Tech Stack

- **Frontend**: Pure HTML5, CSS3, JavaScript (ES6+)
- **AI Backend**: Azure OpenAI GPT-4o Vision / Microsoft Copilot Studio
- **Hosting**: Azure Static Web Apps
- **Design**: Dark theme, glassmorphism, Fluent-inspired animations

---

*Built for the Microsoft AI for Good Hackathon 2026*
