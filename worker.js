import { CosmosClient } from '@azure/cosmos';

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    console.log("HIT Worker!", request.method, request.url);

    // Add CORS headers so your Vue app can call this API
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*', // Update this to your real frontend URL in production
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    // Handle CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: corsHeaders });
    }

    try {
      // Helper function to setup Cosmos so it only runs when needed
      const getCosmosContainer = () => {
        if (!env.COSMOS_CONNECTION_STRING) {
          throw new Error("COSMOS_CONNECTION_STRING is not set in environment variables.");
        }
        const endpointMatch = env.COSMOS_CONNECTION_STRING.match(/AccountEndpoint=([^;]+)/);
        const keyMatch = env.COSMOS_CONNECTION_STRING.match(/AccountKey=([^;]+)/);
        
        if (!endpointMatch || !keyMatch) {
           throw new Error("Invalid connection string in environment variables.");
        }
        const endpoint = endpointMatch[1];
        const key = keyMatch[1];
        const client = new CosmosClient({ endpoint, key });
        return client.database('ArticleDB').container('Articles');
      };

      // GET /api/articles - Fetch all articles
      if (request.method === 'GET' && url.pathname.endsWith('/api/articles')) {
        const container = getCosmosContainer();
        const { resources } = await container.items
          .query('SELECT * from c ORDER BY c._ts DESC')
          .fetchAll();

        return new Response(JSON.stringify(resources), {
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
          status: 200
        });
      }

      // POST /api/articles - Create a new article
      if (request.method === 'POST' && url.pathname.endsWith('/api/articles')) {
        const container = getCosmosContainer();
        const body = await request.json();
        
        // Ensure ID exists for Cosmos
        const newArticle = {
          id: body.id || crypto.randomUUID(),
          title: body.title,
          content: body.content,
          author: body.author || "Jeremy Lankford",
          authorPhoto: body.authorPhoto || null,
          createdAt: body.createdAt || new Date().toISOString(),
          imageUrl: body.imageUrl || null
        };

        const { resource } = await container.items.create(newArticle);

        return new Response(JSON.stringify(resource), {
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
          status: 201
        });
      }

      // POST /api/generate - Generate article content with Cloudflare AI
      if (request.method === 'POST' && url.pathname.endsWith('/api/generate')) {
        const { title, description } = await request.json();
        
        if (!env.AI) {
           throw new Error("Cloudflare AI binding (env.AI) is missing or not configured correctly.");
        }

        const prompt = `Write a comprehensive, compelling, and brand-new tech blog post based on the provided research context. You must act as an expert technology analyst. Write a completely original article discussing the broader implications, real-world applications, and future of the concepts presented. DO NOT just summarize the abstract. DO NOT use the original research title verbatim.

Original Topic: ${title}
Context/Abstract: ${description}

Format the output strictly as beautifully structured semantic HTML, suitable for embedding directly in a Vue.js v-html block. 
CRITICAL: The very first line of your output MUST be an <h1> tag containing your brand-new, catchy, generated blog title. Do not use Markdown. Use <h1>, <h2>, <h3>, <p>, <ul>, <li>. Ensure the HTML is properly indented and formatted for readability in a code editor.`;

        const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
          messages: [
            { role: "system", content: "You are an expert software developer and technical writer. Provide concise but high-quality articles." },
            { role: "user", content: prompt }
          ],
          max_tokens: 800
        });

        return new Response(JSON.stringify({ content: response.response }), {
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
          status: 200
        });
      }

      // GET /api/articles/:id - Fetch single article
      const articleIdMatch = url.pathname.match(/\/api\/articles\/([^\/]+)$/);
      if (request.method === 'GET' && articleIdMatch) {
         const id = articleIdMatch[1];
         const container = getCosmosContainer();
         // Using Cosmos DB point read or query. Point read requires partition key, 
         // so let's query by id if partition key is not identical to id.
         const { resources } = await container.items
           .query({
             query: 'SELECT * from c WHERE c.id = @id',
             parameters: [{ name: '@id', value: id }]
           })
           .fetchAll();

         if (resources.length === 0) {
            return new Response('Not Found', { status: 404, headers: corsHeaders });
         }

         return new Response(JSON.stringify(resources[0]), {
           headers: { ...corsHeaders, 'Content-Type': 'application/json' },
           status: 200
         });
      }

      // 404 for any other route
      return new Response('Not Found', { status: 404, headers: corsHeaders });
      
    } catch (error) {
      return new Response(JSON.stringify({ error: error.message }), {
        status: 500,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }
  },
};
