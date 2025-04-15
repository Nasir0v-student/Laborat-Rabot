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
        <td>
        <button class="btn btn-danger" onclick="delete_user({id})">🗑️</button> 
        </td>
    </tr>`;

    let calculator = await get_calculator();
    let container = document.getElementById("calculator+");
    calculator.forEach(element => {
        let calculator = template
            .replaceAll("{id}", element.id)
            .replace("{Nickname}", element.Nickname)
            .replace("{Email}", element.Email)
            .replace("{Password}", element.Password)
          
        container.innerHTML += calculator;
    });
}

async function delete_user(id) {
    let response = await fetch(`http://localhost:8000/api/user/${id}`, {
        method: 'DELETE'
    });
    
    if (response.ok) {
        window.location.reload(false);
    } else {
        alert("Ошибка http: " + response.status);
    }
}

render_calculator();
