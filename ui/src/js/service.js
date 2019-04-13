class Service {

    constructor() {
        this.url = '/api/result'
        this.url1= '/api/search_make/'
        this.url2='/api/search/test'
        this.url3='/api/search-car/'
        this.url4='/api/search-cars/'
        this.url5='/api/search-budget/'
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

budget(zipcode, carType, milieage, budget){
    return fetch(this.url5+ zipcode+'/'+carType+'/'+milieage+'/'+budget)
    .then((response)=>{
        return response.json()
    })
}






}




     

export default Service;
