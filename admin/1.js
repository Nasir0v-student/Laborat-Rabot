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
    let template = `<tr>
                        <th scope="row">{id}</th>
                        <td>{Nickname}</td>
                        <td>{Email}</td>
                        <td>{Password}</td>
                        <td>
                            <button class="btn btn-danger" onclick="delete_user({id})">🗑️</button>
                            <button class="btn btn-warning" onclick="edit_user({id})">✏️</button>
                        </td>
                    </tr>`;

    let calculator = await get_calculator();

    let container = document.getElementById("calculator+");

    calculator.forEach(element => {
        let row = template
            .replace(/{id}/g, element.id)
            .replace(/{Nickname}/g, element.Nickname)
            .replace(/{Email}/g, element.Email)
            .replace(/{Password}/g, element.Password);

        container.innerHTML += row;
    });
}


function edit_user(id) {
    window.location.href = `forms.html?id=${id}`;
}



async function delete_user(id) {
    let response = await fetch(`http://localhost:8000/api/user/${id}`, {
        method: 'DELETE'
    });
    if (response.ok) {
        window.location.reload(false);
    } else {
        alert("Ошибка HTTP: " + response.status);
    }
}

render_calculator();
