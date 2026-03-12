# Today's Software Developer

Welcome to the source code repository for **Today's Software Developer**. This digital platform serves as a modern web application for publishing articles, showcasing AI tools, and providing top-tier developer resources.

## 🌊 100% Vibe Coded
This entire project—from the responsive layout to the complex enterprise cloud integrations—was **100% Vibe Coded**. Through the pure power of AI-assisted engineering, this application was forged using natural language, rapid iteration, and a seamless flow of intent moving from human thought straight into production-ready code. No manual typing, just pure vibes.

## 🏗️ What It's Built On
This application is powered by a lightning-fast modern frontend stack backed by enterprise-grade cloud services:

### Core Tech Stack
* **Frontend Framework**: [Vue 3](https://vuejs.org/) (Composition API & Vue Router)
* **Build Tool**: [Vite](https://vitejs.dev/)
* **Styling**: [Tailwind CSS](https://tailwindcss.com/)
* **Deployment & Edge**: Cloudflare Workers & Pages (configured via Wrangler)

### Backend & Cloud Services
* **Authentication**: Microsoft Entra ID (Azure Active Directory SSO via `@azure/msal-browser`)
* **Database**: Azure Cosmos DB (NoSQL Document Store)
* **User Profiles**: Microsoft Graph API with [Gravatar](https://gravatar.com) fallbacks (via `md5`)

## 🚀 Getting Started

### Prerequisites
* Node.js (v18+)
* An Azure Entra ID Application configuration (for local SSO testing)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jwlankford/todayssoftwaredeveloper.git
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Spin up the Vite development server:
   ```bash
   npm run dev
   ```

### Building for Production
To bundle the application for production deployment:
```bash
npm run build
```
This leverages Vite to aggressively minify the payload and output static assets ready to be served by Cloudflare Pages.
