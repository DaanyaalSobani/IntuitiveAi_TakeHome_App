function itemCard(selector,itemCount = 0, color = "red"){
    $(selector).css({
        "width": "140px",
        "height": "140px",
        "border-radius":"50%",
        "border": `solid 4px ${color}`,
        "box-shadow": "0px 0px 5px 1px rgba(0,0,0,0.75)",
        "padding-top": "42px",
        "text-align": "center"
    })
    $(selector).html(`${itemCount}<br>Items`)
}

function get_trash(callback = console.log){
    $.ajax({
        url: "api/trash",
        success: callback
    })
}