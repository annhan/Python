/**
 * Created by Admin on 5/10/2017.
 */
$(document).ready( function(){
$('#auto').load('index.html');
refresh();
});

function refresh()
{
	setTimeout( function() {
	  $('#auto').fadeOut('slow').load('index.html').fadeIn('slow');
	  refresh();
	}, 2000);
}