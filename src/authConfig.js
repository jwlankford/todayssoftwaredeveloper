import { PublicClientApplication } from "@azure/msal-browser";

export const msalConfig = {
  auth: {
    // Replace this with your actual Client ID (Application ID) from Azure Portal
    clientId: "b7df6696-114b-443f-87fd-c1a2c08f8ac4", 
    // Replace the tenant ID here if restricted to a single tenant, or use "common" for multi-tenant
    authority: "https://login.microsoftonline.com/e0b1877e-a0e6-450e-9469-ce23c821fda6", 
    redirectUri: window.location.origin, // Automatically redirects back to where the app is running
  },
  cache: {
    cacheLocation: "sessionStorage", // 'sessionStorage' or 'localStorage'
    storeAuthStateInCookie: false,
  }
};

export const loginRequest = {
  scopes: ["User.Read"] // Basic profile read access
};

export const msalInstance = new PublicClientApplication(msalConfig);

// Initialize the msal instance
await msalInstance.initialize();
