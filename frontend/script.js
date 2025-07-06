fetch("http://localhost:5000/quote")
  .then(res => res.json())
  .then(data => {
    document.getElementById("quote").textContent = data.quote;
  })
  .catch(() => {
    document.getElementById("quote").textContent = "Error fetching quote.";
  });
