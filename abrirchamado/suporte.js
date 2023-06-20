const puppeteer = require('puppeteer');

(async()=>{
	browser = await puppeteer.launch({headless:false});		
})();

	

	
async function start_glpi(title, message, login){
					
	try{	
		
	console.log("CRIANDO CHAMADO");
	var pagina = await browser.newPage();
	await pagina.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36');
	await pagina.setViewport({width:800, height:600});				
	await pagina.goto("http://suporteti.cisbaf.org.br/"); 			
				
		const password = "Cisbaf2023";

		const botaoLogin = await pagina.waitForSelector("button[type='submit']",{timeout:5000}).catch(()=>{return});
			if(botaoLogin){				

				if(!login || login == ""){
					login = "Cisbot";					
				}

			console.log("login inserido:"+login);
			console.log("senha:"+password);
				await pagina.type('#login_name', login);
				await pagina.type('input[type="password"]', password);

				await pagina.evaluate(async()=>{
					await document.querySelector("button").click();				
				})
			}	


	new Promise((resolve,reject)=>{
				setTimeout(resolve,2000)
		}).then(async()=>{
				

await pagina.goto("http://suporteti.cisbaf.org.br/front/helpdesk.public.php?create_ticket=1");
		
            await pagina.waitForSelector("input[name='name']",{timeout:2000});
			await pagina.type("input[name='name']", title);
               			
			const elementHandle = await pagina.waitForSelector('iframe',{timeout:3000})
			const iframe = await elementHandle.contentFrame();

			await iframe.waitForSelector('p');
			
			await iframe.evaluate(function(message){	
			
				document.querySelector('p').innerHTML=message;
								
			},message)	

	
	
			await pagina.evaluate(async()=>{			
				
				await new Promise((resolve,reject)=>{
					setInterval(async()=>{
						await document.querySelectorAll("button[type='submit']")[0].click();
						resolve();
					},2000)
				}).then(()=>{
					return
				})			
				
			})

			new Promise((resolve,reject)=>{
				setTimeout(resolve,4000)
			}).then(async()=>{
				await pagina.close();
			})




	})	

			
			

		return "Chamado aberto com sucesso";
	


	}catch(err){		
		await pagina.close();
		return err.toString();		
 	}
	
}


async function create_login(_login, _nome, _sobrenome){
					
	try{	
		
	const pagina = await browser.newPage();
	await pagina.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36');
	//await pagina.setViewport({width:1280, height:768});				
	await pagina.goto("http://suporteti.cisbaf.org.br/"); 			
								
		const botaoLogin = await pagina.waitForSelector("button[type='submit']",{timeout:5000}).catch(()=>{return});
			if(botaoLogin){		
				await pagina.type('#login_name', "Admin");
				await pagina.type('input[type="password"]', "!@7890380!@");

				await pagina.evaluate(async()=>{
					await document.querySelector("button").click();				
				})
			}	


			var button_openTab = await pagina.waitForSelector("body > div.page > aside > div > button",{timeout:7000})
			if(button_openTab){
				await button_openTab.click()
			}else{
				throw new Error("Button new Tab not found")
			}			
			
			await pagina.goto("http://suporteti.cisbaf.org.br/front/user.form.php");
			

			var login = await pagina.waitForSelector("input[name='name']");
			await login.type(_login);

			var sobrenome = await pagina.waitForSelector("input[name='realname']");
		    await sobrenome.type(_sobrenome);

			var name = await pagina.waitForSelector("input[name='firstname']");
			await name.type(_nome)

			var password = await pagina.$("#password");
			await password.type("Cisbaf2023");

			var password2 = await pagina.$("#password2");
			await password2.type("Cisbaf2023");
	
			await pagina.evaluate(()=>{				
				document.querySelectorAll(".select2-selection__rendered > span")[5].innerText = "Usuário";
			})

			
			await pagina.evaluate(async()=>{
				await document.querySelector("button[type='submit']").click();	
				
				setTimeout(async()=>{
					await document.querySelector("button[type='submit']").click();
				},2000)
			})
	
		
		setTimeout(async()=>{
			await pagina.close();
		},4000)

		return "Login criado";
	
	}catch(err){		
		await pagina.close();
		return err.toString();		
 	}
}

module.exports = {start_glpi, create_login};
