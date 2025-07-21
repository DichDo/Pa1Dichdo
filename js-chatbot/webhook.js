// 🚀 AI SOCIAL BOT (JS Version) 🚀
// /webhook.js

const express = require('express');
const router = express.Router();
require('dotenv').config();
const { generateOpenAiReply } = require('./openai');
const { getUser, updateUser } = require('./database');
const axios = require('axios');


const VERIFY_TOKEN = process.env.VERIFY_TOKEN;
const PAGE_ACCESS_TOKEN = process.env.PAGE_ACCESS_TOKEN;

router.get('/webhook', (req, res) => {
  const mode = req.query['hub.mode'];
  const token = req.query['hub.verify_token'];
  const challenge = req.query['hub.challenge'];

  if (mode && token) {
    if (mode === 'subscribe' && token === VERIFY_TOKEN) {
      console.log('WEBHOOK_VERIFIED');
      res.status(200).send(challenge);
    } else {
      res.sendStatus(403);
    }
  }
});

router.post('/webhook', (req, res) => {
  const body = req.body;

  if (body.object === 'page') {
    body.entry.forEach(entry => {
      const webhookEvent = entry.messaging[0];
      const senderId = webhookEvent.sender.id;
      const messageText = webhookEvent.message.text;

      if (messageText) {
        getUser(senderId, async (user) => {
          const aiReply = await generateOpenAiReply(messageText);

          // In a real application, you would fetch the user's name
          // from the Graph API.
          updateUser(senderId, "User", messageText, "");

          sendFacebookReply(senderId, aiReply);
        });
      }
    });

    res.status(200).send('EVENT_RECEIVED');
  } else {
    res.sendStatus(404);
  }
});

async function sendFacebookReply(recipientId, message) {
    const url = `https://graph.facebook.com/v18.0/me/messages?access_token=${PAGE_ACCESS_TOKEN}`;
    const payload = {
        recipient: { id: recipientId },
        message: { text: message },
    };
    const headers = { 'Content-Type': 'application/json' };

    try {
        await axios.post(url, payload, { headers });
        console.log('✅ Message sent');
    } catch (error) {
        console.error('⚠️ Facebook reply error:', error);
    }
}


module.exports = router;
