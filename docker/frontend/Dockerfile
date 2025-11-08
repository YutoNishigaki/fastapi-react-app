FROM node:22-slim

WORKDIR /app

COPY frontend/package*.json ./
RUN npm install

COPY frontend .

# RUN npm run dev だとフォアグラウンドプロセスでビルドが終わらないため、CMDで実行する
CMD ["npm", "run", "dev"]
