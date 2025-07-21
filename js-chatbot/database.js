// 🚀 AI SOCIAL BOT (JS Version) 🚀
// /database.js

const sqlite3 = require('sqlite3').verbose();
const DB_FILE = 'memory.db';

const db = new sqlite3.Database(DB_FILE, err => {
  if (err) {
    return console.error(err.message);
  }
  console.log('Connected to the in-memory SQlite database.');
});

function initDb() {
  db.run(`
    CREATE TABLE IF NOT EXISTS user_memory (
      user_id TEXT PRIMARY KEY,
      name TEXT,
      last_message TEXT,
      tags TEXT
    )
  `);
}

function getUser(userId, callback) {
  db.get(
    'SELECT name, last_message, tags FROM user_memory WHERE user_id = ?',
    [userId],
    (err, row) => {
      if (err) {
        return console.error(err.message);
      }
      callback(row);
    }
  );
}

function updateUser(userId, name, lastMessage, tags) {
  db.run(
    `
    INSERT OR REPLACE INTO user_memory (user_id, name, last_message, tags)
    VALUES (?, ?, ?, ?)
  `,
    [userId, name, lastMessage, tags]
  );
}

module.exports = { initDb, getUser, updateUser };
