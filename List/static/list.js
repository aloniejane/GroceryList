function on()
{
    var select = document.getElementById('itm');
    var input = document.getElementById('item');
    select.onchange = function() {
        input.value = select.value;
    }
}