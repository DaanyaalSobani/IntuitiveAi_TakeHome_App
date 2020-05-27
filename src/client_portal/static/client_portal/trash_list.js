function trash_list(list_container, list, preference) {
	var list_group = $(
		`<ul id='trash_group_${preference}' class="trash-group list-group align-self-stretch" style='flex-grow:1'></ul>`
	).appendTo(list_container);
	$('.trash-group').sortable({
		revert: true,
		out: function (event, ui) {
			update_trash_state_client();
		},
		over: function (event, ui) {
			update_trash_state_client();
		},
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

function update_trash_state_client() {
	$('.trash-group').each((i, parent) => {
		var preference = $(parent).attr('id').replace('trash_group_', '');
		state[preference].length = 0;
		$(parent)
			.children()
			.each((i, child) => {
				data = $(child).data()?.trash_data;
				if (data) {
					data.type = type_name_to_code(preference);
					state[preference].push(data);
				}
			});
	});
	trash_state_updated();
}
