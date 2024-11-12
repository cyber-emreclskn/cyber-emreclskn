<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emre Caliskan - Developer Profile</title>
    <style>
        :root {
            --bg-primary: #0d1117;
            --bg-secondary: #161b22;
            --text-primary: #c9d1d9;
            --text-secondary: #8b949e;
            --accent: #7928ca;
            --border: #30363d;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .header {
            text-align: center;
            margin-bottom: 3rem;
            position: relative;
            overflow: hidden;
        }

        .profile-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(45deg, #1a1a1a, #2d1a4a);
            opacity: 0.8;
            z-index: -1;
        }

        .profile-content {
            padding: 2rem;
            background: var(--bg-secondary);
            border-radius: 1rem;
            border: 1px solid var(--border);
            margin-bottom: 2rem;
        }

        .title {
            font-size: 2.5rem;
            color: var(--accent);
            margin-bottom: 1rem;
            text-shadow: 0 0 10px rgba(121, 40, 202, 0.3);
        }

        .subtitle {
            font-size: 1.2rem;
            color: var(--text-secondary);
            margin-bottom: 2rem;
        }

        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            margin: 2rem 0;
        }

        .tech-item {
            background: var(--bg-primary);
            padding: 0.5rem 1rem;
            border-radius: 2rem;
            border: 1px solid var(--border);
            transition: all 0.3s ease;
        }

        .tech-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            border-color: var(--accent);
        }

        .gaming-section {
            background: var(--bg-secondary);
            padding: 2rem;
            border-radius: 1rem;
            border: 1px solid var(--border);
            margin-top: 2rem;
        }

        .gaming-title {
            color: var(--accent);
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .social-links {
            display: flex;
            gap: 1rem;
            justify-content: center;
            margin-top: 2rem;
        }

        .social-link {
            color: var(--text-primary);
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            transition: all 0.3s ease;
        }

        .social-link:hover {
            background: var(--accent);
            color: white;
        }

        .souls-gif {
            width: 100%;
            max-width: 600px;
            border-radius: 0.5rem;
            margin: 1rem auto;
            display: block;
        }

        @keyframes glow {
            0% { box-shadow: 0 0 5px var(--accent); }
            50% { box-shadow: 0 0 20px var(--accent); }
            100% { box-shadow: 0 0 5px var(--accent); }
        }

        .glow-effect {
            animation: glow 3s infinite;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="profile-bg"></div>
            <h1 class="title glow-effect">Emre Caliskan</h1>
            <p class="subtitle">Python Developer | AWS Engineer | Gaming Enthusiast</p>
        </div>

        <div class="profile-content">
            <p>🚀 Computer Engineer specializing in Python/Django development and AWS cloud solutions</p>
            <p>🌟 Passionate about creating scalable web applications and solving complex problems</p>
            
            <div class="tech-stack">
                <span class="tech-item">Python</span>
                <span class="tech-item">Django</span>
                <span class="tech-item">AWS</span>
                <span class="tech-item">AI</span>
                <span class="tech-item">Java</span>
                <span class="tech-item">React</span>
                <span class="tech-item">Flutter</span>
                <span class="tech-item">HTML/CSS</span>
                <span class="tech-item">Network Engineering</span>
            </div>
        </div>

        <div class="gaming-section">
            <h2 class="gaming-title">Gaming Passion</h2>
            <p>Souls-like gaming enthusiast. When not coding, you'll find me exploring the challenging worlds of Dark Souls, Bloodborne, and Elden Ring.</p>
            <img src="/api/placeholder/600/300" alt="Souls-like gaming gif" class="souls-gif">
        </div>

        <div class="social-links">
            <a href="https://github.com/cyber-emreclskn" class="social-link">GitHub</a>
            <a href="https://open.spotify.com/user/21wydn2a4th25wi7o43bi25ii?si=f788a69a29cf47f3" class="social-link">Spotify</a>
        </div>
    </div>
</body>
</html>
