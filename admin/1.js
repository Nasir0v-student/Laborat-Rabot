async function get_calculator() {
    let response = await fetch("http://localhost:8000/api/user/all");
    if (response.ok) {
        let json = await response.json();
        return json;
    } else {
        alert("Ошибка HTTP: " + response.status);
    }
}

async function render_calculator() {
    let template = `
    <tr>
        <th scope="row">{id}</th>
        <td>{Nickname}</td>
        <td>{Email}</td>
        <td>{Password}
    </tr>`;

    let calculator = await get_calculator();
    let container = document.getElementById("calculator+");
    calculator.forEach(element => {
        let calculator = template
            .replace("{id}", element.id)
            .replace("{Nickname}", element.Nickname)
            .replace("{Email}", element.Email)
            .replace("{Password}", element.Password)
          
        container.innerHTML += calculator;
    });
}

render_calculator();