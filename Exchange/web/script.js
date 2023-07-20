function get_form() {
    var valuta = document.getElementById("number_for_konv").value;
    var in_s = document.getElementById("valuta_1").value;
    var out_s= document.getElementById("valuta_2").value;

        eel.get_course(valuta,in_s,out_s)();
}
async function updareInterface() {
    let res = await eel.get_course(valuta,in_s,out_s)();
    document.getElementById('out').innerHTML = res;
}