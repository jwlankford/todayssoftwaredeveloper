# Today's Software Developer (Jeremy Lankford's Portfolio)

Welcome to the source code repository for **[jeremylankford.com](https://jeremylankford.com)** (also accessible via [todayssoftwaredeveloper.com](https://todayssoftwaredeveloper.com)). 

This digital platform is a modern, high-performance web application designed for publishing thoughts, tutorials, and deep dives into software architecture, AI education, and IT leadership. It serves as Jeremy Lankford's personal platform and technical blog.

## 🌊 100% Vibe Coded
This entire project—from the sleek UI to the complex enterprise cloud integrations—was **100% Vibe Coded**. Through the pure power of AI-assisted engineering, this application was forged using natural language, rapid iteration, and a seamless flow of intent from human thought straight into production-ready code.

## 🏗️ What It's Built On
This application is powered by a lightning-fast modern frontend stack mapped to edge-network APIs and enterprise database platforms:

### Core Tech Stack
* **Frontend Framework**: [Vue 3](https://vuejs.org/) (Composition API & Vue Router)
* **Build Tool**: [Vite](https://vitejs.dev/)
* **Styling**: [Tailwind CSS](https://tailwindcss.com/)
* **Backend API & Edge Hosting**: [Cloudflare Workers](https://workers.cloudflare.com/) (configured via Wrangler)

### Backend & Cloud Services
* **AI Integration**: Cloudflare AI Binding (`@cf/meta/llama-3-8b-instruct`) for dynamic article generation. 
* **Database**: Azure Cosmos DB (NoSQL Document Store)
* **Authentication**: Microsoft Entra ID (Azure Active Directory SSO via `@azure/msal-browser`)
* **User Profiles**: Microsoft Graph API with [Gravatar](https://gravatar.com) fallbacks.
* **Data Processing & Scraping**: Python scripts using `BeautifulSoup4` and `Pandas` for local data acquisition and processing pipelines.

## 🚀 Getting Started

### Prerequisites
* Node.js (v18+)
* An Azure Entra ID Application configuration (for local SSO testing)
* An Azure Cosmos DB Connection String 
* Cloudflare Wrangler CLI

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jwlankford/todayssoftwaredeveloper.git
   cd todayssoftwaredeveloper
   ```

2. Install the necessary dependencies (this includes Vite, Vue, and the Wrangler tooling):
   ```bash
   npm install
   ```

3. **Configure Environment Variables**:
   Create a `.dev.vars` file in the root of the project to hold your secure database keys so the local Cloudflare Worker can connect:
   ```plaintext
   COSMOS_CONNECTION_STRING="AccountEndpoint=https://<YOUR_DB>.documents.azure.com:443/;AccountKey=<YOUR_DB_SECRET_KEY>"
   ```

4. **Spin up the Development Environment**:
   Starting the development server runs both the Vue frontend on port `5173` and the Cloudflare API Worker on port `8787` simultaneously using `concurrently`:
   ```bash
   npm run dev
   ```

### 🚢 Deployment
Deploying to production on Cloudflare is a breeze. Pushing to the `main` branch connects with CI/CD, or you can deploy locally with:
```bash
npm run deploy
```
*Note: Make sure your live Cloudflare Dashboard has the `COSMOS_CONNECTION_STRING` variable securely added as an encrypted secret under Settings > Variables and Secrets!*
