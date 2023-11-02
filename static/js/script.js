document.addEventListener('DOMContentLoaded', function(){
    var template = document.getElementById('template');
    var rank = document.getElementById('rank');
    var projectTitle = document.getElementById('projectTitle');
    var cwa = document.getElementById('cwa');
    var position = document.getElementById('position');

    template.addEventListener("change", function() {
        if (template.value === "firstClassExcellent"){
            projectTitle.style.display = "block";
            cwa.style.display = "block";
            rank.style.display = "none";
            position.style.display = "none";

        } else if (template.value === "firstClassOrdinary"){
            rank.style.display = "block";
            projectTitle.style.display = "none";
            cwa.style.display = "none";
            position.style.display = "none";

        } else if (template.value === "upperExcellent"){
            rank.style.display = "none";
            projectTitle.style.display = "block";
            cwa.style.display = "none";
            position.style.display = "block";

        }
        else {
            rank.style.display = "none"
            projectTitle.style.display = "none"
            cwa.style.display = "none";
            position.style.display = "none";
        }
    });
});