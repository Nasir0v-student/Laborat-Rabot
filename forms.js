async function get_product(id) {
    let response = await fetch("http://localhost:8000/api/user/" + id)
    if (response.ok) {
        let json = await response.json()
        return json
    } else {
        alert("Ошибка HTTP: " + response.status)
    }
}

async function update_form(){
    let params = new URLSearchParams(document.location.search)
    let id = params.get("id")
    if (id == null){
        document.getElementById("_button").innerText = "Добавить"
        document.getElementById("_button").onclick = add_user
        return
    }
    document.getElementById("_button").innerText = "Редактировать"
    document.getElementById("_button").onclick = edit_user
    let product = await get_product(id)
    document.getElementById("Nickname").value = user["Nickame"]
    document.getElementById("Email").value = user["Email"]
    document.getElementById("Password").value = user["Password"]
}

async function edit_user() {
    let params = new URLSearchParams(document.location.search)
    let id = params.get("id")
    let response = await fetch("http://localhost:8000/api/user/" + id, {
        method: "PUT",
        body: new FormData(document.getElementById("form"))
    })
    if (response.ok) {
        window.location = "./"
    } else {
        alert("Ошибка HTTP: " + response.status)
    }
}

async function add_user() {
    let response = await fetch("http://localhost:8000/api/user", {
        method: "POST",
        body: new FormData(document.getElementById("form"))
    })
    if (response.ok) {
        window.location = "./"
    } else {
        alert("Ошибка HTTP: " + response.status)
    }
}

update_form()