// 🚀 AI SOCIAL BOT (JS Version) 🚀
// /index.js

const express = require('express');
const bodyParser = require('body-parser');
const webhookRouter = require('./webhook');

const app = express();
app.use(bodyParser.json());

app.use('/', webhookRouter);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
