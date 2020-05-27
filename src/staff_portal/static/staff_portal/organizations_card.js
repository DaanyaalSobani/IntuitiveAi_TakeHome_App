function get_organizations(callback = console.log){
    $.ajax({
        url: "api/organizations",
        success: callback
    })
}

function populate_organizations(selector){
    get_organizations(res =>{
        res.organizations.forEach(e =>{
            $(selector).append(`
                <li class="list-group-item">${e.name}</li>
            `)
        })
    })
}