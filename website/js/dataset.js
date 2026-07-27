async function loadDataset() {

    const response = await fetch("../data/f1_2021_2025.csv");
 

    const csvText = await response.text();

    const rows = csvText.split("\n").slice(1);

    const tableBody = document.querySelector("#datasetTable tbody");

    rows.forEach(row => {

        const cols = row.split(",");

        if (cols.length > 5) {

            const tr = document.createElement("tr");

            tr.innerHTML = `

                <td>${cols[0]}</td>
                <td>${cols[1]}</td>
                <td>${cols[2]}</td>
                <td>${cols[3]}</td>
                <td>${cols[5]}</td>

            `;

            tableBody.appendChild(tr);

        }

    });

}

loadDataset();


// SEARCH FILTER

const searchInput = document.getElementById("searchInput");

searchInput.addEventListener("keyup", function () {

    let filter = searchInput.value.toLowerCase();

    let rows = document.querySelectorAll("#datasetTable tbody tr");

    rows.forEach(row => {

        let text = row.textContent.toLowerCase();

        row.style.display =
            text.includes(filter)
            ? ""
            : "none";

    });

});