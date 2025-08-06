const express = require('express');
const mongoose = require('mongoose');
const employee = require('./models/Employee');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));
app.set('view engine', 'pug');
app.set('views', path.join(__dirname, 'views'));

// DB Connection
mongoose.connect('mongodb://localhost:27017/Employee', {
  //useNewUrlParser: true,
  //useUnifiedTopology: true
}).then(() => console.log('✅ MongoDB Connected'))
  .catch(err => console.log('❌ Connection Failed:', err));

// Routes
app.get('/', async (req, res) => {
  const myemployee = await employee.find();
  res.render('index', { myemployee});
});

app.get('/new', (req, res) => {
  res.render('new');
});

app.post('/create', async (req, res) => {
  await employee.create(req.body);
  res.redirect('/');
});

app.get('/edit/:id', async (req, res) => {
  const myemployee = await employee.findById(req.params.id);
  res.render('edit', { employee :myemployee});
});

app.post('/update/:id', async (req, res) => {
  await employee.findByIdAndUpdate(req.params.id, req.body);
  res.redirect('/');
});

app.get('/delete/:id', async (req, res) => {
  await employee.findByIdAndDelete(req.params.id);
  res.redirect('/');
});

// Start server
app.listen(PORT, () => console.log(`🚀 Server running at http://localhost:${PORT}`));
