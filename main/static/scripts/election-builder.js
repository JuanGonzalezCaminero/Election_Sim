let districts = [];

function val(id){
    return document.getElementById(id).value;
}

function ival(id){
    return parseInt(val(id));
}

function fval(id){
    return parseFloat(val(id));
}

function genOutput(){
    let output = {
        date: val("election-date").toString(),
        type: val("election-type"),
        configuration: {
            threshold: fval("election-threshold")
        },
        districts: districts
    };
    return output;
}

function updateDistricts(){
    let districtTable = document.getElementById("district-inside-table");
    districtTable.remove();
    districtTable = document.createElement("table");
    districtTable.id = "district-inside-table";
    districtTable.innerHTML = `
    <tr>
    <th>Nombre</th>
    <th>Censo</th>
    <th>Escaños</th>
    <th>Votos en blanco</th>
    <th>Votos nulos</th>
    <th>Candidaturas</th>
    <th>¿Borrar?</th>
    </tr>`;

    document.getElementById("district-table").appendChild(districtTable);

    districts.forEach((district, i)=>{
        let row = document.createElement("tr");
        row.innerHTML = `
        <td>${district.name}</td>
        <td>${district.voters}</td>
        <td>${district.representatives}</td>
        <td>${district.blank}</td>
        <td>${district.null}</td>
        <td><button data-id="${i}" class="view-district">Ver</td>
        <td><button data-id="${i}" class="delete-district">Borrar</button></td>
        `;
        districtTable.appendChild(row);
    });

    let viewButtons = document.querySelectorAll(".view-district");
    viewButtons.forEach((button)=>{
        button.addEventListener("click", ()=>{
            let newCandidature = document.getElementById("new-candidature");
            newCandidature.disabled = false;
            newCandidature.dataset.id = button.dataset.id;
            updateCandidatures();
        });
    });

    let deleteButtons = document.querySelectorAll(".delete-district");
    deleteButtons.forEach((button)=>{
        button.addEventListener("click",()=>{
            districts.splice(button.dataset.id, 1);
            updateDistricts();
        });
        
    });
}

function updateCandidatures(){
    let newCandidature = document.getElementById("new-candidature");
    let candidatureTable = document.getElementById("candidature-inside-table");
    candidatureTable.remove();
    candidatureTable = document.createElement("table");
    candidatureTable.id = "candidature-inside-table";
    candidatureTable.innerHTML = `
    <tr>
    <th>Nombre</th>
    <th>Abreviatura</th>
    <th>Votos</th>
    <th>¿Borrar?</th>
    </tr>`;
    document.getElementById("candidature-table").appendChild(candidatureTable);

    let candidature_id = newCandidature.dataset.id;

    districts[candidature_id].candidatures.forEach((candidature, i)=>{
        let row = document.createElement("tr");
        row.innerHTML = `
        <td>${candidature.name}</td>
        <td>${candidature.abbr}</td>
        <td>${candidature.votes}</td>
        <td><button data-id="${i}" class="delete-candidature">Borrar</button></td>
        `;
        candidatureTable.appendChild(row);
    });

    let deleteButtons = document.querySelectorAll(".delete-candidature");
    deleteButtons.forEach((button)=>{
        button.addEventListener("click",()=>{
            districts[candidature_id].candidatures.splice(button.dataset.id, 1);
            updateCandidatures();
        });
        
    });
}

function main(){
    let dialogs = document.querySelectorAll("dialog");
    dialogs.forEach((dialog)=>{
        dialogPolyfill.registerDialog(dialog);
    });

    let newDistrict = document.getElementById("new-district"); 
    let dialogDistrict = document.getElementById("dialog-district");
    newDistrict.addEventListener("click",()=>{
        dialogDistrict.showModal();
    });

    let addDistrict = document.getElementById("add-district");
    addDistrict.addEventListener("click",()=>{
        districts.push({
            name: val("district-name"),
            voters: ival("district-voters"),
            representatives: ival("district-representatives"),
            blank: ival("district-blank"),
            null: ival("district-null"),
            candidatures: []
        });
        updateDistricts();
        dialogDistrict.close();
    });

    let cancelDistrict = document.getElementById("cancel");
    cancelDistrict.addEventListener("click", ()=>{
        dialogDistrict.close();
    });

    let newCandidature = document.getElementById("new-candidature");
    let dialogCandidature = document.getElementById("dialog-candidature");
    newCandidature.addEventListener("click", ()=>{
        dialogCandidature.showModal();
    });

    let addCandidature = document.getElementById("add-candidature");
    addCandidature.addEventListener("click", () => {
        let candidature_id = newCandidature.dataset.id;
        districts[candidature_id].candidatures.push({
            name: val("candidature-name"),
            abbr: val("candidature-abbrv"),
            votes: ival("candidature-votes")
        });
        updateCandidatures();
        dialogCandidature.close();
    });

    let cancelCandidature = document.getElementById("cancel-candidature");
    cancelCandidature.addEventListener("click", ()=>{
       dialogCandidature.close(); 
    });

    let exportButton = document.getElementById("export");
    exportButton.addEventListener("click", ()=>{
        let output = genOutput();
        let json = JSON.stringify(output);
        let a = document.createElement("a");
        let blob = new Blob([json], {type: "application/json"});
        a.href = window.URL.createObjectURL(blob);
        a.download = "election.json";
        a.click();
    });

    let uploadButton = document.getElementById("load");
    let dialogUpload = document.getElementById("load-dialog");
    uploadButton.addEventListener("click", ()=>{
        dialogUpload.showModal();
    });

    let cancelLoad = document.getElementById("cancel-load");
    cancelLoad.addEventListener("click", ()=>{
       dialogUpload.close(); 
    });

    let calculateButton = document.getElementById("calculate");
    calculateButton.addEventListener("click", ()=>{
        let token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
        let output = genOutput();
        let json = JSON.stringify(output);
        let blob = new Blob([json], {type: "application/json"});

        let form = new FormData();
        form.append("csrfmiddlewaretoken", token);
        form.append("file",blob);
        form.append("method", "ajax");

        let req = new XMLHttpRequest();
        req.open("POST", "/");
        req.send(form);
        req.addEventListener("load",()=>{
            window.location.href = "/results/"+req.response;
        })
    });
}

window.addEventListener("load", main);