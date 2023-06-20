const express = require("express");
const server = express();
const suporte = require("./suporte");


server.get("/", async (req, res) => {
		  
		  
	try{	  
		  
	const title = req.query.title;
	const message = req.query.message;
	const login = req.query.login;
		

    if (title != null && message  != null && login  != null ){
        await suporte.start_glpi(title , message , login).then((x) => {
			
			console.log(x);
		
            return;
			
        }).catch((err) => {
			
            console.log("Ocorreu algum erro ao tentar criar o chamado " + err);
			
			return;
			
        })	       
		
    
	} else {
		
        console.log("Campos enviados incorretamente");       
		return;
		
    }   
	
	}catch(err){
		console.log(err)	
		return
	}
	
    
});



	
server.listen(2000, () => {
    console.log("Servidor iniciado")
})


