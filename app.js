function toggleDarkMode() {
  document.body.classList.toggle("dark-mode");
}

let history = [];

function simulateSignal() {
  const signal = Math.random() > 0.5 ? "BUY" : "SELL";
  const confidence = Math.floor(Math.random() * 50 + 50);
  const sl = (Math.random() * 0.005).toFixed(4);
  const tp = (Math.random() * 0.010).toFixed(4);

  document.getElementById("signal").innerText = signal;
  document.getElementById("confidence").innerText = confidence + "%";
  document.getElementById("sl").innerText = sl;
  document.getElementById("tp").innerText = tp;

  const entry = `${new Date().toLocaleTimeString()} ‑ ${signal} | Conf: ${confidence}% | SL: ${sl} | TP: ${tp}`;
  history.unshift(entry);
  if (history.length > 10) history.pop();

  const list = document.getElementById("history");
  list.innerHTML = "";
  history.forEach(h => { const li = document.createElement("li"); li.innerText = h; list.appendChild(li); });

  console.log("📲 Telegram placeholder:", entry);
}

function saveNote() {
  const notes = document.getElementById("notes").value;
  if (notes) {
    const div = document.getElementById("saved-notes");
    const p = document.createElement("p");
    p.innerText = `📝 [${new Date().toLocaleTimeString()}] ${notes}`;
    div.prepend(p);
    document.getElementById("notes").value = "";
  }
}

setInterval(simulateSignal, 4000);
simulateSignal();
