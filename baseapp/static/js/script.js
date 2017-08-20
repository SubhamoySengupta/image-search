$(document).ready(function($) {
	var options = {
		url: "/static/data/list.json",
		getValue: "name",
		placeholder: "Search for images",
		/*template: {
			type: "iconRight",
			fields: {iconSrc:'link'}
		},*/
		list: {
			onClickEvent: function() {
				var value = $("#search-bar").getSelectedItemData().link;
				value = value.replace('thumbnails', 'original');
				$("#img-div").css('background-image', 'url('+ value +')');
				console.log($("#search-bar").getSelectedItemData().name);
				runMatcher($("#search-bar").getSelectedItemData().name);
			},

			onSelectItemEvent: function() {
				var value = $("#search-bar").getSelectedItemData().link;
				value = value.replace('thumbnails', 'original');
				$("#img-div").css('background-image', 'url('+ value +')');
			},
			showAnimation: {
				type: "fade", //normal|slide|fade
				time: 400,
				callback: function() {}
			},
			match: {
				enabled: true
			},
			maxNumberOfElements: 4
		}
	};	
	$("#search-bar").easyAutocomplete(options);
});



var runMatcher = function (name) {
	$.ajax({
		url: 'get-matches/',
		type: 'GET',
		data: {name: name},
	})
	.done(function(data) {
		console.log(data);
		var matcher = data['matcher'];
		var color = data['color'];
		var t = data['time'];

		var str = ''
		for (var i=0;i<matcher.length;i++){
			str += '<div class="s-images"';
			str += 'style="background-image:url(\'http://0.0.0.0:8000/static/original/';
			str += matcher[i]['name'] + '\')"></div>';
		}

		var cp = color[0][0];
		var cs = color[0][1];
		var color_p = 'rgb(' + cp[0].toString() + ',' + cp[1].toString() +','+cp[2].toString() +')';  
		var color_s = 'rgb(' + cs[0].toString() + ',' + cs[1].toString() +','+cs[2].toString() +')';  
		
		pc_p = color[1][0];
		pc_s = color[1][1];

		$(".bar .p").css('background-color', color_p);
		$(".bar .s").css('background-color', color_s);	
		$(".bar .p").css('width', parseInt(pc_p * 100).toString() + '%');
		$(".bar .s").css('width', parseInt(pc_s * 100).toString() + '%');
		$(".bar .p").html(parseInt(pc_p * 100).toString());
		$(".bar .s").html(parseInt(pc_s * 100).toString());
		$('.time .t').html(parseFloat(t).toFixed(2) + ' secs');
		$('.similars').html(str);
		$('#di').css('visibility', 'visible');
	})
	.fail(function() {
		console.log("error");
	})
	.always(function(data) {
		console.log(data);
	});
}