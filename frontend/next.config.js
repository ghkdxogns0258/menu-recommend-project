// next.config.js

const nextConfig = {
  reactStrictMode: true,
  env: {
    REACT_APP_BACKEND_URL: process.env.REACT_APP_BACKEND_URL || "http://default-url.com",
  },
};

module.exports = nextConfig;