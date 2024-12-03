document.getElementById("quizForm").addEventListener("submit", async (event) => {
    event.preventDefault(); // Prevent default form submission

    const formData = {
        age: document.getElementById("age").value,
        fitness: document.getElementById("fitness").value,
        type: document.getElementById("type").value,
        time: document.getElementById("time").value,
    };

    try {
        const response = await fetch("/recommend", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(formData),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();

        document.getElementById("recommendation").innerHTML = `
            <h2>We recommend: ${data.sport}</h2>
            <p>${data.description}</p>
        `;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("recommendation").innerHTML = `
            <p style="color: red;">Failed to get a recommendation. Please try again!</p>
        `;
    }
});
