const fs = require('fs');

fs.readFile('./wordsearch.txt','utf-8', (err, data) => {
  if (err) throw err;

//   console.log(data.toString());
//   let d=data.toString();  
  let inputdata=data.split(`\n`);
  console.log(inputdata)


});


