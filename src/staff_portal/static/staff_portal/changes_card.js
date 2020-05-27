function get_change_requests(callback = console.log){
    $.ajax({
        url:'api/pending_changes',
        success: callback
    })
}
function format_change_request(change_request){
    change_request_JSON = JSON.parse(change_request.change_request_JSON)
    result = `${change_request.wastemanager} from ${change_request.organization} wants to: `
    change_request_JSON.forEach(request=>{
        result = result + `move ${request.name} to type ${request.type}`
    })

    return result
}
function populate_change_requests(selector){
    get_change_requests((res)=>{
        res['change_requests'].forEach((organization)=>{
            organization.forEach(request =>{
                $(selector).append(`
                <li class="list-group-item">
                    ${format_change_request(request)}
                    <div class='btn btn-primary'>Approve</div>
                    <div class='btn btn-danger'>Delete</div>
                </li>
                `)
            })
        })
    })
}