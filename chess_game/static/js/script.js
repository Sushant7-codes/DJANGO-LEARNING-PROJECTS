function sendMove(move) {
    fetch('/move/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ move: move })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "ok") {
            console.log("Move successful, board state:", data.fen);
            // Optionally update board UI
        } else {
            alert("Illegal move");
        }
    });
}
