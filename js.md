# js search table  
```  
<!DOCTYPE html>
<html lang="en">
<head>
<title>Perform Live Search and Filter on HTML Table using jQuery </title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<!-- <script src="https://ajax.googleapis.com/libs/jquery/1.12.4/jquery.min.js"></script> -->
<script src="D:\wokroom_door\web\static\plugins\bootstrap-multiselect\bootstrap-multiselect.js"></script>
<!-- <script src=""https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script> -->
<script src="D:\wokroom_door\web\static\bootstrap\js\bootstrap-datetimepicker.js"></script>

<script>
$(document).ready(function(){
	$('.search').on('keyup',function(){
		var searchTerm = $(this).val().toLowerCase();
		$('#userTb1 tbody tr').each(function(){
			var lineStr = $(this).text().toLowerCase();
			if (lineStr.indexOf(searchTerm) === -1) {
				$(this).hide();
			} else {
				$(this).show();
			}
		});
	});
});
</script>

</head>

<body>
	<div class="container">
		<h2>Perform Live Search and Filter on HTML Table using jQuery</h2>
		<div class="form-group pull-right">
			<input type="text" class="form-controls" placeholder="What you looking for?">
		</div>
		<table class="table table-striped" id="userTb1">
			<thead>
			<tr>
				<th>Firstname</th>
				<th>Lastname</th>
				<th>Email</th>
			</tr>
			</thead>
			
			<tbody>
			<tr>
				<td>John</td>
				<td>Doe</td>
				<td>hello@153.com</td>
			</tr>
			<tr>
				<td>Johnson</td>
				<td>Youny</td>
				<td>johnson@153.com</td>
			</tr>
			<tr>
				<td>Jack</td>
				<td>Chen</td>
				<td>jack@153.com</td>
			</tr>
			<tr>
				<td>Kevin</td>
				<td>Dolly</td>
				<td>kevin@153.com</td>
			</tr>
			<tr>
				<td>July</td>
				<td>Reat</td>
				<td>july@153.com</td>
			</tr>
			</tbody>
	</div>


</body>
</html>

```
