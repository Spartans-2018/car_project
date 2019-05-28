class Service {

    constructor() {
        this.url = '/api/result'
        this.url1= '/api/search_make/'
        this.url2='/api/search/test'
        this.url3='/api/search-car/'
        this.url4='/api/search-cars/'
        this.url5='/api/search-budget/'
        this.url6= '/api/search-newcar/'
        this.url7= '/api/search-budget/anymileage/'
    }
    /**-
     * Making a remote call using promises
     */

    helloWorld(){
        //  console.log('Func working');
         return fetch(this.url)
         .then((response) => {
             return response.text()
             })
        
         
     }

     selectMake(make){
        return fetch(this.url1+make)
        .then((response)=>{
            return response.json()
        })
    }


completeMake(zipcode, fromyear, toyear, make, model){
    return fetch(this.url4+ zipcode+'/'+fromyear+'/'+toyear+'/'+make+'/'+model)
    .then((response)=>{
        return response.json()
    })
}

budget(zipcode, carType, milieage, budget, color){
    return fetch(this.url5+ zipcode+'/'+carType+'/'+milieage+'/'+budget+'/'+color)
    .then((response)=>{
        return response.json()
    })
}
budgetAnyMileage(zipcode, carType, budget, color){
    return fetch(this.url7+ zipcode+'/'+carType+'/'+'/'+budget+'/'+color)
    .then((response)=>{
        return response.json()
    })
}

newCarSearch(make, model, zipcode){
    return fetch(this.url6 +make+'/'+model +'/'+ zipcode)
        .then(response =>{
            return response.json()
        })
    
}





}


     

export default Service;
