#!/usr/bin/env python3
"""
Initialize a React + Shadcn/ui prototype project.

Usage:
    python init_prototype.py <project-name> [--template base|dashboard|form]
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def create_package_json(project_path: Path, project_name: str) -> None:
    """Create package.json with required dependencies."""
    package_json = {
        "name": project_name,
        "private": True,
        "version": "0.0.0",
        "type": "module",
        "scripts": {
            "dev": "vite",
            "build": "tsc && vite build",
            "preview": "vite preview"
        },
        "dependencies": {
            "react": "^18.3.1",
            "react-dom": "^18.3.1",
            "class-variance-authority": "^0.7.0",
            "clsx": "^2.1.1",
            "lucide-react": "^0.462.0",
            "tailwind-merge": "^2.5.4"
        },
        "devDependencies": {
            "@types/react": "^18.3.12",
            "@types/react-dom": "^18.3.1",
            "@vitejs/plugin-react": "^4.3.4",
            "autoprefixer": "^10.4.20",
            "postcss": "^8.4.49",
            "tailwindcss": "^3.4.17",
            "typescript": "~5.6.2",
            "vite": "^6.0.1"
        }
    }

    with open(project_path / "package.json", "w") as f:
        json.dump(package_json, f, indent=2)


def create_vite_config(project_path: Path) -> None:
    """Create vite.config.ts."""
    config = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
})
"""
    with open(project_path / "vite.config.ts", "w") as f:
        f.write(config)


def create_tsconfig(project_path: Path) -> None:
    """Create tsconfig.json."""
    config = {
        "compilerOptions": {
            "target": "ES2020",
            "useDefineForClassFields": True,
            "lib": ["ES2020", "DOM", "DOM.Iterable"],
            "module": "ESNext",
            "skipLibCheck": True,
            "moduleResolution": "bundler",
            "allowImportingTsExtensions": True,
            "resolveJsonModule": True,
            "isolatedModules": True,
            "noEmit": True,
            "jsx": "react-jsx",
            "strict": True,
            "noUnusedLocals": True,
            "noUnusedParameters": True,
            "noFallthroughCasesInSwitch": True,
            "baseUrl": ".",
            "paths": {
                "@/*": ["./src/*"]
            }
        },
        "include": ["src"],
        "references": [{"path": "./tsconfig.node.json"}]
    }

    with open(project_path / "tsconfig.json", "w") as f:
        json.dump(config, f, indent=2)


def create_tsconfig_node(project_path: Path) -> None:
    """Create tsconfig.node.json."""
    config = {
        "compilerOptions": {
            "composite": True,
            "skipLibCheck": True,
            "module": "ESNext",
            "moduleResolution": "bundler",
            "allowSyntheticDefaultImports": True
        },
        "include": ["vite.config.ts"]
    }

    with open(project_path / "tsconfig.node.json", "w") as f:
        json.dump(config, f, indent=2)


def create_tailwind_config(project_path: Path) -> None:
    """Create tailwind.config.js."""
    config = """/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  content: [
    './pages/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    './app/**/*.{ts,tsx}',
    './src/**/*.{ts,tsx}',
  ],
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      keyframes: {
        "accordion-down": {
          from: { height: 0 },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: 0 },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}
"""
    with open(project_path / "tailwind.config.js", "w") as f:
        f.write(config)


def create_postcss_config(project_path: Path) -> None:
    """Create postcss.config.js."""
    config = """module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
"""
    with open(project_path / "postcss.config.js", "w") as f:
        f.write(config)


def create_components_json(project_path: Path) -> None:
    """Create components.json for Shadcn."""
    config = {
        "$schema": "https://ui.shadcn.com/schema.json",
        "style": "default",
        "rsc": False,
        "tsx": True,
        "tailwind": {
            "config": "tailwind.config.js",
            "css": "src/index.css",
            "baseColor": "slate",
            "cssVariables": True
        },
        "aliases": {
            "components": "@/components",
            "utils": "@/lib/utils"
        }
    }

    with open(project_path / "components.json", "w") as f:
        json.dump(config, f, indent=2)


