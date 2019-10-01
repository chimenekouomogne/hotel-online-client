function onValidQuanity() {

    qtev = document.getElementById('qtev').value;
    qte = document.getElementById('quantite').value
    console.log("quantite en stock : " + qte);
    console.log("quantite en vendu : " + qtev);

    if (parseInt(qtev) <= parseInt(qte)) {
        console.log("good value! ");
        document.getElementById('error').innerText = "";
        document.getElementById('ajouter').style.display = 'inline-block';
    } else {
        console.log("bad value! please correct it");
        document.getElementById('error').innerText = "La quantite vendu doit etre inferieur a la quantite en stock";
        document.getElementById('ajouter').style.display = 'none';

    }
}