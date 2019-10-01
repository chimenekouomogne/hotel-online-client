var listesProduitparCategories = [];
$(document).ready(function () {
    var Url = '/admin/sock/api/prosuits-par-categories';
    $.ajax({
        type: 'GET',
        url: Url,
        dataType: 'json',
        contentType: 'application/json',
        success: function (result) {
            listesProduitparCategories = result;
        }
    });


});

var donnees = {
    lines: [],
    totale: 0,
    description: "",
    id_client: -1,
    id_fournisseur: -1
};
var sampleProductCategories = listesProduitparCategories;

//alert(sampleProductCategories)

function formatCurrency(value) {
    return value.toFixed(2);
}


var CartLine = function () {
    var self = this;
    self.category = ko.observable();
    self.product = ko.observable();
    self.quantity = ko.observable(1);
    self.quantity_in_stock = ko.computed(function () {
        return self.product ? parseInt("0" + self.product(), 10) : 0;
    });
    ;
    self.prix_entre = ko.observable(1);
    /*  self.subtotal = ko.computed(function() {
         return self.product() ? self.product().prix * parseInt("0" + self.quantity(), 10) : 0;
     }); */
    self.subtotal = ko.computed(function () {
        return self.prix_entre ? parseInt("0" + self.prix_entre(), 10) * parseInt("0" + self.quantity(), 10) : 0;
    });

    self.nbrefaux = ko.computed(function () {
        var res;
        if (self.product()) {
            res = self.product().quantite < self.quantity() ? 1 : 0;
        }
        return res;
    });


    // Whenever the category changes, reset the product selection
    self.category.subscribe(function () {
        self.product(undefined);
    });

};
var totale = 0;
var Cart = function () {
    // Stores an array of lines, and from these, can work out the grandTotal
    var self = this;
    self.lines = ko.observableArray([]); // Put zero line in by default -->  new CartLine()
    self.grandTotal = ko.computed(function () {
        var total = 0;
        $.each(self.lines(), function () {
            total += this.subtotal()
        })
        return total;
    });
    totale = self.grandTotal();
    self.nbrefauxTotal = ko.computed(function () {
        var total = 0;
        $.each(self.lines(), function () {
            total += this.nbrefaux()
        })
        return total;
    });

    // Operations

    self.addLine = function () {
        self.lines.push(new CartLine())
    };
    self.removeLine = function (line) {
        self.lines.remove(line)
    };
    self.removeAll = function () {
        self.lines.pop()
        var i = 0;
        ko.utils.arrayForEach(this.lines(), function (line) {

            console.log(i);
            console.log(line);
            self.lines.pop();
            i++;
        });
    }
    self.save = function () {
        //construction des donnnes a sauvegarder
        var dataToSave = $.map(self.lines(), function (line) {
            return line.product() ? {
                productId: line.product().id,
                productName: line.product().nom,
                quantite: line.quantity(),
                subtotal: line.subtotal(),
                prix_entre: line.prix_entre()
            } : undefined
        });
        donnees.lines = dataToSave;
        donnees.totale = parseFloat(document.getElementById("totale").innerText);
        donnees.description = document.getElementById("description").value;
        self.donne = ko.observable(donnees);
        /*--------------fin construction des donneees a sauvegarder-------------------------*/

        //reinitialisation liste a vide et preparation du message de nautification succes ou echec
        document.getElementById("description").value = "";
        self.removeAll();
        //location.reload(true);
        //ajout id client
        if (document.getElementById("id_client").value != -1) {
            donnees.id_client = document.getElementById("id_client").value;
        }
        if (document.getElementById("id_fournisseur").value != -1) {
            donnees.id_client = document.getElementById("id_fournisseur").value;
        }
        /* alert("Could now save this to server: " + JSON.stringify(dataToSave));
         alert("1------\n: "+JSON.stringify(donnees));
         alert("2------\n: "+ko.toJSON(donnees));*/

        // Customize the document to send ajax request properly to handle csrf issue
        /* $(function () {
             var token = $("meta[name='_csrf']").attr("content");
             var header = $("meta[name='_csrf_header']").attr("content");
             alert(header);
             alert(token)
             $(document).ajaxSend(function (e, xhr, options) {
                 xhr.setRequestHeader(header, token);
             });
         });
 */
        //ajouter avant de s controle sur la presence d'une description, prixtotal > 0


        //choix de l'action a mener
        if ($('#action').val() === "entree") {
            $.ajax({
                url: " /admin/sock/api/entree/ajouter",
                method: "POST",
                traditional: true,
                data: {
                    resultats: ko.toJSON(donnees)
                },
                success: function () {
                    //after saving the mark delete the current node row table into the current table
                    self.removeAll();
                    $('#message').show();
                    //alert(" enregistrée avec succès ! success");
                    //vider les entree
                    // self.removeAll();

                },
                error: function (e) {
                    alert(" enregistrement non effectuer ! error");
                }
            });
        } else if ($('#action').val() === "sortie") {
            $.ajax({
                url: " /admin/sock/api/sortie/ajouter",
                method: "POST",
                traditional: true,
                data: {
                    resultats: ko.toJSON(donnees)
                },
                success: function () {
                    //after saving the mark delete the current node row table into the current table
                    self.removeAll();
                    $('#message').show();
                    //alert(" enregistrée avec succès ! success");
                },
                error: function (e) {
                    alert(" enregistrement non effectuer ! error");
                }
            });

        } else if ($('#action').val() === "vente") {
            $.ajax({
                url: " /admin/sock/api/vente/ajouter",
                method: "POST",
                traditional: true,
                data: {
                    resultats: ko.toJSON(donnees)
                },
                success: function () {
                    //after saving the mark delete the current node row table into the current table
                    self.removeAll();
                    //alert(" enregistrée avec succès ! success");
                    $('#message').show();
                },
                error: function (e) {
                    alert(" enregistrement non effectuer ! error");
                }
            });

        }

        //verifier que la quantite entree n'est pas superieur a celle en stock
        $('.qte').on("keypress keyup blur", function (event) {
            //alert($(this).val());
            // alert($('.qte_stock').text());

            //  alert(parseInt($(this).val()) >  parseInt($('#qte_stock').text()));

            if (parseInt($(this).val()) > parseInt($('#qte_stock').text())) {

                $(this).addClass("text-danger");
                $(this).val(0);
            } else {
                $(this).addClass("text-success");
            }

            if ((event.which < 48 || event.which > 57)) {
                event.preventDefault();
            }
        });


    };
};

ko.applyBindings(new Cart());