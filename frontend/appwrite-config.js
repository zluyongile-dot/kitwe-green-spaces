// Appwrite Configuration for Kitwe Green Spaces
// This replaces your Flask backend completely!

const APPWRITE_CONFIG = {
    endpoint: 'https://cloud.appwrite.io/v1',
    projectId: '67a0b8b4002b8b8c8d8e', // You'll replace this with your actual project ID
    databaseId: 'kitwe_green_spaces',
    collectionId: 'green_spaces'
};

// Initialize Appwrite
const { Client, Databases, Query } = Appwrite;

const client = new Client()
    .setEndpoint(APPWRITE_CONFIG.endpoint)
    .setProject(APPWRITE_CONFIG.projectId);

const databases = new Databases(client);

// Export configuration for use in other files
window.APPWRITE_CONFIG = APPWRITE_CONFIG;
window.appwriteClient = client;
window.appwriteDatabases = databases;

console.log('🚀 Appwrite configured successfully!');