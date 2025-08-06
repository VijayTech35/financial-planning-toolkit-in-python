
const mongoose = require('mongoose');

const employeeSchema = new mongoose.Schema({
  E_id:Number,
  E_name: String,
  E_email: String,
  E_number:Number,
  E_gender: String,
  E_dept: String,
  E_location: String
});

module.exports = mongoose.model('myemployee', employeeSchema);