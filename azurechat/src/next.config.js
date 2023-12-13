/** @type {import('next').NextConfig} */
const nextConfig = {
  output: "standalone",
  experimental: {
    serverActions: {
      allowedOrigins: [
        'localhost:3000',
        // ここでCodespaceのURLのOriginを指定する
        ''
      ],
    },
  },
};

module.exports = nextConfig;
