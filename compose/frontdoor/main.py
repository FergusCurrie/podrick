from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Podrick Dashboard")


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Podrick Dashboard</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --bg-primary: #0d1117;
            --bg-secondary: #161b22;
            --bg-card: #21262d;
            --border: #30363d;
            --text-primary: #e6edf3;
            --text-secondary: #8b949e;
            --accent-mlflow: #58a6ff;
            --accent-minio: #f78166;
            --glow-mlflow: rgba(88, 166, 255, 0.15);
            --glow-minio: rgba(247, 129, 102, 0.15);
        }

        body {
            font-family: 'Outfit', sans-serif;
            background: var(--bg-primary);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: var(--text-primary);
            background-image: 
                radial-gradient(ellipse at top, rgba(88, 166, 255, 0.08) 0%, transparent 50%),
                radial-gradient(ellipse at bottom right, rgba(247, 129, 102, 0.06) 0%, transparent 50%);
        }

        .container {
            text-align: center;
            padding: 2rem;
        }

        h1 {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            letter-spacing: -0.02em;
        }

        .subtitle {
            font-family: 'JetBrains Mono', monospace;
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-bottom: 3rem;
        }

        .cards {
            display: flex;
            gap: 1.5rem;
            flex-wrap: wrap;
            justify-content: center;
        }

        .card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 2rem 2.5rem;
            text-decoration: none;
            color: var(--text-primary);
            transition: all 0.2s ease;
            min-width: 220px;
            position: relative;
            overflow: hidden;
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            opacity: 0;
            transition: opacity 0.2s ease;
        }

        .card:hover {
            transform: translateY(-4px);
            border-color: transparent;
        }

        .card.mlflow::before {
            background: var(--accent-mlflow);
        }

        .card.mlflow:hover {
            box-shadow: 0 8px 32px var(--glow-mlflow), 0 0 0 1px var(--accent-mlflow);
        }

        .card.mlflow:hover::before {
            opacity: 1;
        }

        .card.minio::before {
            background: var(--accent-minio);
        }

        .card.minio:hover {
            box-shadow: 0 8px 32px var(--glow-minio), 0 0 0 1px var(--accent-minio);
        }

        .card.minio:hover::before {
            opacity: 1;
        }

        .card-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .card-title {
            font-size: 1.4rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .card-port {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8rem;
            color: var(--text-secondary);
        }

        .footer {
            margin-top: 4rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
            color: var(--text-secondary);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Podrick</h1>
        <p class="subtitle">ML Infrastructure Dashboard</p>
        
        <div class="cards">
            <a href="http://localhost:6335" target="_blank" class="card mlflow">
                <div class="card-icon">📊</div>
                <div class="card-title">MLflow</div>
                <div class="card-port">:9432</div>
            </a>
            
            <a href="http://localhost:6332" target="_blank" class="card minio">
                <div class="card-icon">🪣</div>
                <div class="card-title">Minio</div>
                <div class="card-port">:9001</div>
            </a>
            <a href="http://localhost:6338" target="_blank" class="card minio">
                <div class="card-title">Grafana</div>
            </a>
            <a href="http://localhost:6337" target="_blank" class="card minio">
                <div class="card-title">ALloy</div>
            </a>
        </div>
        
        <p class="footer">Running on port 8000</p>
    </div>
</body>
</html>
"""


@app.get("/health")
async def health():
    return {"status": "ok"}
