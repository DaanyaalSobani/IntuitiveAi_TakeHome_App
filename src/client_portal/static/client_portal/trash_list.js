function trash_list(list_container, list) {
	var list_group = $(
		`<ul class="trash-group list-group align-self-stretch" style='flex-grow:1'></ul>`
	).appendTo(list_container);
	$('.list-group').sortable({
		revert: true,
	});
	$('ul, li').disableSelection();
	list.forEach((item) => {
		list_group.append(
			$(
				`<li id='trash_item_${item.id}' class="list-group-item d-flex flex-row justify-content-start"></li>`
			)
				.css({
					height: '50px',
					padding: '0px',
				})
				.append(
					$(`<div class='flex-fill'></div>`).css({
						background: 'black',
						'max-width': '30%',
					})
				)
				.append(
					$(`<div class='flex-fill align-self-center'>${item.name}</div>`).css({
						'max-width': '70%',
					})
				)
				.draggable({
					connectToSortable: '.list-group',
					revert: 'invalid',
				})
				.data('trash_data', item)
		);
	});
}

function update_trash_state_client(state) {
	$('.trash-group').each((e, i) => {
		console.log(e, i);
	});
}
