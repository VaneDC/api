$(document).ready(function(){
	$('#buscarProveedor').autocomplete({
		minLength: 2, 
		source: function(req, add){
			var search = $('#buscarProveedor').val();
			$.ajax({
				url:"busqueda",
				async:false,
				dataType:'json',
				type:'GET',
				data:{'start':search},
				success: function(data){
					var suggestions=[];
					$.each(data, function(index, objeto){
						suggestions.push(objeto);
					});
					add(suggestions);
				},
				error:function(err){
					alert("Error");
				}
			});
		}
		

	});
	$(".ui-helper-hidden-accessible").css({"display":"none"})

});

$(document).ready(function(){
	$('#buscarProducto').autocomplete({
		minLength: 2, 
		source: function(req, add){
			var search = $('#buscarProducto').val();
			$.ajax({
				url:"busqueda",
				async:false,
				dataType:'json',
				type:'GET',
				data:{'start':search},
				success: function(data){
					var suggestions=[];
					$.each(data, function(index, objeto){
						suggestions.push(objeto);
					});
					add(suggestions);
				},
				error:function(err){
					alert("Error");
				}
			});
		}
		

	});
	$(".ui-helper-hidden-accessible").css({"display":"none"})

});