def create_src_files(project_path: Path) -> None:
    """Create src directory with basic files."""
    src = project_path / "src"
    src.mkdir(exist_ok=True)

    # Create lib/utils.ts
    lib = src / "lib"
    lib.mkdir(exist_ok=True)
    with open(lib / "utils.ts", "w") as f:
        f.write("""import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
""")

    # Create components directory
    components = src / "components"
    components.mkdir(exist_ok=True)

    # Create index.css
    with open(src / "index.css", "w") as f:
        f.write("""@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --card: 0 0% 100%;
    --card-foreground: 222.2 84% 4.9%;
    --popover: 0 0% 100%;
    --popover-foreground: 222.2 84% 4.9%;
    --primary: 222.2 47.4% 11.2%;
    --primary-foreground: 210 40% 98%;
    --secondary: 210 40% 96.1%;
    --secondary-foreground: 222.2 47.4% 11.2%;
    --muted: 210 40% 96.1%;
    --muted-foreground: 215.4 16.3% 46.9%;
    --accent: 210 40% 96.1%;
    --accent-foreground: 222.2 47.4% 11.2%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 40% 98%;
    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: 222.2 84% 4.9%;
    --radius: 0.5rem;
  }

  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    --card: 222.2 84% 4.9%;
    --card-foreground: 210 40% 98%;
    --popover: 222.2 84% 4.9%;
    --popover-foreground: 210 40% 98%;
    --primary: 210 40% 98%;
    --primary-foreground: 222.2 47.4% 11.2%;
    --secondary: 217.2 32.6% 17.5%;
    --secondary-foreground: 210 40% 98%;
    --muted: 217.2 32.6% 17.5%;
    --muted-foreground: 215 20.2% 65.1%;
    --accent: 217.2 32.6% 17.5%;
    --accent-foreground: 210 40% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 210 40% 98%;
    --border: 217.2 32.6% 17.5%;
    --input: 217.2 32.6% 17.5%;
    --ring: 212.7 26.8% 83.9%;
  }
}

@layer base {
  * {
    @apply border-border;
  }
  body {
    @apply bg-background text-foreground;
  }
}
""")

    # Create App.tsx
    with open(src / "App.tsx", "w") as f:
        f.write("""function App() {
  return (
    <div className="min-h-screen bg-background p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold mb-4">Prototype</h1>
        <p className="text-muted-foreground">
          Start building your prototype here.
        </p>
      </div>
    </div>
  )
}

export default App
""")

    # Create main.tsx
    with open(src / "main.tsx", "w") as f:
        f.write("""import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
""")

    # Create vite-env.d.ts
    with open(src / "vite-env.d.ts", "w") as f:
        f.write("""/// <reference types="vite/client" />
""")


def create_html(project_path: Path, project_name: str) -> None:
    """Create index.html."""
    html = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{project_name}</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
"""
    with open(project_path / "index.html", "w") as f:
        f.write(html)


def create_readme(project_path: Path, project_name: str) -> None:
    """Create README.md."""
    readme = f"""# {project_name}

A prototype built with React, TypeScript, Vite, and Shadcn/ui.

## Setup

Install dependencies:

```bash
npm install
```

## Development

Run the development server:

```bash
npm run dev
```

## Adding Shadcn Components

Install components as needed:

```bash
npx shadcn@latest add button
npx shadcn@latest add card
npx shadcn@latest add input
# etc.
```

See available components: https://ui.shadcn.com/docs/components

## Build

Build for production:

```bash
npm run build
```

Preview production build:

```bash
npm run preview
```

## Technologies

- React 18
- TypeScript
- Vite
- Tailwind CSS
- Shadcn/ui
"""
    with open(project_path / "README.md", "w") as f:
        f.write(readme)


def create_gitignore(project_path: Path) -> None:
    """Create .gitignore."""
    gitignore = """# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?
"""
    with open(project_path / ".gitignore", "w") as f:
        f.write(gitignore)


def init_project(project_name: str, template: str = "base") -> None:
    """Initialize a new prototype project."""
    project_path = Path.cwd() / project_name

    if project_path.exists():
        print(f"❌ Error: Directory '{project_name}' already exists")
        sys.exit(1)

    print(f"🚀 Creating prototype: {project_name}")
    print(f"📁 Location: {project_path}")

    # Create project directory
    project_path.mkdir(parents=True)

    # Create all config files
    print("📝 Creating configuration files...")
    create_package_json(project_path, project_name)
    create_vite_config(project_path)
    create_tsconfig(project_path)
    create_tsconfig_node(project_path)
    create_tailwind_config(project_path)
    create_postcss_config(project_path)
    create_components_json(project_path)
    create_gitignore(project_path)

    # Create source files
    print("📦 Creating source files...")
    create_src_files(project_path)
    create_html(project_path, project_name)

    # Create README
    print("📄 Creating README...")
    create_readme(project_path, project_name)

    print(f"\n✅ Prototype '{project_name}' created successfully!")
    print(f"\nNext steps:")
    print(f"  cd {project_name}")
    print(f"  npm install")
    print(f"  npm run dev")
    print(f"\nAdd Shadcn components:")
    print(f"  npx shadcn@latest add button")
    print(f"  npx shadcn@latest add card")
    print(f"  npx shadcn@latest add input")


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a React + Shadcn/ui prototype project"
    )
    parser.add_argument(
        "project_name",
        help="Name of the prototype project"
    )
    parser.add_argument(
        "--template",
        choices=["base", "dashboard", "form"],
        default="base",
        help="Template to use (default: base)"
    )

    args = parser.parse_args()
    init_project(args.project_name, args.template)


if __name__ == "__main__":
    main()
