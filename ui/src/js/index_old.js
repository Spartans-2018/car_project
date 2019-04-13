// import '../styles/app.css';

import Service from './service';
import Plotly from 'plotly.js/dist/plotly';
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App'
//  import BudgetSearch from './src/components/BudgetSearch';



let service = new Service();


// document.querySelector('form').addEventListener('submit', function (event) {
//     console.log("Submit event track");
//     event.preventDefault();
//     service.helloWorld().then(function (result) {
//         console.log(`${result}`);
//         document.getElementById('gch').innerHTML = result;
//     }); 

// })


let carMakeHandler1 = (event) => {
    let selectElem = event.currentTarget;
    let selectedMake = selectElem.value;

    let dataMake = service.selectMake(selectedMake);

    dataMake.then(function (model) {
        console.log(`Data received ${model}`);

        var options = '<option value="">' + '--Please choose a model--' + '</option>';
        for (var i = 0; i < model.length; i++) {
            options += '<option value="' + model[i] + '">' + model[i] + '</option>';
        }

        document.getElementById('model1').innerHTML = options

    });
};

let carMakeHandler2 = (event) => {
    let selectElem = event.currentTarget;
    let selectedMake = selectElem.value;

    let dataMake = service.selectMake(selectedMake);

    dataMake.then(function (model) {
        console.log(`Data received ${model}`);

        var options = '<option value="">' + '--Please choose a model--' + '</option>';
        for (var i = 0; i < model.length; i++) {
            options += '<option value="' + model[i] + '">' + model[i] + '</option>';
        }

        document.getElementById('model2').innerHTML = options

    });
};



document.getElementById('make1')
    .addEventListener('input', carMakeHandler1);

document.getElementById('make2')
    .addEventListener('input', carMakeHandler2);


let completeSelection = (event) => {
    event.preventDefault();
    let selectE = event.currentTarget;

    var selectedMake = '';
    var selectedModel = '';
    var selectedFromYear= '';
    var selectedToYear='';
    var selectedZip='';

    let selectedMakeCar1 = selectE.make1.value;
    let selectedModelCar1 = selectE.model1.value;
    let selectedMakeCar2 = selectE.make2.value;
    let selectedModelCar2 = selectE.model2.value;



    let selectedFromyearCar1 = selectE.fromyear1.value;
    let selectedToyearCar1 = selectE.toyear1.value;
    let selectedFromyearCar2 = selectE.fromyear2.value;
    let selectedToyearCar2 = selectE.toyear2.value;


    let selectedZip1 = selectE.zip1.value;
    let selectedZip2 = selectE.zip2.value;
    

    var selectedMake = selectedMakeCar1 + ',' + selectedMakeCar2;
    var selectedModel = selectedModelCar1 + ',' + selectedModelCar2;

    var selectedYearCar1= selectedFromyearCar1+','+selectedToyearCar1;
    var selectedYearCar2= selectedFromyearCar2+','+selectedToyearCar2;
    
    var selectedZip= selectedZip1 + ','+ selectedZip2;
    

    // let searchResults = service.completeMake(selectedZip, selectedFromyear, selectedToyear, selectedMake, selectedModel);
    let searchResults = service.completeMake(selectedZip, selectedYearCar1, selectedYearCar2, selectedMake, selectedModel);

    searchResults.then(function (data) {
        console.log(data)
        // document.getElementById('gch').innerHTML=data.num_found;
        // document.getElementById('makers').innerHTML=data.listings[0].build.make;

        var trace1= {y: data.x1, x: data.y1, name: data.mm1};
        var trace2= {y: data.x2, x: data.y2, name: data.mm2};
        var data_graph=[trace1, trace2];
        let test_graph = document.getElementById('graph');

        Plotly.plot(test_graph,data_graph,
                 {
                margin: { t: 0 }
            },
            { name: "Car Prices" },
            {
                xaxis: {autorange: 'reversed'}
            }

        );

    })


}

let budgetSelection= (event)=>{
    event.preventDefault();
    let selectE=event.currentTarget;

    let selectedBudget=selectE.budget.value;
    let selectedType= selectE.type.value;
    let selectedMileage= selectE.miles.value;
    let selectedZip= selectE.zipb.value;

    let budgetResults= service.budget(selectedBudget, selectedType, selectedMileage, selectedZip);

    budgetResults.then(function(budgetData){

        // ReactDOM.render(<h1>test</h1>, document.getElementById('bmake'))
        


        
        // for (var i=0; i < budgetData.length; i++){
        //     document.getElementById('bmake').innerHTML= budgetData[i].make
        //     document.getElementById('bmodel').innerHTML= budgetData[i].model
        //     document.getElementById('bprice').innerHTML= budgetData[i].price
        //     document.getElementsByTagName('img').src= budgetData[i].photo
        // }
        
        // budgetData.num_found//needs correction
        
    })

}

document.getElementById('carform')
    .addEventListener('submit', completeSelection);

document.getElementById('budget-form')
    .addEventListener('submit', budgetSelection);






ReactDOM.render(<App />, document.getElementById("root"))





let tester = document.getElementById('tester');
// Plotly.plot( tester, [{
// 	x: [1, 2, 3, 4, 5],
// 	y: [1, 2, 4, 8, 16] }], {
// 	margin: { t: 0 } } );







// // Close the dropdown menu if the user clicks outside of it
// window.onclick = function (event) {
//     if (!event.target.matches('.dropbtn')) {
//         var dropdowns = document.getElementsByClassName("dropdown-content");
//         var i;
//         for (i = 0; i < dropdowns.length; i++) {
//             var openDropdown = dropdowns[i];
//             if (openDropdown.classList.contains('show')) {
//                 openDropdown.classList.remove('show');
//             }
//         }
//     }
// };