fetch('http://127.0.0.1:8787/api/articles')
  .then(res => { console.log("STATUS:", res.status); return res.text(); })
  .then(text => console.log("BODY:", text.substring(0, 100)))
  .catch(err => console.error("ERROR:", err.message));